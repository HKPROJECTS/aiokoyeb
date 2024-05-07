##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import ConfirmOrganizationActionModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class OrganizationConfirmationsMethod:
    async def confirm_organization_action(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(ConfirmOrganizationActionModel(id=id))
