##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import Error, ErrorWithFields, GooglerpcStatus, VerifyDockerImageReply

from .base import KoyebMethod, KoyebType


class VerifyDockerImageModel(
    KoyebMethod[Error | ErrorWithFields | GooglerpcStatus | VerifyDockerImageReply]
):
    image: str | None
    secret_id: str | None

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/docker-helper/verify")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": VerifyDockerImageReply,
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
        if self.image is not None:
            __query_params__["image"] = self.image
        if self.secret_id is not None:
            __query_params__["secret_id"] = self.secret_id
        return __query_params__
