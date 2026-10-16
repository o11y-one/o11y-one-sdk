"""Small files in the shapes Loop's dataset exports write, one per trainer and export kind, for
the adapters' smoke legs to load with each trainer's own loader.

A task set holds a row per task: its prompt and the case its rollout resets on. A trajectory
set holds a row per rollout: the prompt, then each assistant turn and a tool turn per call,
the tool turn's content as ``_core.render`` gave it to the model; each call's ``arguments``
are JSON text. A rollout's row ends on its last tool turn.

Parquet columns are typed as the export types them: every message field in every message,
null where the message lacks it, and lists and strings in their large forms, except TRL's,
which are written as ``datasets`` writes them, with the arguments and the tools under the
``arrow.json`` extension type and the file's ``huggingface`` features naming them ``Json()``.
JSONL rows leave out a field a message lacks.
"""

from __future__ import annotations

import json
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
from o11y_one.sdk.loop import _core

CASES = ["0b9f6c84-6d3e-4c0e-9a51-7f0d5b0c1a01", "0b9f6c84-6d3e-4c0e-9a51-7f0d5b0c1a02"]
PROMPTS = [[{"role": "user", "content": f"Fix the module, case {n}."}] for n in (1, 2)]


def _call(index: int, name: str, **arguments: str) -> dict:
    function = {"name": name, "arguments": json.dumps(arguments)}
    return {"id": f"{index:09}", "type": "function", "function": function}


def _answer(call: dict, content: str) -> dict:
    name = call["function"]["name"]
    return {"role": "tool", "content": content, "tool_call_id": call["id"], "name": name}


def _conversations() -> list[list[dict]]:
    """Two rollouts: one call, then a message's two parallel calls, whose tools take different
    arguments."""
    shell = _call(1, "shell", command="pytest -q")
    read = _call(1, "read_file", path="/work/mod.py")
    write = _call(
        2, "write_file", path="/work/mod.py", content="def add(a, b):\n    return a + b\n"
    )
    return [
        [
            *PROMPTS[0],
            {"role": "assistant", "content": "Running the tests.", "tool_calls": [shell]},
            _answer(shell, "exit code 1\nstdout:\n1 failed"),
        ],
        [
            *PROMPTS[1],
            {"role": "assistant", "content": "", "tool_calls": [read, write]},
            _answer(read, "done\nfile:\ndef add(a, b):\n    return a - b\n"),
            _answer(write, "done"),
        ],
    ]


def _string(large: bool) -> pa.DataType:
    return pa.large_string() if large else pa.string()


def _list(item: pa.DataType, large: bool) -> pa.DataType:
    field = pa.field("element", item, nullable=False)
    return pa.large_list(field) if large else pa.list_(field)


def _message_type(*, large: bool, name: bool, json_arguments: bool = False) -> pa.DataType:
    text = _string(large)
    arguments = pa.field(
        "arguments", text, nullable=False, metadata=_JSON if json_arguments else None
    )
    function = pa.struct([pa.field("name", text, nullable=False), arguments])
    call = pa.struct(
        [
            pa.field("id", text, nullable=False),
            pa.field("type", text, nullable=False),
            pa.field("function", function, nullable=False),
        ]
    )
    fields = [
        pa.field("role", text, nullable=False),
        pa.field("content", text, nullable=False),
        pa.field("tool_calls", _list(call, large)),
        pa.field("tool_call_id", text),
    ]
    return pa.struct(fields + ([pa.field("name", text)] if name else []))


_JSON = {"ARROW:extension:name": "arrow.json", "ARROW:extension:metadata": ""}


def _columns(messages: list[dict], keys: tuple[str, ...]) -> list[dict]:
    return [{key: message.get(key) for key in keys} for message in messages]


def _write(path: Path, rows: list[dict], fields: list[pa.Field], metadata=None) -> Path:
    schema = pa.schema(fields, metadata=metadata)
    pq.write_table(pa.Table.from_pylist(rows, schema=schema), path, compression="zstd")
    return path


def _jsonl(path: Path, rows: list[dict]) -> Path:
    path.write_text("".join(json.dumps(row) + "\n" for row in rows))
    return path


def _prompt_column(prompt: list[dict]) -> list[dict]:
    return _columns(prompt, ("role", "content", "tool_calls", "tool_call_id"))


