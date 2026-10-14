"""OpenRLHF's agent executor on a Loop run (#934). Point OpenRLHF at this file::

    --train.agent_func_path $(python -c 'import o11y_one.sdk.loop.openrlhf as m; print(m.__file__)')

OpenRLHF loads it by path, so every import here is absolute. Each sample is one rollout
of the run ``O11Y_RUN``, of the case its label's JSON names. A turn's tool calls run in
Loop's VM as one step, and the sample's reward is the Loop verifier's primary reward,
set when its rollout closes. A task's or verifier's failure keeps its value; our failure
(``INFRASTRUCTURE``) re-runs the sample once.

The prompts carry the tool schemas: render them with :func:`render_prompts` and train
without ``--data.apply_chat_template``. OpenRLHF has no extra (its wheel pins CUDA builds);
this module checks the installed release instead.
"""

from __future__ import annotations

import importlib.metadata
import json
import re
from contextvars import ContextVar
from pathlib import Path
from types import SimpleNamespace
from typing import Any

#: The OpenRLHF releases this adapter is tested on: 0.11.2 up to 0.12.
SUPPORTED = ((0, 11, 2), (0, 12))
try:
    _installed = importlib.metadata.version("openrlhf")
except importlib.metadata.PackageNotFoundError:
    _installed = "none"
_release = tuple(int(part) for part in re.findall(r"\d+", _installed)[:3])
if not SUPPORTED[0] <= _release < SUPPORTED[1]:
    raise ImportError(f"o11y_one.sdk.loop.openrlhf needs openrlhf 0.11.2 to 0.12, not {_installed}")

import torch  # noqa: E402
from o11y_one.sdk.loop import _SDK_VERSION, AsyncLoopClient, _core  # noqa: E402
from openrlhf.utils.agent import AgentInstanceBase, MultiTurnAgentExecutor  # noqa: E402

__all__ = ["AgentExecutor", "LoopAgentInstance", "render_prompts"]

_TOOL_CALL = re.compile(r"<tool_call>(.*?)</tool_call>", re.DOTALL)
_MARK = "<<o11y-loop-turn>>"
_MAX_CALLS = 16  # Loop's calls per step
# The sample's tokenizer and its rollout, for the instance OpenRLHF makes inside execute.
_sample: ContextVar[SimpleNamespace] = ContextVar("o11y_one_loop_sample")


def render_prompts(rows: Path, out: Path, tokenizer: Any) -> None:
    """P3.9's OpenRLHF JSONL, each ``prompt`` rendered by ``tokenizer``'s chat template
    with the core tools, as OpenRLHF never passes ``tools=``."""
    with Path(rows).open() as lines, Path(out).open("w") as written:
        for line in lines:
            row = json.loads(line)
            row["prompt"] = tokenizer.apply_chat_template(
                row["prompt"], tools=_core.TOOLS, add_generation_prompt=True, tokenize=False
            )
            written.write(json.dumps(row) + "\n")


def _tool_turn(tokenizer: Any, texts: list[str]) -> str:
    """The chat template's tool turn after the model's, to its next assistant turn, less
    the end-of-turn token the model's own tokens already end with."""
    turn = [{"role": "user", "content": "-"}, {"role": "assistant", "content": _MARK}]
    tools = [{"role": "tool", "content": text} for text in texts]
    end = tokenizer.apply_chat_template(turn, tokenize=False).split(_MARK, 1)[1].rstrip()
    rendered = tokenizer.apply_chat_template(
        turn + tools, tokenize=False, add_generation_prompt=True
    )
    return rendered.split(_MARK, 1)[1].removeprefix(end)


class LoopAgentInstance(AgentInstanceBase):
    """One sample's rollout: reset at the sample's start, a step per turn with tool calls."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    async def reset(self, states: dict, **kwargs: Any) -> dict:
        case = json.loads(states["label"] or "{}").get("case_revision_id")
        sample = _sample.get()
        sample.client = AsyncLoopClient(
            adapter="o11y_one.sdk.loop.openrlhf",  # OpenRLHF loads it as agent_module
            adapter_version=_SDK_VERSION,
            framework_version=_installed,
        )
        await sample.client.reset(**({"case_revision_id": case} if case else {}))
        return {"observation": states["observation"]}

    async def step(self, states: dict, **kwargs: Any) -> dict:
        action, sample = states["action_text"], _sample.get()
        found = _TOOL_CALL.findall(action)
        if not found:
            return {"rewards": torch.tensor(0.0), "environment_feedback": "", "done": True}
        texts: list[str | None] = []
        calls = []
        for raw in found:
            try:
                parsed = json.loads(raw)
                call = _core.to_call(parsed["name"], parsed.get("arguments", {}))
            except (ValueError, KeyError, TypeError, AttributeError):
                texts.append("error: tool_call_invalid")
                continue
            if len(calls) == _MAX_CALLS:
                texts.append("error: too many tool calls in one turn")
                continue
            texts.append(None)
            calls.append(call)
        if calls:
            message = json.dumps({"role": "assistant", "content": action})
            results = iter((await sample.client.step(calls, model_message=message)).results)
            texts = [text if text is not None else _core.render(next(results)) for text in texts]
        feedback = _tool_turn(sample.tokenizer, texts)
        return {"rewards": torch.tensor(0.0), "environment_feedback": feedback, "done": False}


class AgentExecutor(MultiTurnAgentExecutor):
    """OpenRLHF's multi-turn executor, whose sample's reward is its Loop rollout's."""

    def __init__(self) -> None:
        super().__init__(LoopAgentInstance)

    async def execute(
        self, prompt, label, sampling_params, max_length, hf_tokenizer, llm_engine, images=None
    ):
        for _ in range(2):  # our failure re-runs once
            sample = SimpleNamespace(tokenizer=hf_tokenizer, client=None)
            token = _sample.set(sample)
            try:
                response = await super().execute(
                    prompt, label, sampling_params, max_length, hf_tokenizer, llm_engine, images
                )
            finally:
                _sample.reset(token)
                closed = sample.client and await sample.client.close()
            reward = _core.reward(closed)
            if reward is not None:
                response["reward"] = response["scores"] = reward
                return response
        raise _core.LoopInfrastructureFailure(
            f"rollout {closed.rollout_id} failed on Loop's side, twice"
        )
