##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import (
    DiscourseAuthReply,
    DiscourseAuthRequest,
    Error,
    ErrorWithFields,
    GooglerpcStatus,
)

from .base import KoyebMethod, KoyebType


class DiscourseAuthModel(
    KoyebMethod[
        DiscourseAuthRequest | GooglerpcStatus | Error | ErrorWithFields | DiscourseAuthReply
    ]
):
    data: DiscourseAuthRequest

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/sso/discourse")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": DiscourseAuthReply,
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
