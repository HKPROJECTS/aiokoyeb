##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import ActivityList, Error, ErrorWithFields, GooglerpcStatus

from .base import KoyebMethod, KoyebType


class GetAccountActivitiesModel(
    KoyebMethod[ActivityList | GooglerpcStatus | ErrorWithFields | Error]
):
    limit: str | None
    offset: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/account/activities")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": ActivityList,
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
        if self.limit is not None:
            __query_params__["limit"] = self.limit
        if self.offset is not None:
            __query_params__["offset"] = self.offset
        return __query_params__
