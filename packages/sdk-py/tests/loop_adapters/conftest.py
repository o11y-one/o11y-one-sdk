"""The trainer adapters' fixtures; the fake Loop itself is fake_loop.py."""

from __future__ import annotations

import threading
from wsgiref.simple_server import make_server

import pytest
from fake_loop import CREDENTIAL, RUN, FakeLoop, _Quiet, _Server, _unchunked
from o11y_one.agentic.v1.rollout_connect import LoopRolloutServiceWSGIApplication


@pytest.fixture
def loop(monkeypatch: pytest.MonkeyPatch):
    fake = FakeLoop()
    app = _unchunked(LoopRolloutServiceWSGIApplication(fake))
    server = make_server("127.0.0.1", 0, app, server_class=_Server, handler_class=_Quiet)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    fake.url = f"http://127.0.0.1:{server.server_port}"
    monkeypatch.setenv("O11Y_RUN", RUN)
    monkeypatch.setenv("O11Y_API_KEY", CREDENTIAL)
    monkeypatch.setenv("O11Y_BASE_URL", fake.url)  # an adapter test never reaches a real Loop
    yield fake
    for event in fake.held.values():
        event.set()
    server.shutdown()
    server.server_close()
