##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import GetSubscriptionModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class SubscriptionsMethod:
    async def get_subscription(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetSubscriptionModel(id=id))
