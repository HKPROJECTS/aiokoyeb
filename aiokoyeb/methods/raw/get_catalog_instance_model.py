##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import GetCatalogInstanceReply, GooglerpcStatus

from .base import KoyebMethod, KoyebType


class GetCatalogInstanceModel(KoyebMethod[GetCatalogInstanceReply | GooglerpcStatus]):
    id: str

    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for(f"/v1/catalog/instances/{self.id}")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": GetCatalogInstanceReply,
            "default": GooglerpcStatus,
        }

    @property
    def payload(self) -> dict:
        return {}
