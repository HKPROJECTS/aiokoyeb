##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import (
    CreateService,
    CreateServiceReply,
    Error,
    ErrorWithFields,
    GooglerpcStatus,
)

from .base import KoyebMethod, KoyebType


class CreateServiceModel(
    KoyebMethod[GooglerpcStatus | Error | CreateService | ErrorWithFields | CreateServiceReply]
):
    dry_run: bool | None
    data: CreateService

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/services")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": CreateServiceReply,
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
        return self.data

    @property
    def query_params(self) -> dict:
        __query_params__ = {}
        if self.dry_run is not None:
            __query_params__["dry_run"] = self.dry_run
        return __query_params__
