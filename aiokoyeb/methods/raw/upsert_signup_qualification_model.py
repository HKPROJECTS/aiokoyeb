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
    UpsertSignupQualificationReply,
    UpsertSignupQualificationRequest,
)

from .base import KoyebMethod, KoyebType


class UpsertSignupQualificationModel(
    KoyebMethod[
        Error
        | ErrorWithFields
        | GooglerpcStatus
        | UpsertSignupQualificationReply
        | UpsertSignupQualificationRequest
    ]
):
    id: str
    data: UpsertSignupQualificationRequest

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for(f"/v1/organizations/{self.id}/signup_qualification")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": UpsertSignupQualificationReply,
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
