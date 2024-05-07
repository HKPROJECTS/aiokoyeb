##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import GetOrganizationUsageReply, GooglerpcStatus

from .base import KoyebMethod, KoyebType


class GetOrganizationUsageModel(KoyebMethod[GooglerpcStatus | GetOrganizationUsageReply]):
    starting_time: str | None
    ending_time: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/usages")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": GetOrganizationUsageReply,
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
        return __query_params__