def task_set(trainer: str, path: Path) -> Path:
    """The task-set export for ``trainer``: verl and TRL Parquet, OpenRLHF and Tinker JSONL."""
    prompt = pa.field("prompt", _list(_message_type(large=True, name=False), True), nullable=False)
    text = pa.large_string()
    if trainer == "verl":
        case = pa.struct([pa.field("case_revision_id", text, nullable=False)])
        fields = [
            prompt,
            pa.field("agent_name", text, nullable=False),
            pa.field("data_source", text, nullable=False),
            pa.field("extra_info", pa.struct([pa.field("loop", case, nullable=False)]), False),
        ]
        rows = [
            {
                "prompt": _prompt_column(messages),
                "agent_name": "loop",
                "data_source": "loop",
                "extra_info": {"loop": {"case_revision_id": case_id}},
            }
            for messages, case_id in zip(PROMPTS, CASES, strict=True)
        ]
        return _write(path, rows, fields)
    if trainer == "trl":
        fields = [prompt, pa.field("loop_case_revision_id", text, nullable=False)]
        rows = [
            {"prompt": _prompt_column(messages), "loop_case_revision_id": case_id}
            for messages, case_id in zip(PROMPTS, CASES, strict=True)
        ]
        return _write(path, rows, fields)
    if trainer == "openrlhf":
        rows = [
            {
                "prompt": messages,
                "label": json.dumps({"case_revision_id": case_id}, separators=(",", ":")),
            }
            for messages, case_id in zip(PROMPTS, CASES, strict=True)
        ]
        return _jsonl(path, rows)
    rows = [
        {"messages": messages, "loop": {"case_revision_id": case_id}}
        for messages, case_id in zip(PROMPTS, CASES, strict=True)
    ]
    return _jsonl(path, rows)


_KEYS = ("role", "content", "tool_calls", "tool_call_id", "name")


def trajectory_set(trainer: str, path: Path) -> Path:
    """The trajectory-set export for ``trainer``: verl and TRL Parquet, OpenRLHF and Tinker
    JSONL. Only verl and TRL carry the tools the rollouts reset with."""
    conversations, tools = _conversations(), json.dumps(_core.TOOLS)
    rewards = [json.dumps({"tests_passed": value}) for value in (0.0, 1.0)]
    if trainer in ("verl", "trl"):
        large = trainer == "verl"
        text = _string(large)
        message = _message_type(large=large, name=True, json_arguments=not large)
        fields = [
            pa.field("messages", _list(message, large), nullable=False),
            pa.field("tools", text, metadata=None if large else _JSON),
            pa.field("loop_rollout_id", text, nullable=False),
        ]
        rows = [
            {
                "messages": _columns(messages, _KEYS),
                "tools": tools,
                "loop_rollout_id": f"rollout-{n}",
                "loop_rewards": reward,
                **({"loop_group_id": "group-1"} if large else {}),
            }
            for n, (messages, reward) in enumerate(zip(conversations, rewards, strict=True))
        ]
        if large:
            fields.append(pa.field("loop_group_id", text, nullable=False))
        fields.append(pa.field("loop_rewards", text, nullable=False))
        metadata = None if large else {"huggingface": TRL_FEATURES}
        return _write(path, rows, fields, metadata)
    return _jsonl(path, [{"messages": messages} for messages in conversations])


#: The ``huggingface`` features the TRL trajectory export names in its file, as ``datasets`` 5.1
#: writes them for its columns.
TRL_FEATURES = json.dumps(
    {
        "info": {
            "features": {
                "messages": {
                    "feature": {
                        "role": {"dtype": "string", "_type": "Value"},
                        "content": {"dtype": "string", "_type": "Value"},
                        "tool_calls": {
                            "feature": {
                                "id": {"dtype": "string", "_type": "Value"},
                                "type": {"dtype": "string", "_type": "Value"},
                                "function": {
                                    "name": {"dtype": "string", "_type": "Value"},
                                    "arguments": {"_type": "Json"},
                                },
                            },
                            "_type": "List",
                        },
                        "tool_call_id": {"dtype": "string", "_type": "Value"},
                        "name": {"dtype": "string", "_type": "Value"},
                    },
                    "_type": "List",
                },
                "tools": {"_type": "Json"},
                "loop_rollout_id": {"dtype": "string", "_type": "Value"},
                "loop_rewards": {"dtype": "string", "_type": "Value"},
            }
        }
    }
)
