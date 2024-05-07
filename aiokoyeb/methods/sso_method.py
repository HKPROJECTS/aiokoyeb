##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import CannyAuthRequest, DiscourseAuthRequest

from .raw import CannyAuthModel, DiscourseAuthModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class SsoMethod:
    async def canny_auth(
        self: KoyebAPI,
        data: CannyAuthRequest,
    ):
        return await self.request(CannyAuthModel(data=data))

    async def discourse_auth(
        self: KoyebAPI,
        data: DiscourseAuthRequest,
    ):
        return await self.request(DiscourseAuthModel(data=data))
