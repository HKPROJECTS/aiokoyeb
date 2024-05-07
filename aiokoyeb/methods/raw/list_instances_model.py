##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, ListInstancesReply

from .base import KoyebMethod, KoyebType


class ListInstancesModel(
    KoyebMethod[Error | ErrorWithFields | GooglerpcStatus | ListInstancesReply]
):
    app_id: str | None
    service_id: str | None
    deployment_id: str | None
    regional_deployment_id: str | None
    allocation_id: str | None
    statuses: list[str] | None
    limit: str | None
    offset: str | None
    order: str | None
    starting_time: str | None
    ending_time: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/instances")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": ListInstancesReply,
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
        if self.deployment_id is not None:
            __query_params__["deployment_id"] = self.deployment_id
        if self.regional_deployment_id is not None:
            __query_params__["regional_deployment_id"] = self.regional_deployment_id
        if self.allocation_id is not None:
            __query_params__["allocation_id"] = self.allocation_id
        if self.statuses is not None:
            __query_params__["statuses"] = self.statuses
        if self.limit is not None:
            __query_params__["limit"] = self.limit
        if self.offset is not None:
            __query_params__["offset"] = self.offset
        if self.order is not None:
            __query_params__["order"] = self.order
        if self.starting_time is not None:
            __query_params__["starting_time"] = self.starting_time
        if self.ending_time is not None:
            __query_params__["ending_time"] = self.ending_time
        return __query_params__
