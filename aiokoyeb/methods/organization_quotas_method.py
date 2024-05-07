##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import GetQuotasModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class OrganizationQuotasMethod:
    async def get_quotas(
        self: KoyebAPI,
        organization_id: str,
    ):
        return await self.request(GetQuotasModel(organization_id=organization_id))
