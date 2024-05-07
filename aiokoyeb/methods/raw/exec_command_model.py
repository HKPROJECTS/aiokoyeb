##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, StreamResultOfExecCommandReply

from .base import KoyebMethod, KoyebType


class ExecCommandModel(
    KoyebMethod[Error | ErrorWithFields | GooglerpcStatus | StreamResultOfExecCommandReply]
):
    id: str | None
    body_command: list[str] | None
    body_tty_size_height: int | None
    body_tty_size_width: int | None
    body_stdin_data: str | None
    body_stdin_close: bool | None
    body_disableTty: bool | None
    id_type: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/streams/instances/exec")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": StreamResultOfExecCommandReply,
            "400": ErrorWithFields,
            "401": Error,
            "403": Error,
            "404": Error,
            "500": Error,
            "503": Error,
            "default": GooglerpcStatus,
        }

    @property
    def payload(self) -> dict:
        return {}

    @property
    def query_params(self) -> dict:
        __query_params__ = {}
        if self.id is not None:
            __query_params__["id"] = self.id
        if self.body_command is not None:
            __query_params__["body.command"] = self.body_command
        if self.body_tty_size_height is not None:
            __query_params__["body.tty_size.height"] = self.body_tty_size_height
        if self.body_tty_size_width is not None:
            __query_params__["body.tty_size.width"] = self.body_tty_size_width
        if self.body_stdin_data is not None:
            __query_params__["body.stdin.data"] = self.body_stdin_data
        if self.body_stdin_close is not None:
            __query_params__["body.stdin.close"] = self.body_stdin_close
        if self.body_disableTty is not None:
            __query_params__["body.disableTty"] = self.body_disableTty
        if self.id_type is not None:
            __query_params__["id_type"] = self.id_type
        return __query_params__
