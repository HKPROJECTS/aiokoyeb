##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import (
    Error,
    ErrorWithFields,
    GithubInstallationCallbackReply,
    GithubInstallationCallbackRequest,
    GooglerpcStatus,
)

from .base import KoyebMethod, KoyebType


class GithubInstallationCallbackModel(
    KoyebMethod[
        Error
        | ErrorWithFields
        | GithubInstallationCallbackReply
        | GithubInstallationCallbackRequest
        | GooglerpcStatus
    ]
):
    data: GithubInstallationCallbackRequest

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/github/installation/callback")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": GithubInstallationCallbackReply,
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
