"""No test reaches a real endpoint or holds a real credential: every endpoint default is a
closed local port, and the credential env is gone. A fixture that serves a fake sets its own."""

from __future__ import annotations

import pytest
from o11y_one.sdk import loop

CLOSED = "http://127.0.0.1:9"
CREDENTIAL_ENV = ("O11Y_API_KEY", "O11Y_RUN", "TINKER_API_KEY")


@pytest.fixture(autouse=True)
def no_real_endpoint(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("O11Y_BASE_URL", CLOSED)
    monkeypatch.setattr(loop, "DEFAULT_BASE_URL", CLOSED)
    for name in CREDENTIAL_ENV:
        monkeypatch.delenv(name, raising=False)
