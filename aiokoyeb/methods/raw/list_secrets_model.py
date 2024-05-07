##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, ListSecretsReply

from .base import KoyebMethod, KoyebType


class ListSecretsModel(KoyebMethod[Error | ListSecretsReply | ErrorWithFields | GooglerpcStatus]):
    name: str | None
    limit: str | None
    offset: str | None
    types: list[str] | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/secrets")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": ListSecretsReply,
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
        if self.name is not None:
            __query_params__["name"] = self.name
        if self.limit is not None:
            __query_params__["limit"] = self.limit
        if self.offset is not None:
            __query_params__["offset"] = self.offset
        if self.types is not None:
            __query_params__["types"] = self.types
        return __query_params__
