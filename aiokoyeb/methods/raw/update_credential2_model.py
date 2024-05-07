##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import (
    Credential,
    Error,
    ErrorWithFields,
    GooglerpcStatus,
    UpdateCredentialReply,
)

from .base import KoyebMethod, KoyebType


class UpdateCredential2Model(
    KoyebMethod[UpdateCredentialReply | GooglerpcStatus | Error | Credential | ErrorWithFields]
):
    id: str
    update_mask: str | None
    data: Credential

    @property
    def method(self) -> str:
        return "PATCH"

    @property
    def uri(self) -> str:
        return self._url_for(f"/v1/credentials/{self.id}")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": UpdateCredentialReply,
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
        if self.update_mask is not None:
            __query_params__["update_mask"] = self.update_mask
        return __query_params__
