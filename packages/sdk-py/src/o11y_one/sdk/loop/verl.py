"""verl's agent loop on a Loop run.

Rows name ``agent_name: loop``, and verl loads :class:`LoopAgentLoop` from this
package's agent-loop config::

    actor_rollout_ref.rollout.agent.agent_loop_config_path=$(python -m o11y_one.sdk.loop.verl)

Each trajectory is one rollout of the run ``O11Y_RUN``: verl's ``uid`` is its
group, its tool calls run in Loop's VM, and its ``reward_score`` is the Loop
verifier's primary reward. A task's or verifier's failure keeps its value; our
failure (``INFRASTRUCTURE``) re-runs the trajectory once.

verl's SFT trainer reads Loop's verl trajectory export with :class:`LoopSFTDataset`::

    data.custom_cls.path=pkg://o11y_one.sdk.loop.verl data.custom_cls.name=LoopSFTDataset

Needs the ``verl`` extra: ``pip install 'o11y-one[verl]'``.
"""

from __future__ import annotations

import functools
import itertools
import json
from contextvars import ContextVar
from pathlib import Path
from typing import Any

try:
    import pandas as pd
    import verl
    from verl.experimental.agent_loop.agent_loop import AgentLoopOutput, ToolListWrap
    from verl.experimental.agent_loop.tool_agent_loop import ToolAgentLoop
    from verl.tools.base_tool import BaseTool
    from verl.tools.schemas import OpenAIFunctionToolSchema, ToolResponse
    from verl.utils.dataset.multiturn_sft_dataset import MultiTurnSFTDataset
except ModuleNotFoundError as error:
    raise ImportError(
        "o11y_one.sdk.loop.verl needs the verl extra: pip install 'o11y-one[verl]'"
    ) from error

from . import _SDK_VERSION, AsyncLoopClient, _core
from ._core import LoopInfrastructureFailure

__all__ = ["CONFIG", "LoopAgentLoop", "LoopInfrastructureFailure", "LoopSFTDataset"]

#: verl's ``agent_loop_config_path`` for :class:`LoopAgentLoop`.
CONFIG = Path(__file__).with_name("verl.yaml")

_rollout: ContextVar[AsyncLoopClient] = ContextVar("o11y_one_loop_rollout")
#: The uids whose group-index counters a worker keeps; a step holds far fewer.
UIDS_KEPT = 1 << 16


@functools.lru_cache(maxsize=UIDS_KEPT)
def _counter(uid: str) -> itertools.count:
    return itertools.count()


class _LoopTool(BaseTool):
    """One of the core tools, run on the trajectory's open rollout."""

    async def execute(
        self, instance_id: str, parameters: dict[str, Any], **kwargs: Any
    ) -> tuple[ToolResponse, float, dict]:
        message = json.dumps(kwargs["agent_data"].messages[-1])
        call = _core.to_call(self.name, parameters)
        (result,) = (await _rollout.get().step([call], model_message=message)).results
        return ToolResponse(text=_core.render(result)), 0.0, {}


@functools.cache
def _tools() -> ToolListWrap:
    # Once per worker, not per trajectory: a BaseTool prints its schema when made.
    return ToolListWrap(
        [_LoopTool({}, OpenAIFunctionToolSchema.model_validate(t)) for t in _core.TOOLS]
    )


class LoopAgentLoop(ToolAgentLoop):
    """verl's ``ToolAgentLoop`` with the core tools on a Loop rollout. ``run`` and
    ``base_url`` beside ``_target_`` in the agent-loop config go to
    :class:`AsyncLoopClient`; the key never does, so it never sits in a config."""

    def __init__(self, *args: Any, tools: Any = None, **kwargs: Any) -> None:
        client = {key: kwargs.pop(key) for key in ("run", "base_url") if key in kwargs}
        super().__init__(*args, tools=_tools(), **kwargs)
        self._client = client

    async def run(self, sampling_params: dict[str, Any], **kwargs: Any) -> AgentLoopOutput:
        uid, n = kwargs["uid"], self.rollout_config.n
        fields = {
            "group_id": uid,
            "group_index": next(_counter(uid)) % n,
            "group_size": n,
            "experiment_name": self.config.trainer.get("experiment_name", ""),
        }
        loop = ((kwargs.get("extra_info") or {}).get("loop")) or {}
        if case := loop.get("case_revision_id"):
            fields["case_revision_id"] = case
        for _ in range(2):  # our failure re-runs once
            client = AsyncLoopClient(
                adapter=__name__,
                adapter_version=_SDK_VERSION,
                framework_version=verl.__version__,
                **self._client,
            )
            await client.reset(**fields)
            rollout_id, token = client.rollout_id, _rollout.set(client)
            try:
                output = await super().run(sampling_params, **kwargs)
            finally:
                _rollout.reset(token)
                closed = await client.close()
            output.reward_score = _core.reward(closed)
            if output.reward_score is not None:
                return output
        raise LoopInfrastructureFailure(f"rollout {rollout_id} failed on Loop's side, twice")


class LoopSFTDataset(MultiTurnSFTDataset):
    """verl's ``MultiTurnSFTDataset`` for Loop's verl trajectory export, whose ``tools`` and
    each call's ``arguments`` are JSON text: they are parsed once, as the files load."""

    def _read_files_and_process(self) -> None:
        super()._read_files_and_process()
        self.messages = [_core.sft_messages(messages) for messages in self.messages]
        # Each item's messages are read from its frame row, not from self.messages.
        column = pd.Series(self.messages, dtype=object).to_numpy()
        self.dataframe[self.messages_key] = column
        if self.tools is not None:
            self.tools = [json.loads(t) if isinstance(t, str) else None for t in self.tools]


if __name__ == "__main__":
    print(CONFIG)
