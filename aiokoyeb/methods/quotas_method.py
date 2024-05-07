##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import ReviewOrganizationCapacityRequest

from .raw import ReviewOrganizationCapacityModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class QuotasMethod:
    async def review_organization_capacity(
        self: KoyebAPI,
        data: ReviewOrganizationCapacityRequest,
    ):
        return await self.request(ReviewOrganizationCapacityModel(data=data))
