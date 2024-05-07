##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GetMetricsReply, GooglerpcStatus

from .base import KoyebMethod, KoyebType


class GetMetricsModel(KoyebMethod[Error | ErrorWithFields | GetMetricsReply | GooglerpcStatus]):
    service_id: str | None
    instance_id: str | None
    name: str | None
    start: str | None
    end: str | None
    step: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/streams/metrics")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": GetMetricsReply,
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
        if self.service_id is not None:
            __query_params__["service_id"] = self.service_id
        if self.instance_id is not None:
            __query_params__["instance_id"] = self.instance_id
        if self.name is not None:
            __query_params__["name"] = self.name
        if self.start is not None:
            __query_params__["start"] = self.start
        if self.end is not None:
            __query_params__["end"] = self.end
        if self.step is not None:
            __query_params__["step"] = self.step
        return __query_params__
