"""tinker-cookbook's RL loop on a Loop run (#724).

:class:`LoopRLDataset` turns P3.9's Tinker JSONL rows into :class:`LoopEnvGroupBuilder`
groups. Each env is the cookbook's own tool env (``build_agent_tool_env``) whose tools run
in a Loop rollout of the run ``O11Y_RUN``, and each trajectory's whole reward is that
rollout's verifier reward, added by ``compute_group_rewards`` however the episode ended.
A task's or verifier's failure keeps its value; our failure (``INFRASTRUCTURE``) raises
:class:`~o11y_one.sdk.loop._core.LoopInfrastructureFailure`, so the group is never scored.

Sampling and training stay Tinker's: this module never imports ``tinker`` nor reads
``TINKER_API_KEY``. Needs the ``tinker`` extra: ``pip install 'o11y-one[tinker]'``.
"""

from __future__ import annotations

import asyncio
import contextlib
import copy
import importlib.metadata
import uuid
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any

try:
    from tinker_cookbook.renderers import get_renderer
    from tinker_cookbook.rl.types import Env, EnvGroupBuilder, RLDataset, Trajectory
    from tinker_cookbook.tokenizer_utils import get_tokenizer
    from tinker_cookbook.tool_use.agent_tool_message_env import build_agent_tool_env
    from tinker_cookbook.tool_use.tools import error_tool_result
    from tinker_cookbook.tool_use.types import ToolInput, ToolResult
except ModuleNotFoundError as error:
    raise ImportError(
        "o11y_one.sdk.loop.tinker needs the tinker extra: pip install 'o11y-one[tinker]'"
    ) from error

from . import _SDK_VERSION, AsyncLoopClient, _core

__all__ = ["LoopEnvGroupBuilder", "LoopRLDataset"]

_COOKBOOK = importlib.metadata.version("tinker-cookbook")


class _Rollout:
    """One env's Loop rollout, reset at its first use: the extra envs a retry's
    ``make_envs`` makes are never started, so never billed."""

    def __init__(self, fields: dict[str, Any], client: dict[str, Any]) -> None:
        self.client = AsyncLoopClient(
            adapter=__name__,
            adapter_version=_SDK_VERSION,
            framework_version=_COOKBOOK,
            **client,
        )
        self._fields, self._lock, self.started = fields, asyncio.Lock(), False

    async def open(self) -> AsyncLoopClient:
        async with self._lock:
            if not self.started:
                self.started = True
                await self.client.reset(**self._fields)
        return self.client

    async def close(self):
        await self.open()  # a rollout that never called a tool is still graded
        return await self.client.close()


@dataclass
class _LoopTool:
    """One of the core tools, on its env's rollout; the cookbook's ``Tool`` protocol."""

    spec: dict[str, Any]
    rollout: _Rollout | None

    @property
    def name(self) -> str:
        return self.spec["name"]

    @property
    def description(self) -> str:
        return self.spec["description"]

    @property
    def parameters_schema(self) -> dict[str, Any]:
        return self.spec["parameters"]

    def to_spec(self) -> dict[str, Any]:
        return dict(self.spec)

    async def run(self, input: ToolInput) -> ToolResult:
        call_id = input.call_id or ""
        try:
            call = _core.to_call(self.name, input.arguments)
        except (ValueError, KeyError, AttributeError) as error:
            return error_tool_result(str(error), call_id=call_id, name=self.name)
        client = await self.rollout.open()
        (result,) = (await client.step([call])).results
        message = {"role": "tool", "content": _core.render(result), "tool_call_id": call_id}
        return ToolResult(messages=[{**message, "name": self.name}])


def _tools(rollout: _Rollout | None) -> list[_LoopTool]:
    return [_LoopTool(tool["function"], rollout) for tool in _core.TOOLS]


async def _no_reward(messages: list) -> tuple[float, dict[str, float]]:
    return 0.0, {}  # the verifier's reward comes in compute_group_rewards


