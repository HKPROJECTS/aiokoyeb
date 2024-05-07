##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import GetOrganizationUsageDetailsReply, GooglerpcStatus

from .base import KoyebMethod, KoyebType


class GetOrganizationUsageDetailsModel(
    KoyebMethod[GetOrganizationUsageDetailsReply | GooglerpcStatus]
):
    starting_time: str | None
    ending_time: str | None
    limit: str | None
    offset: str | None
    order: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/usages/details")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": GetOrganizationUsageDetailsReply,
            "default": GooglerpcStatus,
        }

    @property
    def payload(self) -> dict:
        return {}

    @property
    def query_params(self) -> dict:
        __query_params__ = {}
        if self.starting_time is not None:
            __query_params__["starting_time"] = self.starting_time
        if self.ending_time is not None:
            __query_params__["ending_time"] = self.ending_time
        if self.limit is not None:
            __query_params__["limit"] = self.limit
        if self.offset is not None:
            __query_params__["offset"] = self.offset
        if self.order is not None:
            __query_params__["order"] = self.order
        return __query_params__
