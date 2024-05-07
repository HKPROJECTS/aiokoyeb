##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from aiokoyeb.models import GooglerpcStatus, ListDatacentersReply

from .base import KoyebMethod, KoyebType


class ListDatacentersModel(KoyebMethod[ListDatacentersReply | GooglerpcStatus]):
    @property
    def method(self) -> str:
        return "GET"

    @property
    def uri(self) -> str:
        return self._url_for("/v1/catalog/datacenters")

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {
            "200": ListDatacentersReply,
            "default": GooglerpcStatus,
        }

    @property
    def payload(self) -> dict:
        return {}
