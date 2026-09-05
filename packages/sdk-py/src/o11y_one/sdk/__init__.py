"""``o11y_one.sdk`` — hand-written client layer over the generated ``o11y_one.*``
protobuf packages shipped by the ``o11y-one-api`` distribution.

Three things live here and nothing else:

* transport construction (:mod:`o11y_one.sdk.client`)
* credential injection and its local validation (:mod:`o11y_one.sdk.auth`)
* the failure taxonomy an SDK exists to render (:mod:`o11y_one.sdk.errors`)

Service methods are NOT wrapped or re-exported. Import the generated
``*ServiceClient`` you need from ``o11y_one.<domain>.v1.<file>_connect`` and hand
the class to :meth:`O11yClient.service` / :meth:`O11yClient.service_sync`.

Note that ``o11y_one`` itself is a PEP 420 namespace package contributed to by
two distributions: ``o11y-one-api`` (generated) and ``o11y-one`` (this one).
There is deliberately no ``o11y_one/__init__.py`` in either.
"""

from __future__ import annotations

from .auth import (
    CREDENTIAL_HEADER,
    CREDENTIAL_MAX_LEN,
    MACHINE_CREDENTIAL_PREFIX,
    ORG_ID_HEADER,
    TENANT_ID_HEADER,
    assert_looks_like_machine_credential,
)
from .client import CredentialInterceptor, O11yClient
from .errors import MACHINE_SCOPES, ClassifiedFailure, Disposition, classify

__all__ = [
    "CREDENTIAL_HEADER",
    "CREDENTIAL_MAX_LEN",
    "MACHINE_CREDENTIAL_PREFIX",
    "MACHINE_SCOPES",
    "ORG_ID_HEADER",
    "TENANT_ID_HEADER",
    "ClassifiedFailure",
    "CredentialInterceptor",
    "Disposition",
    "O11yClient",
    "assert_looks_like_machine_credential",
    "classify",
]

__version__ = "0.0.0"
