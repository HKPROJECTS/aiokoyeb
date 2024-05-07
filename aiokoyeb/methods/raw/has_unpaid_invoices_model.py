##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, HasUnpaidInvoicesReply

from .base import KoyebMethod, KoyebType


class HasUnpaidInvoicesModel(
    KoyebMethod[Error | ErrorWithFields | GooglerpcStatus | HasUnpaidInvoicesReply]
):
    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/billing/has_unpaid_invoices")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": HasUnpaidInvoicesReply,
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
