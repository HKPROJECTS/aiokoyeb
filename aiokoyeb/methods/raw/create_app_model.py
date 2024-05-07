##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import CreateApp, CreateAppReply, Error, ErrorWithFields, GooglerpcStatus

from .base import KoyebMethod, KoyebType


class CreateAppModel(
    KoyebMethod[GooglerpcStatus | Error | CreateAppReply | CreateApp | ErrorWithFields]
):
    data: CreateApp

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/apps")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": CreateAppReply,
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
