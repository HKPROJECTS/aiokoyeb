##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import GetCatalogInstanceModel, ListCatalogInstancesModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class CatalogInstancesMethod:
    async def list_catalog_instances(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        id: str | None = None,
    ):
        return await self.request(ListCatalogInstancesModel(limit=limit, offset=offset, id=id))

    async def get_catalog_instance(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetCatalogInstanceModel(id=id))
