import datetime

from o11y_one.common.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoopEnvironmentProfileV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_ENVIRONMENT_PROFILE_V1_UNSPECIFIED: _ClassVar[LoopEnvironmentProfileV1]
    LOOP_ENVIRONMENT_PROFILE_V1_SMALL: _ClassVar[LoopEnvironmentProfileV1]
    LOOP_ENVIRONMENT_PROFILE_V1_MEDIUM: _ClassVar[LoopEnvironmentProfileV1]
    LOOP_ENVIRONMENT_PROFILE_V1_LARGE: _ClassVar[LoopEnvironmentProfileV1]

class LoopEnvironmentNetworkModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_ENVIRONMENT_NETWORK_MODE_V1_UNSPECIFIED: _ClassVar[LoopEnvironmentNetworkModeV1]
    LOOP_ENVIRONMENT_NETWORK_MODE_V1_OFFLINE: _ClassVar[LoopEnvironmentNetworkModeV1]

class LoopEnvironmentVersionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_ENVIRONMENT_VERSION_STATE_V1_UNSPECIFIED: _ClassVar[LoopEnvironmentVersionStateV1]
    LOOP_ENVIRONMENT_VERSION_STATE_V1_IMPORTING: _ClassVar[LoopEnvironmentVersionStateV1]
    LOOP_ENVIRONMENT_VERSION_STATE_V1_PUBLISHED: _ClassVar[LoopEnvironmentVersionStateV1]
    LOOP_ENVIRONMENT_VERSION_STATE_V1_REJECTED: _ClassVar[LoopEnvironmentVersionStateV1]
    LOOP_ENVIRONMENT_VERSION_STATE_V1_FAILED: _ClassVar[LoopEnvironmentVersionStateV1]

class LoopEnvironmentFailureCauseV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_ENVIRONMENT_FAILURE_CAUSE_V1_UNSPECIFIED: _ClassVar[LoopEnvironmentFailureCauseV1]
    LOOP_ENVIRONMENT_FAILURE_CAUSE_V1_TASK: _ClassVar[LoopEnvironmentFailureCauseV1]
    LOOP_ENVIRONMENT_FAILURE_CAUSE_V1_INFRASTRUCTURE: _ClassVar[LoopEnvironmentFailureCauseV1]
LOOP_ENVIRONMENT_PROFILE_V1_UNSPECIFIED: LoopEnvironmentProfileV1
LOOP_ENVIRONMENT_PROFILE_V1_SMALL: LoopEnvironmentProfileV1
LOOP_ENVIRONMENT_PROFILE_V1_MEDIUM: LoopEnvironmentProfileV1
LOOP_ENVIRONMENT_PROFILE_V1_LARGE: LoopEnvironmentProfileV1
LOOP_ENVIRONMENT_NETWORK_MODE_V1_UNSPECIFIED: LoopEnvironmentNetworkModeV1
LOOP_ENVIRONMENT_NETWORK_MODE_V1_OFFLINE: LoopEnvironmentNetworkModeV1
LOOP_ENVIRONMENT_VERSION_STATE_V1_UNSPECIFIED: LoopEnvironmentVersionStateV1
LOOP_ENVIRONMENT_VERSION_STATE_V1_IMPORTING: LoopEnvironmentVersionStateV1
LOOP_ENVIRONMENT_VERSION_STATE_V1_PUBLISHED: LoopEnvironmentVersionStateV1
LOOP_ENVIRONMENT_VERSION_STATE_V1_REJECTED: LoopEnvironmentVersionStateV1
LOOP_ENVIRONMENT_VERSION_STATE_V1_FAILED: LoopEnvironmentVersionStateV1
LOOP_ENVIRONMENT_FAILURE_CAUSE_V1_UNSPECIFIED: LoopEnvironmentFailureCauseV1
LOOP_ENVIRONMENT_FAILURE_CAUSE_V1_TASK: LoopEnvironmentFailureCauseV1
LOOP_ENVIRONMENT_FAILURE_CAUSE_V1_INFRASTRUCTURE: LoopEnvironmentFailureCauseV1

