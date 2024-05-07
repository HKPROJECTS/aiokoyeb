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
    RedeployReply,
    RedeployRequestInfo,
)

from .base import KoyebMethod, KoyebType


class ReDeployModel(
    KoyebMethod[GooglerpcStatus | RedeployRequestInfo | Error | RedeployReply | ErrorWithFields]
):
    id: str
    data: RedeployRequestInfo

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for(f"/v1/services/{self.id}/redeploy")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": RedeployReply,
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
