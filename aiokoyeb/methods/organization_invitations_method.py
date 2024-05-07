##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import CreateOrganizationInvitationRequest

from .raw import (
    CreateOrganizationInvitationModel,
    DeleteOrganizationInvitationModel,
    GetOrganizationInvitationModel,
    ListOrganizationInvitationsModel,
    ResendOrganizationInvitationModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class OrganizationInvitationsMethod:
    async def list_organization_invitations(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        statuses: list[str] | None = None,
        user_id: str | None = None,
    ):
        return await self.request(
            ListOrganizationInvitationsModel(
                limit=limit, offset=offset, statuses=statuses, user_id=user_id
            )
        )

    async def create_organization_invitation(
        self: KoyebAPI,
        data: CreateOrganizationInvitationRequest,
    ):
        return await self.request(CreateOrganizationInvitationModel(data=data))

    async def get_organization_invitation(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetOrganizationInvitationModel(id=id))

    async def delete_organization_invitation(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeleteOrganizationInvitationModel(id=id))

    async def resend_organization_invitation(
        self: KoyebAPI,
        id: str,
        data: dict,
    ):
        return await self.request(ResendOrganizationInvitationModel(id=id, data=data))