class LoopEnvironmentV1(_message.Message):
    __slots__ = ("environment_id", "name", "created_at", "description")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    name: str
    created_at: _timestamp_pb2.Timestamp
    description: str
    def __init__(self, environment_id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class LoopRegistryCredentialV1(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoopOciImageSourceV1(_message.Message):
    __slots__ = ("repository", "digest", "credential")
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    repository: str
    digest: str
    credential: LoopRegistryCredentialV1
    def __init__(self, repository: _Optional[str] = ..., digest: _Optional[str] = ..., credential: _Optional[_Union[LoopRegistryCredentialV1, _Mapping]] = ...) -> None: ...

class LoopDockerfileSourceV1(_message.Message):
    __slots__ = ("context_sha256", "dockerfile_path", "target", "build_args", "credential_registry", "credential", "image_manifest_sha256")
    CONTEXT_SHA256_FIELD_NUMBER: _ClassVar[int]
    DOCKERFILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    BUILD_ARGS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_MANIFEST_SHA256_FIELD_NUMBER: _ClassVar[int]
    context_sha256: bytes
    dockerfile_path: str
    target: str
    build_args: _containers.RepeatedCompositeFieldContainer[LoopBuildArgV1]
    credential_registry: str
    credential: LoopRegistryCredentialV1
    image_manifest_sha256: bytes
    def __init__(self, context_sha256: _Optional[bytes] = ..., dockerfile_path: _Optional[str] = ..., target: _Optional[str] = ..., build_args: _Optional[_Iterable[_Union[LoopBuildArgV1, _Mapping]]] = ..., credential_registry: _Optional[str] = ..., credential: _Optional[_Union[LoopRegistryCredentialV1, _Mapping]] = ..., image_manifest_sha256: _Optional[bytes] = ...) -> None: ...

class LoopBuildArgV1(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class LoopEnvironmentProfileRefV1(_message.Message):
    __slots__ = ("id", "version")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    id: LoopEnvironmentProfileV1
    version: int
    def __init__(self, id: _Optional[_Union[LoopEnvironmentProfileV1, str]] = ..., version: _Optional[int] = ...) -> None: ...

class LoopEnvironmentExecStepV1(_message.Message):
    __slots__ = ("argv", "timeout_millis")
    ARGV_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MILLIS_FIELD_NUMBER: _ClassVar[int]
    argv: _containers.RepeatedScalarFieldContainer[str]
    timeout_millis: int
    def __init__(self, argv: _Optional[_Iterable[str]] = ..., timeout_millis: _Optional[int] = ...) -> None: ...

class LoopEnvironmentFileV1(_message.Message):
    __slots__ = ("path", "content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: bytes
    def __init__(self, path: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...

class LoopEnvironmentVerifierV1(_message.Message):
    __slots__ = ("files", "argv", "bundle_sha256", "final_state_paths", "protected_paths", "start", "timeout_millis", "run_as_uid", "rewards", "failure_reward")
    FILES_FIELD_NUMBER: _ClassVar[int]
    ARGV_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_SHA256_FIELD_NUMBER: _ClassVar[int]
    FINAL_STATE_PATHS_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_PATHS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MILLIS_FIELD_NUMBER: _ClassVar[int]
    RUN_AS_UID_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REWARD_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[LoopEnvironmentFileV1]
    argv: _containers.RepeatedScalarFieldContainer[str]
    bundle_sha256: bytes
    final_state_paths: _containers.RepeatedScalarFieldContainer[str]
    protected_paths: _containers.RepeatedScalarFieldContainer[str]
    start: _containers.RepeatedCompositeFieldContainer[LoopEnvironmentExecStepV1]
    timeout_millis: int
    run_as_uid: int
    rewards: _containers.RepeatedCompositeFieldContainer[LoopEnvironmentRewardDeclV1]
    failure_reward: float
    def __init__(self, files: _Optional[_Iterable[_Union[LoopEnvironmentFileV1, _Mapping]]] = ..., argv: _Optional[_Iterable[str]] = ..., bundle_sha256: _Optional[bytes] = ..., final_state_paths: _Optional[_Iterable[str]] = ..., protected_paths: _Optional[_Iterable[str]] = ..., start: _Optional[_Iterable[_Union[LoopEnvironmentExecStepV1, _Mapping]]] = ..., timeout_millis: _Optional[int] = ..., run_as_uid: _Optional[int] = ..., rewards: _Optional[_Iterable[_Union[LoopEnvironmentRewardDeclV1, _Mapping]]] = ..., failure_reward: _Optional[float] = ...) -> None: ...

class LoopEnvironmentRewardDeclV1(_message.Message):
    __slots__ = ("name", "min", "max")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    name: str
    min: float
    max: float
    def __init__(self, name: _Optional[str] = ..., min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...

class LoopEnvironmentSpecV1(_message.Message):
    __slots__ = ("verifier", "profile", "network_mode", "setup_steps")
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_MODE_FIELD_NUMBER: _ClassVar[int]
    SETUP_STEPS_FIELD_NUMBER: _ClassVar[int]
    verifier: LoopEnvironmentVerifierV1
    profile: LoopEnvironmentProfileRefV1
    network_mode: LoopEnvironmentNetworkModeV1
    setup_steps: _containers.RepeatedCompositeFieldContainer[LoopEnvironmentExecStepV1]
    def __init__(self, verifier: _Optional[_Union[LoopEnvironmentVerifierV1, _Mapping]] = ..., profile: _Optional[_Union[LoopEnvironmentProfileRefV1, _Mapping]] = ..., network_mode: _Optional[_Union[LoopEnvironmentNetworkModeV1, str]] = ..., setup_steps: _Optional[_Iterable[_Union[LoopEnvironmentExecStepV1, _Mapping]]] = ...) -> None: ...

class LoopEnvironmentVersionV1(_message.Message):
    __slots__ = ("environment_id", "version", "oci_image", "dockerfile", "spec", "state", "reason_code", "signed_manifest", "environment_manifest_sha256", "critical_fixable", "high", "created_at", "finished_at", "revoked_at", "scan_report_only", "failure_cause", "storage_full")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OCI_IMAGE_FIELD_NUMBER: _ClassVar[int]
    DOCKERFILE_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_MANIFEST_SHA256_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_FIXABLE_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    SCAN_REPORT_ONLY_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CAUSE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FULL_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    version: int
    oci_image: LoopOciImageSourceV1
    dockerfile: LoopDockerfileSourceV1
    spec: LoopEnvironmentSpecV1
    state: LoopEnvironmentVersionStateV1
    reason_code: str
    signed_manifest: bytes
    environment_manifest_sha256: bytes
    critical_fixable: int
    high: int
    created_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    scan_report_only: bool
    failure_cause: LoopEnvironmentFailureCauseV1
    storage_full: bool
    def __init__(self, environment_id: _Optional[str] = ..., version: _Optional[int] = ..., oci_image: _Optional[_Union[LoopOciImageSourceV1, _Mapping]] = ..., dockerfile: _Optional[_Union[LoopDockerfileSourceV1, _Mapping]] = ..., spec: _Optional[_Union[LoopEnvironmentSpecV1, _Mapping]] = ..., state: _Optional[_Union[LoopEnvironmentVersionStateV1, str]] = ..., reason_code: _Optional[str] = ..., signed_manifest: _Optional[bytes] = ..., environment_manifest_sha256: _Optional[bytes] = ..., critical_fixable: _Optional[int] = ..., high: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., scan_report_only: _Optional[bool] = ..., failure_cause: _Optional[_Union[LoopEnvironmentFailureCauseV1, str]] = ..., storage_full: _Optional[bool] = ...) -> None: ...

class CreateLoopEnvironmentRequest(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateLoopEnvironmentResponse(_message.Message):
    __slots__ = ("environment",)
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: LoopEnvironmentV1
    def __init__(self, environment: _Optional[_Union[LoopEnvironmentV1, _Mapping]] = ...) -> None: ...

class CreateLoopEnvironmentVersionRequest(_message.Message):
    __slots__ = ("environment_id", "oci_image", "dockerfile", "spec", "scan_report_only", "request_id")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    OCI_IMAGE_FIELD_NUMBER: _ClassVar[int]
    DOCKERFILE_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    SCAN_REPORT_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    oci_image: LoopOciImageSourceV1
    dockerfile: LoopDockerfileSourceV1
    spec: LoopEnvironmentSpecV1
    scan_report_only: bool
    request_id: str
    def __init__(self, environment_id: _Optional[str] = ..., oci_image: _Optional[_Union[LoopOciImageSourceV1, _Mapping]] = ..., dockerfile: _Optional[_Union[LoopDockerfileSourceV1, _Mapping]] = ..., spec: _Optional[_Union[LoopEnvironmentSpecV1, _Mapping]] = ..., scan_report_only: _Optional[bool] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateLoopEnvironmentVersionResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: LoopEnvironmentVersionV1
    def __init__(self, version: _Optional[_Union[LoopEnvironmentVersionV1, _Mapping]] = ...) -> None: ...

class GetLoopEnvironmentVersionRequest(_message.Message):
    __slots__ = ("environment_id", "version")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    version: int
    def __init__(self, environment_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class GetLoopEnvironmentVersionResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: LoopEnvironmentVersionV1
    def __init__(self, version: _Optional[_Union[LoopEnvironmentVersionV1, _Mapping]] = ...) -> None: ...

class ListLoopEnvironmentVersionsRequest(_message.Message):
    __slots__ = ("environment_id", "page")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    page: _common_pb2.PageRequestV1
    def __init__(self, environment_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListLoopEnvironmentVersionsResponse(_message.Message):
    __slots__ = ("versions", "page", "environment")
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[LoopEnvironmentVersionV1]
    page: _common_pb2.PageResponseV1
    environment: LoopEnvironmentV1
    def __init__(self, versions: _Optional[_Iterable[_Union[LoopEnvironmentVersionV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., environment: _Optional[_Union[LoopEnvironmentV1, _Mapping]] = ...) -> None: ...

class ListLoopEnvironmentsRequest(_message.Message):
    __slots__ = ("page",)
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: _common_pb2.PageRequestV1
    def __init__(self, page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class LoopEnvironmentSummaryV1(_message.Message):
    __slots__ = ("environment", "newest", "latest_published")
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    NEWEST_FIELD_NUMBER: _ClassVar[int]
    LATEST_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    environment: LoopEnvironmentV1
    newest: LoopEnvironmentVersionV1
    latest_published: LoopEnvironmentVersionV1
    def __init__(self, environment: _Optional[_Union[LoopEnvironmentV1, _Mapping]] = ..., newest: _Optional[_Union[LoopEnvironmentVersionV1, _Mapping]] = ..., latest_published: _Optional[_Union[LoopEnvironmentVersionV1, _Mapping]] = ...) -> None: ...

class ListLoopEnvironmentsResponse(_message.Message):
    __slots__ = ("environments", "page")
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[LoopEnvironmentSummaryV1]
    page: _common_pb2.PageResponseV1
    def __init__(self, environments: _Optional[_Iterable[_Union[LoopEnvironmentSummaryV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class CreateLoopEnvironmentUploadRequest(_message.Message):
    __slots__ = ("sha256", "size_bytes")
    SHA256_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    sha256: bytes
    size_bytes: int
    def __init__(self, sha256: _Optional[bytes] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class CreateLoopEnvironmentUploadResponse(_message.Message):
    __slots__ = ("upload_url", "expires_at", "already_uploaded")
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ALREADY_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    upload_url: str
    expires_at: _timestamp_pb2.Timestamp
    already_uploaded: bool
    def __init__(self, upload_url: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., already_uploaded: _Optional[bool] = ...) -> None: ...

class LoopEnvironmentRejectionV1(_message.Message):
    __slots__ = ("reason_code", "field")
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    reason_code: str
    field: str
    def __init__(self, reason_code: _Optional[str] = ..., field: _Optional[str] = ...) -> None: ...
