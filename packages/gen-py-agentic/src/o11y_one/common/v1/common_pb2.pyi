from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SortDirectionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_DIRECTION_V1_UNSPECIFIED: _ClassVar[SortDirectionV1]
    SORT_DIRECTION_V1_DESC: _ClassVar[SortDirectionV1]
    SORT_DIRECTION_V1_ASC: _ClassVar[SortDirectionV1]
SORT_DIRECTION_V1_UNSPECIFIED: SortDirectionV1
SORT_DIRECTION_V1_DESC: SortDirectionV1
SORT_DIRECTION_V1_ASC: SortDirectionV1

class PageRequestV1(_message.Message):
    __slots__ = ("limit", "page_token")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_token: str
    def __init__(self, limit: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class PageResponseV1(_message.Message):
    __slots__ = ("next_page_token", "has_more", "total_count", "cursor_semantics", "total_count_approximate", "total_count_semantics")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_SEMANTICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_APPROXIMATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_SEMANTICS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    has_more: bool
    total_count: int
    cursor_semantics: str
    total_count_approximate: bool
    total_count_semantics: str
    def __init__(self, next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., total_count: _Optional[int] = ..., cursor_semantics: _Optional[str] = ..., total_count_approximate: _Optional[bool] = ..., total_count_semantics: _Optional[str] = ...) -> None: ...

class SortSpecV1(_message.Message):
    __slots__ = ("key", "direction")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    key: str
    direction: SortDirectionV1
    def __init__(self, key: _Optional[str] = ..., direction: _Optional[_Union[SortDirectionV1, str]] = ...) -> None: ...
