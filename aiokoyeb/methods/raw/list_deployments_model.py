##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, ListDeploymentsReply

from .base import KoyebMethod, KoyebType


class ListDeploymentsModel(
    KoyebMethod[Error | GooglerpcStatus | ErrorWithFields | ListDeploymentsReply]
):
    app_id: str | None
    service_id: str | None
    limit: str | None
    offset: str | None
    statuses: list[str] | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/deployments")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": ListDeploymentsReply,
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
        if self.app_id is not None:
            __query_params__["app_id"] = self.app_id
        if self.service_id is not None:
            __query_params__["service_id"] = self.service_id
        if self.limit is not None:
            __query_params__["limit"] = self.limit
        if self.offset is not None:
            __query_params__["offset"] = self.offset
        if self.statuses is not None:
            __query_params__["statuses"] = self.statuses
        return __query_params__
