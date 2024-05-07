##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import InviteUserRequest

from .raw import CreateInviteModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class InviteMethod:
    async def create_invite(
        self: KoyebAPI,
        data: InviteUserRequest,
    ):
        return await self.request(CreateInviteModel(data=data))
