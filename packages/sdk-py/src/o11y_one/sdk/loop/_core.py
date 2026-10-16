"""What every trainer adapter shares: three tools, their Loop calls and results as
text, the reward rule, and a trajectory export's messages as a chat template takes
them. ``exec``, ``list``, ``patch`` and ``set_env`` are reachable through ``shell``."""

from __future__ import annotations

import contextlib
import json
from collections.abc import Mapping

from o11y_one.agentic.v1.rollout_pb2 import (
    LoopFailureClassV1,
    LoopRolloutV1,
    LoopToolCallV1,
    LoopToolReadFileV1,
    LoopToolResultV1,
    LoopToolShellV1,
    LoopToolWriteFileV1,
)

#: Each tool call's timeout.
TOOL_TIMEOUT_MS = 60_000


def _tool(name: str, description: str, **parameters: str) -> dict:
    properties = {key: {"type": "string", "description": text} for key, text in parameters.items()}
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {"type": "object", "properties": properties, "required": [*parameters]},
        },
    }


#: The tools as OpenAI function schemas, for a chat template's ``tools=``.
TOOLS = [
    _tool(
        "shell",
        "Runs a shell script in the task's environment and shows its exit code and output.",
        command="The script, run by /bin/sh -c.",
    ),
    _tool("read_file", "Reads a file in the task's environment.", path="The file's absolute path."),
    _tool(
        "write_file",
        "Writes a file in the task's environment, replacing any file at that path.",
        path="The file's absolute path.",
        content="The file's new content.",
    ),
]

_CALLS = {
    "shell": lambda args: LoopToolShellV1(script=args["command"]),
    "read_file": lambda args: LoopToolReadFileV1(path=args["path"]),
    "write_file": lambda args: LoopToolWriteFileV1(
        path=args["path"], data=args["content"].encode()
    ),
}


def to_call(name: str, arguments: Mapping[str, str]) -> LoopToolCallV1:
    """A call of one of :data:`TOOLS`; any other name raises ``ValueError``."""
    if name not in _CALLS:
        raise ValueError(f"unknown tool {name!r}: the tools are {', '.join(_CALLS)}")
    return LoopToolCallV1(timeout_millis=TOOL_TIMEOUT_MS, **{name: _CALLS[name](arguments)})


def render(result: LoopToolResultV1) -> str:
    """A call's result as the text the model reads next."""
    lines = [
        {
            "exit_code": f"exit code {result.exit_code}",
            "signal": f"killed by signal {result.signal}",
            "done": "done",
            "error": f"error: {result.error}",
        }.get(result.WhichOneof("outcome"), "no outcome")
    ]
    if result.timed_out:
        lines.append("timed out")
    for name in ("stdout", "stderr", "file"):
        if data := getattr(result, name):
            lines.append(f"{name}:\n{data.decode(errors='replace')}")
    if result.truncated:
        lines.append("(truncated: the output stops short)")
    return "\n".join(lines)


def sft_messages(messages: list[dict]) -> list[dict]:
    """A trajectory export row's messages as a chat template takes them: each call's
    ``arguments``, JSON text in the file, parsed (text that is not JSON stays text), and a
    field a Parquet row holds as null left out, as the JSONL rows leave it."""
    parsed = []
    for message in messages:
        message = {key: value for key, value in message.items() if value is not None}
        if "tool_calls" in message:
            message["tool_calls"] = [_parsed_call(call) for call in message["tool_calls"]]
        parsed.append(message)
    return parsed


def _parsed_call(call: dict) -> dict:
    function = dict(call["function"])
    with contextlib.suppress(TypeError, ValueError):
        function["arguments"] = json.loads(function["arguments"])
    return {**call, "function": function}


class LoopInfrastructureFailure(Exception):
    """Loop failed a rollout on its own side twice in a row; an adapter never scores it."""


_NO_REWARD = (
    LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_INFRASTRUCTURE,
    LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_CANCELLED,
)


def reward(rollout: LoopRolloutV1, name: str | None = None) -> float | None:
    """A closed rollout's reward: the one named, or the primary. Rewards are in
    the environment's declared order, primary first (rollout.proto). A task's
    or verifier's failure keeps its value; ours (``INFRASTRUCTURE``) or a
    person's Stop answers ``None``, never a score. A reward the rollout lacks
    raises ``LookupError`` naming it."""
    if rollout.failure.failure_class in _NO_REWARD:
        return None
    rewards = [each for each in rollout.rewards if name is None or each.name == name]
    if not rewards:
        raise LookupError(f"rollout {rollout.rollout_id} closed without reward {name or 'any'}")
    return rewards[0].value
