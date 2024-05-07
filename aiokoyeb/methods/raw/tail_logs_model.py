##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, StreamResultOfLogEntry

from .base import KoyebMethod, KoyebType


class TailLogsModel(
    KoyebMethod[Error | StreamResultOfLogEntry | GooglerpcStatus | ErrorWithFields]
):
    type: str | None
    app_id: str | None
    service_id: str | None
    deployment_id: str | None
    regional_deployment_id: str | None
    instance_id: str | None
    stream: str | None
    start: str | None
    limit: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/streams/logs/tail")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": StreamResultOfLogEntry,
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
        if self.type is not None:
            __query_params__["type"] = self.type
        if self.app_id is not None:
            __query_params__["app_id"] = self.app_id
        if self.service_id is not None:
            __query_params__["service_id"] = self.service_id
        if self.deployment_id is not None:
            __query_params__["deployment_id"] = self.deployment_id
        if self.regional_deployment_id is not None:
            __query_params__["regional_deployment_id"] = self.regional_deployment_id
        if self.instance_id is not None:
            __query_params__["instance_id"] = self.instance_id
        if self.stream is not None:
            __query_params__["stream"] = self.stream
        if self.start is not None:
            __query_params__["start"] = self.start
        if self.limit is not None:
            __query_params__["limit"] = self.limit
        return __query_params__
