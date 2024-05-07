##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, KsearchSearchReply

from .base import KoyebMethod, KoyebType


class SearchModel(KoyebMethod[Error | ErrorWithFields | GooglerpcStatus | KsearchSearchReply]):
    query: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/search")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": KsearchSearchReply,
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
        if self.query is not None:
            __query_params__["query"] = self.query
        return __query_params__
