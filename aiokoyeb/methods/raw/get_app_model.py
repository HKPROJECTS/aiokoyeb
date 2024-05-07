##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GetAppReply, GooglerpcStatus

from .base import KoyebMethod, KoyebType


class GetAppModel(KoyebMethod[Error | ErrorWithFields | GetAppReply | GooglerpcStatus]):
    id: str

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for(f"/v1/apps/{self.id}")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": GetAppReply,
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
