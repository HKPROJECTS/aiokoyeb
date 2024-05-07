##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import DeleteUserModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class UsersMethod:
    async def delete_user(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeleteUserModel(id=id))
