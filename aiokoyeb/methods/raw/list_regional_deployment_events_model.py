##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import (
    Error,
    ErrorWithFields,
    GooglerpcStatus,
    ListRegionalDeploymentEventsReply,
)

from .base import KoyebMethod, KoyebType


class ListRegionalDeploymentEventsModel(
    KoyebMethod[Error | ErrorWithFields | GooglerpcStatus | ListRegionalDeploymentEventsReply]
):
    regional_deployment_id: str | None
    types: list[str] | None
    limit: str | None
    offset: str | None
    order: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/regional_deployment_events")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": ListRegionalDeploymentEventsReply,
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
        if self.regional_deployment_id is not None:
            __query_params__["regional_deployment_id"] = self.regional_deployment_id
        if self.types is not None:
            __query_params__["types"] = self.types
        if self.limit is not None:
            __query_params__["limit"] = self.limit
        if self.offset is not None:
            __query_params__["offset"] = self.offset
        if self.order is not None:
            __query_params__["order"] = self.order
        return __query_params__
