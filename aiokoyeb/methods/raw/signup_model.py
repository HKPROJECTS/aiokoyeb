##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import (
    CreateAccountRequest,
    Error,
    ErrorWithFields,
    GooglerpcStatus,
    LoginReply,
)

from .base import KoyebMethod, KoyebType


class SignupModel(
    KoyebMethod[CreateAccountRequest | Error | ErrorWithFields | GooglerpcStatus | LoginReply]
):
    data: CreateAccountRequest

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/account/signup")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": LoginReply,
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
