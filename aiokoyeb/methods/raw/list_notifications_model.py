##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, NotificationList

from .base import KoyebMethod, KoyebType


class ListNotificationsModel(
    KoyebMethod[Error | ErrorWithFields | GooglerpcStatus | NotificationList]
):
    limit: str | None
    offset: str | None
    mark_read: str | None
    mark_seen: str | None
    unread: str | None
    unseen: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/notifications")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": NotificationList,
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
        if self.mark_read is not None:
            __query_params__["mark_read"] = self.mark_read
        if self.mark_seen is not None:
            __query_params__["mark_seen"] = self.mark_seen
        if self.unread is not None:
            __query_params__["unread"] = self.unread
        if self.unseen is not None:
            __query_params__["unseen"] = self.unseen
        return __query_params__
