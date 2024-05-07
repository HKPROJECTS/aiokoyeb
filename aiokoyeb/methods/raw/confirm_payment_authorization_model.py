##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import (
    ConfirmPaymentAuthorizationReply,
    Error,
    ErrorWithFields,
    GooglerpcStatus,
)

from .base import KoyebMethod, KoyebType


class ConfirmPaymentAuthorizationModel(
    KoyebMethod[ConfirmPaymentAuthorizationReply | GooglerpcStatus | ErrorWithFields | Error]
):
    id: str
    data: dict

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for(f"/v1/payment_methods/{self.id}/confirm")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": ConfirmPaymentAuthorizationReply,
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
