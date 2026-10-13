"""The TRL adapter against a fake Loop: lazy resets, one concurrent close per batch,
content-derived groups, refusals that stop training, and tools TRL can read.

Needs the ``trl`` extra; skipped without it.
"""

from __future__ import annotations

import functools
import inspect
import logging
import threading
import time
from types import SimpleNamespace

import pytest

pytest.importorskip("trl")

from conftest import CREDENTIAL, refusal  # noqa: E402
from o11y_one.agentic.v1.rollout_pb2 import LoopFailureClassV1  # noqa: E402
from o11y_one.sdk.loop import RolloutRefused, _core  # noqa: E402
from o11y_one.sdk.loop import trl as adapter  # noqa: E402
from transformers.utils import get_json_schema  # noqa: E402

GROUP_SIZE = 4


def start(step: int = 3) -> None:
    """What GRPOTrainer tells LoopCallback at train begin and at each step."""
    args = SimpleNamespace(
        generation_batch_size=8, num_generations=GROUP_SIZE, run_name="pyfix-trl"
    )
    callback = adapter.LoopCallback()
    callback.on_train_begin(args, SimpleNamespace(max_steps=30), None)
    callback.on_step_begin(args, SimpleNamespace(global_step=step), None)


def environments(loop, count: int) -> list[adapter.LoopEnvironment]:
    return [adapter.LoopEnvironment(base_url=loop.url) for _ in range(count)]


def row(case: str) -> dict:
    return {"prompt": [{"role": "user", "content": f"fix {case}"}], "loop_case_revision_id": case}


def started(envs: list[adapter.LoopEnvironment]) -> list[str]:
    """Each environment's rollout id, once its reset answered."""
    for env in envs:
        env._started.result(10)
    return [env._client.rollout_id for env in envs]


def test_reset_answers_at_once_and_the_batch_resets_concurrently(loop) -> None:
    start()
    envs = environments(loop, 8)
    held = loop.hold("reset")
    for env in envs:
        began = time.monotonic()
        assert env.reset(**row("case-a")) is None
        assert time.monotonic() - began < 0.05
    loop.wait_in_flight("reset", 8)
    held.set()
    assert len(set(started(envs))) == 8


def test_loop_reward_closes_the_batch_concurrently_and_answers_in_order(loop) -> None:
    start()
    envs = environments(loop, 8)
    for env in envs:
        env.reset(**row("case-a"))
    rollouts = started(envs)
    held = loop.hold("close")
    answered: list = []
    scoring = threading.Thread(target=lambda: answered.append(adapter.loop_reward(envs)))
    scoring.start()
    loop.wait_in_flight("close", 8)
    held.set()
    scoring.join(10)
    assert answered == [[int(rollout.removeprefix("r-")) / 10 for rollout in rollouts]]
    assert sorted(request.rollout_id for request in loop.sent("close")) == sorted(rollouts)


def test_a_rollout_failure_is_kept_or_dropped_by_whose_it_is(loop) -> None:
    start()
    envs = environments(loop, 2)
    for env in envs:
        env.reset(**row("case-a"))
    ours, task = started(envs)
    loop.closes[ours] = (LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_INFRASTRUCTURE, [])
    loop.closes[task] = (LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_TASK, [("tests_passed", -1.0)])
    assert adapter.loop_reward(envs) == [None, -1.0]


def test_the_tools_are_the_core_three_as_trl_reads_them_and_no_reward_of_their_own() -> None:
    public = {
        name
        for name, _ in inspect.getmembers(adapter.LoopEnvironment, predicate=inspect.isfunction)
        if not name.startswith("_")
    }
    assert public == {"reset", "shell", "read_file", "write_file"}
    schemas = []
    for tool in _core.TOOLS:
        schema = get_json_schema(getattr(adapter.LoopEnvironment, tool["function"]["name"]))
        schema["function"].pop("return")
        schemas.append(schema)
    assert schemas == _core.TOOLS


def test_a_tool_steps_its_rollout_with_one_call_and_answers_its_result(loop) -> None:
    start()
    (env,) = environments(loop, 1)
    env.reset(**row("case-a"))
    assert env.shell("pytest -q") == "exit code 0\nstdout:\nran shell"
    ((request),) = loop.sent("step")
    (call,) = request.calls
    assert (request.rollout_id, call.shell.script) == (env._client.rollout_id, "pytest -q")


def test_a_group_is_its_step_and_case_in_every_process(loop) -> None:
    start(step=3)
    batch = environments(loop, 8)
    for env, case in zip(batch, ["case-a"] * 4 + ["case-b"] * 4, strict=True):
        env.reset(**row(case))
    started(batch)
    start(step=3)  # another process, at the same step
    (other,) = environments(loop, 1)
    other.reset(**row("case-a"))
    start(step=4)
    (later,) = environments(loop, 1)
    later.reset(**row("case-a"))
    started([other, later])
    sent = loop.sent("reset")
    first, (other_request,), (later_request,) = sent[:8], sent[8:9], sent[9:]
    if other_request.trainer_step == 4:
        other_request, later_request = later_request, other_request
    groups = {
        case: {(r.group_id, r.group_index) for r in first if r.case_revision_id == case}
        for case in ("case-a", "case-b")
    }
    (group_a,), (group_b,) = ({group for group, _ in pairs} for pairs in groups.values())
    assert group_a != group_b
    assert (
        {index for _, index in groups["case-a"]}
        == {index for _, index in groups["case-b"]}
        == {0, 1, 2, 3}
    )
    assert other_request.group_id == group_a != later_request.group_id
    assert {(request.group_size, request.trainer_step) for request in first} == {(GROUP_SIZE, 3)}
    assert {(request.trainer_total_steps, request.experiment_name) for request in first} == {
        (30, "pyfix-trl")
    }
    client = first[0].client
    assert (client.adapter, client.framework_version) == (
        "o11y_one.sdk.loop.trl",
        adapter.trl.__version__,
    )


def test_a_case_repeated_in_one_step_keeps_its_indices_inside_the_group(loop) -> None:
    start()
    envs = environments(loop, 8)
    for env in envs:
        env.reset(**row("case-a"))
    started(envs)
    indices = sorted(request.group_index for request in loop.sent("reset"))
    assert indices == [0, 0, 1, 1, 2, 2, 3, 3]


def test_a_refused_reset_reaches_the_model_and_then_stops_training_with_its_code(loop) -> None:
    start()
    loop.refusals["reset"] = [refusal("run_concurrency_reached")]
    (env,) = environments(loop, 1)
    env.reset(**row("case-a"))
    with pytest.raises(RolloutRefused) as told:
        env.shell("ls")
    assert told.value.code == "run_concurrency_reached"
    with pytest.raises(RolloutRefused) as stopped:
        adapter.loop_reward([env])
    assert stopped.value.code == "run_concurrency_reached"


def test_reset_without_the_callback_says_to_add_it(loop, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(adapter._trainer, "group_size", 0)
    (env,) = environments(loop, 1)
    with pytest.raises(RuntimeError, match="LoopCallback"):
        env.reset(**row("case-a"))


def test_the_key_reaches_loop_and_never_a_log_or_repr(
    loop, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.DEBUG)
    start()
    factory = functools.partial(adapter.LoopEnvironment, base_url=loop.url)
    env = factory()
    env.reset(**row("case-a"))
    env.shell("ls")
    adapter.loop_reward([env])
    assert loop.keys == {CREDENTIAL}
    shown = [repr(env), str(env), repr(env._client), caplog.text]
    assert not [text for text in shown if CREDENTIAL in text or "BBBBBBBB" in text]
