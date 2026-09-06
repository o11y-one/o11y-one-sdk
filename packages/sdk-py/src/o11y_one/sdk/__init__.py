"""``o11y_one.sdk`` — hand-written client layer over the generated ``o11y_one.*``
protobuf packages shipped by the ``o11y-one-api`` distribution.

Four things live here:

* transport construction (:mod:`o11y_one.sdk.client`)
* credential injection and its local validation (:mod:`o11y_one.sdk.auth`)
* the failure taxonomy an SDK exists to render (:mod:`o11y_one.sdk.errors`)
* an ergonomic facade over exactly ONE generated service,
  ``AgenticEvaluationService`` (:mod:`o11y_one.sdk.agentic`)

For every other generated service, methods are still NOT wrapped or
re-exported: import the generated ``*ServiceClient`` you need from
``o11y_one.<domain>.v1.<file>_connect`` and hand the class to
:meth:`O11yClient.service` / :meth:`O11yClient.service_sync`. The rationale for
staying thin there is unchanged — a hand-written facade over every one of the
29 generated services would be a second API surface to keep in sync with the
proto, and it would rot the first time a field is added upstream.

``AgenticEvaluationService`` is the deliberate exception, not a reversal of
that rule: it is the run-submission / lease-heartbeat-submit-release /
dataset-draft / annotation surface an eval-authoring or externally-executed
runtime integration calls minute to minute, its messages repeat the same
refusal-on-a-200, idempotency and capability-envelope conventions across
dozens of RPCs, and getting any one of those conventions wrong locally
degrades silently to an opaque network error rather than a loud local one. See
:mod:`o11y_one.sdk.agentic` for what the facade adds on top of the generated
client, and ``l2-notes.md`` for why this scope was drawn where it was.

Note that ``o11y_one`` itself is a PEP 420 namespace package contributed to by
two distributions: ``o11y-one-api`` (generated) and ``o11y-one`` (this one).
There is deliberately no ``o11y_one/__init__.py`` in either.
"""

from __future__ import annotations

from .agentic import (
    MACHINE_SCOPE_NAME_TO_ENUM,
    AgenticClient,
    AgenticClientSync,
    CaseOutput,
    IssuedMachineCredential,
)
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
from .recovery import bare_enum_name, find_error_detail
from .results import Refusal
from .validation import ValidationError

__all__ = [
    "CREDENTIAL_HEADER",
    "CREDENTIAL_MAX_LEN",
    "MACHINE_CREDENTIAL_PREFIX",
    "MACHINE_SCOPES",
    "MACHINE_SCOPE_NAME_TO_ENUM",
    "ORG_ID_HEADER",
    "TENANT_ID_HEADER",
    "AgenticClient",
    "AgenticClientSync",
    "CaseOutput",
    "ClassifiedFailure",
    "CredentialInterceptor",
    "Disposition",
    "IssuedMachineCredential",
    "O11yClient",
    "Refusal",
    "ValidationError",
    "assert_looks_like_machine_credential",
    "bare_enum_name",
    "classify",
    "find_error_detail",
]

__version__ = "0.0.0"
