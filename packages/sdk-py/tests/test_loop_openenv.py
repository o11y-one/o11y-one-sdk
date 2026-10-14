"""LoopEnvClient: OpenEnv v0.8.0's own client, with the machine key on its upgrade.

Needs the ``openenv`` extra (``uv sync --all-packages --all-extras``); skipped
without it. The conformance test runs OpenEnv's client code path against a live
Loop server, and is skipped unless ``O11Y_OPENENV_URL`` names one (with
``O11Y_API_KEY`` and ``O11Y_RUN``), as ``o11y-eval`` reads ``O11Y_BASE_URL``.
"""

from __future__ import annotations

import json
import os
import threading

import pytest

pytest.importorskip("openenv")

from o11y_one.sdk.loop import LoopEnvClient  # noqa: E402
from openenv.core.generic_client import GenericEnvClient  # noqa: E402
from websockets.sync.server import serve  # noqa: E402

CREDENTIAL = "o11y_mach.AAAAAAAAAAAAAAAAAAAAAA.BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBA"
RUN = "trn_06AZ3XN1YQF4KD2M8RP7TV5W9C"
LIVE = os.environ.get("O11Y_OPENENV_URL")


def test_the_upgrade_carries_the_key_and_the_run_and_an_episode_runs_over_it() -> None:
    seen: dict[str, object] = {"messages": []}
    observation = {"metadata": {}, "rollout_id": "r-1", "snapshot_id": "ab"}

    def handler(ws) -> None:
        seen["path"] = ws.request.path
        seen["key"] = ws.request.headers.get("x-o11y-key")
        for raw in ws:
            message = json.loads(raw)
            seen["messages"].append(message)
            if message["type"] == "reset":
                data = {"observation": observation, "reward": None, "done": False}
                ws.send(json.dumps({"type": "observation", "data": data}))

    with serve(handler, "127.0.0.1", 0) as server:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        port = server.socket.getsockname()[1]
        url = f"http://127.0.0.1:{port}/loop/v1/openenv"
        client = LoopEnvClient(url, run=RUN, credential=CREDENTIAL)
        shown = [repr(client), str(client)]
        with client.sync() as env:
            result = env.reset(group_size=4)
        server.shutdown()

    assert (seen["path"], seen["key"]) == (f"/loop/v1/openenv/ws?run={RUN}", CREDENTIAL)
    assert seen["messages"][0] == {"type": "reset", "data": {"group_size": 4}}
    assert (result.observation, result.reward, result.done) == (observation, None, False)
    assert not [text for text in shown if CREDENTIAL in text]


def test_a_plain_websocket_off_this_machine_is_refused() -> None:
    with pytest.raises(ValueError, match="'ws'") as refused:
        LoopEnvClient("http://openenv.example/loop/v1/openenv", run=RUN, credential=CREDENTIAL)
    assert CREDENTIAL not in str(refused.value)
    LoopEnvClient("https://openenv.example/loop/v1/openenv", run=RUN, credential=CREDENTIAL)


def test_run_and_credential_fall_back_to_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("O11Y_RUN", raising=False)
    monkeypatch.delenv("O11Y_API_KEY", raising=False)
    with pytest.raises(ValueError, match="O11Y_RUN"):
        LoopEnvClient("http://127.0.0.1:1", credential=CREDENTIAL)
    with pytest.raises(ValueError, match="empty"):
        LoopEnvClient("http://127.0.0.1:1", run=RUN)
    monkeypatch.setenv("O11Y_RUN", RUN)
    monkeypatch.setenv("O11Y_API_KEY", CREDENTIAL)
    LoopEnvClient("http://127.0.0.1:1")


@pytest.mark.skipif(not LIVE, reason="O11Y_OPENENV_URL names no Loop server")
def test_openenv_conformance_against_a_live_loop_server() -> None:
    with LoopEnvClient(LIVE).sync() as env:
        reset = env.reset()
        rollout_id = reset.observation["rollout_id"]
        assert (reset.reward, reset.done) == (None, False)
        called = env.step(
            {"type": "call_tool", "tool_name": "exec", "arguments": {"argv": ["true"]}}
        )
        assert (called.observation["tool_name"], called.observation["error"]) == ("exec", None)
        assert (called.reward, called.done) == (None, False)
        assert env.state() == {"episode_id": rollout_id, "step_count": 1}
        submitted = env.step({"submit": {}})
        assert submitted.done
        assert set(submitted.metadata) == {"rewards", "verdict", "error"}

    # OpenEnv's stock client sends no key, so Loop refuses its upgrade before any session.
    with pytest.raises(ConnectionError), GenericEnvClient(base_url=LIVE).sync() as stock:
        stock.reset()