@dataclass
class LoopEnvGroupBuilder(EnvGroupBuilder):
    """A GRPO group of one case: ``group_size`` envs, one Loop group. Only strings and
    numbers, so it pickles; the key is read from ``O11Y_API_KEY`` when the envs are made.
    ``base_url`` ``None`` means ``O11Y_BASE_URL``, else Loop's own."""

    messages: list[dict[str, Any]]
    group_size: int
    trainer_step: int
    model_name: str
    renderer_name: str
    case_revision_id: str = ""
    trainer_total_steps: int = 0
    max_turns: int = 8
    base_url: str | None = None
    _group_id: str = field(default="", init=False)
    _rollouts: dict[int, _Rollout] = field(default_factory=dict, init=False, repr=False)

    def __getstate__(self) -> dict[str, Any]:
        return {**self.__dict__, "_rollouts": {}}  # live connections never pickle

    async def make_envs(self) -> Sequence[Env]:
        # A retry's fresh envs join the same group.
        self._group_id = self._group_id or str(uuid.uuid4())
        tokenizer = get_tokenizer(self.model_name)
        envs = []
        for index in range(self.group_size):
            # ponytail: a tokenizer per env. The cookbook renders envs in threads, and its Qwen3
            # renderer flips the shared HF tokenizer's split_special_tokens per call, which
            # races ("Already borrowed"). Share one again once the cookbook guards that.
            renderer = get_renderer(self.renderer_name, copy.deepcopy(tokenizer))
            specs = [tool.to_spec() for tool in _tools(None)]
            prefix = renderer.create_conversation_prefix_with_tools(specs)
            fields = {
                "group_id": self._group_id,
                "group_index": index,
                "group_size": self.group_size,
                "trainer_step": self.trainer_step,
                "trainer_total_steps": self.trainer_total_steps,
            }
            if self.case_revision_id:
                fields["case_revision_id"] = self.case_revision_id
            rollout = _Rollout(fields, {"base_url": self.base_url})
            env = build_agent_tool_env(
                renderer,
                _tools(rollout),
                [*prefix, *self.messages],
                _no_reward,
                max_turns=self.max_turns,
                failed_parse_reward=0.0,  # the verifier is the only score
            )
            self._rollouts[id(env)] = rollout
            envs.append(env)
        return envs

    async def compute_group_rewards(
        self, trajectory_group: list[Trajectory], env_group: Sequence[Env]
    ) -> list[tuple[float, dict[str, float]]]:
        rollouts = [self._rollouts[id(env)] for env in env_group]
        closed = await asyncio.gather(*(rollout.close() for rollout in rollouts))
        rewards = [_core.reward(each) for each in closed]
        for each, reward in zip(closed, rewards, strict=True):
            if reward is None:
                raise _core.LoopInfrastructureFailure(
                    f"rollout {each.rollout_id} failed on Loop's side; its group is not scored"
                )
        return [(reward, {"loop/reward": reward}) for reward in rewards]

    async def cleanup(self) -> None:
        open_rollouts = [r for r in self._rollouts.values() if r.started and r.client.rollout_id]
        for rollout in open_rollouts:
            with contextlib.suppress(Exception):
                await rollout.client.close()

    def logging_tags(self) -> list[str]:
        return ["loop"]


class LoopRLDataset(RLDataset):
    """P3.9's Tinker JSONL rows (``{"messages", "loop": {"case_revision_id"}}``), each a
    group of ``group_size``, ``batch_size`` groups a step; step ``i`` is batch ``i``."""

    def __init__(
        self,
        rows: list[dict[str, Any]],
        *,
        batch_size: int,
        group_size: int,
        model_name: str,
        renderer_name: str,
        max_turns: int = 8,
        base_url: str | None = None,
    ) -> None:
        self.rows, self.batch_size, self.group_size = rows, batch_size, group_size
        self.model_name, self.renderer_name = model_name, renderer_name
        self.max_turns, self.base_url = max_turns, base_url

    def __len__(self) -> int:
        return len(self.rows) // self.batch_size

    def get_batch(self, index: int) -> Sequence[LoopEnvGroupBuilder]:
        rows = self.rows[index * self.batch_size : (index + 1) * self.batch_size]
        return [
            LoopEnvGroupBuilder(
                messages=row["messages"],
                group_size=self.group_size,
                trainer_step=index,
                model_name=self.model_name,
                renderer_name=self.renderer_name,
                case_revision_id=row.get("loop", {}).get("case_revision_id", ""),
                trainer_total_steps=len(self),
                max_turns=self.max_turns,
                base_url=self.base_url,
            )
            for row in rows
        ]
