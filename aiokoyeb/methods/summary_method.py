##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import GetOrganizationSummaryModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class SummaryMethod:
    async def get_organization_summary(
        self: KoyebAPI,
        organization_id: str,
    ):
        return await self.request(GetOrganizationSummaryModel(organization_id=organization_id))
