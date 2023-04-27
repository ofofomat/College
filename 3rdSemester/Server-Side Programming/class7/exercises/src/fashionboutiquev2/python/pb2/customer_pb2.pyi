from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor


class Customer(_message.Message):
    __slots__ = ["email", "id", "nome"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    email: str
    id: Id
    nome: str
    def __init__(self, id: _Optional[_Union[Id, _Mapping]] = ...,
                 nome: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...


class Id(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

    def count():
        id += 1


class Request(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: int
    def __init__(self, request: _Optional[int] = ...) -> None: ...


class Response(_message.Message):
    __slots__ = ["http_status_code", "name", "operation"]

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADD: Response.Type
    ALTER: Response.Type
    DELETE: Response.Type
    HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    http_status_code: int
    name: str
    operation: Response.Type

    def __init__(self, operation: _Optional[_Union[Response.Type, str]] = ...,
                 name: _Optional[str] = ..., http_status_code: _Optional[int] = ...) -> None: ...
