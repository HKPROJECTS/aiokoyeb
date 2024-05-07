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
    UpdateService,
    UpdateServiceReply,
)

from .base import KoyebMethod, KoyebType


class UpdateService2Model(
    KoyebMethod[GooglerpcStatus | Error | UpdateService | UpdateServiceReply | ErrorWithFields]
):
    id: str
    dry_run: bool | None
    data: UpdateService

    @property
    def method(self) -> str:
        return "PATCH"

    @property
    def uri(self) -> str:
        return self._url_for(f"/v1/services/{self.id}")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": UpdateServiceReply,
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
