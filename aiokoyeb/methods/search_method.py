##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import SearchModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class SearchMethod:
    async def search(
        self: KoyebAPI,
        query: str | None = None,
    ):
        return await self.request(SearchModel(query=query))
