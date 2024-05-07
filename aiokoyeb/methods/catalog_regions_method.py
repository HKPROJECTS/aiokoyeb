##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import GetRegionModel, ListRegionsModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class CatalogRegionsMethod:
    async def list_regions(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        id: str | None = None,
    ):
        return await self.request(ListRegionsModel(limit=limit, offset=offset, id=id))

    async def get_region(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetRegionModel(id=id))
