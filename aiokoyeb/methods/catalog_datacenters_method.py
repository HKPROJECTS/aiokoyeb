##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import ListDatacentersModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class CatalogDatacentersMethod:
    async def list_datacenters(self: KoyebAPI):
        return await self.request(ListDatacentersModel())
