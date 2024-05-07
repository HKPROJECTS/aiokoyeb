##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import ListOrganizationMembersModel, RemoveOrganizationMemberModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class OrganizationMembersMethod:
    async def list_organization_members(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        organization_id: str | None = None,
        user_id: str | None = None,
    ):
        return await self.request(
            ListOrganizationMembersModel(
                limit=limit, offset=offset, organization_id=organization_id, user_id=user_id
            )
        )

    async def remove_organization_member(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(RemoveOrganizationMemberModel(id=id))
