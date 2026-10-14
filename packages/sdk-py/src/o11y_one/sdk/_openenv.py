"""LoopEnvClient, behind the ``openenv`` extra; import it from :mod:`o11y_one.sdk.loop`."""

from __future__ import annotations

import asyncio
import os
from typing import Any
from urllib.parse import urlencode

from openenv.core.env_client import ws_connect
from openenv.core.generic_client import GenericEnvClient
from websockets.protocol import State

from .auth import CREDENTIAL_HEADER, assert_looks_like_machine_credential
from .client import require_secure_url


class LoopEnvClient(GenericEnvClient):
    """OpenEnv's own ``GenericEnvClient`` for a Loop run, sending the machine
    key as ``x-o11y-key`` on its WebSocket upgrade. A stock OpenEnv client
    sends none, so Loop refuses it.

    ``base_url`` is Loop's OpenEnv root, e.g.
    ``https://api.o11y.one/loop/v1/openenv``. ``run`` and ``credential``
    default to ``O11Y_RUN`` and ``O11Y_API_KEY``; the run rides in the URL, the
    key never does.
    """

    def __init__(
        self,
        base_url: str,
        *,
        run: str | None = None,
        credential: str | None = None,
        **kwargs: Any,
    ) -> None:
        run = run or os.environ.get("O11Y_RUN")
        if not run:
            raise ValueError("no run: pass run= or set O11Y_RUN")
        self._run = run
        credential = credential or os.environ.get("O11Y_API_KEY", "")
        self._key = {CREDENTIAL_HEADER: assert_looks_like_machine_credential(credential)}
        super().__init__(base_url=base_url, **kwargs)

    def _set_base_url(self, base_url: str) -> None:
        super()._set_base_url(base_url)
        require_secure_url(self._ws_url, "wss", "ws")
        self._ws_url = f"{self._ws_url}?{urlencode({'run': self._run})}"

    async def _connect_async(self) -> LoopEnvClient:
        # EnvClient._connect_async at v0.8.0, for a client given its base_url,
        # with the key added to ws_connect.
        loop = asyncio.get_running_loop()
        open_here = self._ws is not None and self._ws_loop is loop
        if open_here and self._ws.state not in (State.CLOSING, State.CLOSED):
            return self
        self._ws, self._ws_loop = None, None
        await self._drain_pending_close_tasks()
        try:
            self._ws = await ws_connect(
                self._ws_url,
                additional_headers=self._key,
                open_timeout=self._connect_timeout,
                max_size=self._max_message_size,
                ping_interval=self._websocket_ping_interval_s,
                ping_timeout=self._websocket_ping_timeout_s,
            )
        except Exception as error:
            await self.close()
            raise ConnectionError(f"Failed to connect to {self._ws_url}: {error}") from error
        self._ws_loop = loop
        return self
