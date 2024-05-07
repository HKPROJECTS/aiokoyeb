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
    KgitproxyResyncOrganizationReply,
)

from .base import KoyebMethod, KoyebType


class ResyncOrganizationModel(
    KoyebMethod[Error | GooglerpcStatus | ErrorWithFields | KgitproxyResyncOrganizationReply]
):
    organization_id: str

    @property
    def method(self) -> str:
        return "POST"

    @property
    def uri(self) -> str:
        return self._url_for(
            f"/v1/git/sync/organization/{self.organization_id}"
        )

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": KgitproxyResyncOrganizationReply,
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
