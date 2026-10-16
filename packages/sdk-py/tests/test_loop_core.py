"""What every trainer adapter shares: the tools, their calls and results, and the reward rule."""

from __future__ import annotations

import pytest
from o11y_one.agentic.v1.rollout_pb2 import (
    LoopFailureClassV1,
    LoopRewardV1,
    LoopRolloutFailureV1,
    LoopRolloutV1,
    LoopToolResultV1,
)
from o11y_one.sdk.loop import _core


def rollout(failure_class: int = 0, *rewards: tuple[str, float]) -> LoopRolloutV1:
    failure = LoopRolloutFailureV1(failure_class=failure_class, code="x") if failure_class else None
    return LoopRolloutV1(
        rollout_id="r-1",
        failure=failure,
        rewards=[LoopRewardV1(name=name, value=value) for name, value in rewards],
    )


@pytest.mark.parametrize(
    "failure_class",
    [
        LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_TASK,
        LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_VERIFIER,
    ],
)
def test_a_task_or_verifier_failure_keeps_its_reward(failure_class: int) -> None:
    assert _core.reward(rollout(failure_class, ("tests_passed", -1.0))) == -1.0


@pytest.mark.parametrize(
    "failure_class",
    [
        LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_INFRASTRUCTURE,
        LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_CANCELLED,
    ],
)
def test_our_failure_or_a_cancellation_has_no_reward(failure_class: int) -> None:
    assert _core.reward(rollout(failure_class)) is None


def test_the_primary_reward_is_the_first_unless_one_is_named() -> None:
    rewarded = rollout(0, ("tests_passed", 0.5), ("all_passed", 0.0))
    assert _core.reward(rewarded) == 0.5
    assert _core.reward(rewarded, "all_passed") == 0.0
    with pytest.raises(LookupError, match="rollout r-1 closed without reward style"):
        _core.reward(rewarded, "style")


def test_a_rewarded_rollout_without_rewards_raises_naming_it() -> None:
    with pytest.raises(LookupError, match="rollout r-1 closed without reward any"):
        _core.reward(rollout())


def test_shell_runs_its_command_as_a_script_within_the_tool_timeout() -> None:
    call = _core.to_call("shell", {"command": "pytest -q | tail -1"})
    assert call.WhichOneof("call") == "shell"
    assert (call.shell.script, call.timeout_millis) == (
        "pytest -q | tail -1",
        _core.TOOL_TIMEOUT_MS,
    )


def test_read_and_write_file_map_to_their_own_calls() -> None:
    read = _core.to_call("read_file", {"path": "/work/fix.py"})
    assert (read.WhichOneof("call"), read.read_file.path) == ("read_file", "/work/fix.py")
    written = _core.to_call("write_file", {"path": "/work/fix.py", "content": "x = 1\n"})
    assert (written.WhichOneof("call"), written.write_file.path) == ("write_file", "/work/fix.py")
    assert (written.write_file.data, written.write_file.append) == (b"x = 1\n", False)
    assert read.timeout_millis == written.timeout_millis == _core.TOOL_TIMEOUT_MS
    with pytest.raises(ValueError, match="exec"):
        _core.to_call("exec", {"argv": ["true"]})


def test_every_declared_tool_maps_to_a_call_from_its_required_arguments() -> None:
    for tool in _core.TOOLS:
        function = tool["function"]
        arguments = {name: "x" for name in function["parameters"]["required"]}
        assert _core.to_call(function["name"], arguments).WhichOneof("call") == function["name"]
    assert [tool["function"]["name"] for tool in _core.TOOLS] == [
        "shell",
        "read_file",
        "write_file",
    ]


def test_render_shows_the_exit_code_both_streams_and_a_cut() -> None:
    result = LoopToolResultV1(exit_code=1, stdout=b"1 failed\n", stderr=b"boom", truncated=True)
    assert _core.render(result) == (
        "exit code 1\nstdout:\n1 failed\n\nstderr:\nboom\n(truncated: the output stops short)"
    )


def test_render_shows_a_signal_a_timeout_an_error_and_a_file() -> None:
    assert (
        _core.render(LoopToolResultV1(signal=9, timed_out=True)) == "killed by signal 9\ntimed out"
    )
    assert _core.render(LoopToolResultV1(error="tool_call_invalid")) == "error: tool_call_invalid"
    assert _core.render(LoopToolResultV1(done=True, file=b"x = 1\n")) == "done\nfile:\nx = 1\n"


def test_render_never_raises_on_bytes_that_are_not_utf8() -> None:
    assert _core.render(LoopToolResultV1(exit_code=0, stdout=b"\xff\xfe ok")) == (
        "exit code 0\nstdout:\n�� ok"
    )


def test_a_trajectory_rows_calls_get_their_arguments_parsed_and_its_nulls_dropped() -> None:
    # As a trajectory export writes a row: every call's arguments JSON text, and in a Parquet
    # column every message field present, null where the message lacks it.
    call = {"id": "000000001", "type": "function", "function": {"name": "shell"}}
    written = [
        {"role": "user", "content": "Fix it.", "tool_calls": None, "tool_call_id": None},
        {
            "role": "assistant",
            "content": "",
            "tool_calls": [
                {**call, "function": {"name": "shell", "arguments": '{"command": "pytest -q"}'}},
                {**call, "function": {"name": "shell", "arguments": "not json"}},
            ],
        },
        {"role": "tool", "content": "exit code 0", "tool_call_id": "000000001", "name": "shell"},
    ]
    messages = _core.sft_messages(written)
    assert messages[0] == {"role": "user", "content": "Fix it."}
    arguments = [each["function"]["arguments"] for each in messages[1]["tool_calls"]]
    assert arguments == [{"command": "pytest -q"}, "not json"]  # text that is not JSON stays
    assert messages[2] == written[2]
    assert written[1]["tool_calls"][0]["function"]["arguments"] == '{"command": "pytest -q"}'
