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
    UpdateUserRequestUserUpdateBody,
    UserReply,
)

from .base import KoyebMethod, KoyebType


class UpdateUserModel(
    KoyebMethod[
        GooglerpcStatus | Error | UpdateUserRequestUserUpdateBody | ErrorWithFields | UserReply
    ]
):
    update_mask: str | None
    data: UpdateUserRequestUserUpdateBody

    @property
    def method(self) -> str:
        return "PUT"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/account/profile")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": UserReply,
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
