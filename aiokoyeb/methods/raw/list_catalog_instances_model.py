##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import GooglerpcStatus, ListCatalogInstancesReply

from .base import KoyebMethod, KoyebType


class ListCatalogInstancesModel(KoyebMethod[GooglerpcStatus | ListCatalogInstancesReply]):
    limit: str | None
    offset: str | None
    id: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/catalog/instances")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": ListCatalogInstancesReply,
            "default": GooglerpcStatus,
        }

    @property
    def payload(self) -> dict:
        return {}

    @property
    def query_params(self) -> dict:
        __query_params__ = {}
        if self.limit is not None:
            __query_params__["limit"] = self.limit
        if self.offset is not None:
            __query_params__["offset"] = self.offset
        if self.id is not None:
            __query_params__["id"] = self.id
        return __query_params__
