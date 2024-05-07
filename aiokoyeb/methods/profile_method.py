##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import (
    CreateAccountRequest,
    OAuthCallbackRequest,
    ResendEmailValidationRequest,
    ResetPasswordRequest,
    UpdatePasswordRequest,
    UpdateUserRequestUserUpdateBody,
)

from .raw import (
    AcceptOrganizationInvitationModel,
    DeclineOrganizationInvitationModel,
    GetCurrentOrganizationModel,
    GetCurrentUserModel,
    GetOAuthOptionsModel,
    GetUserOrganizationInvitationModel,
    ListUserOrganizationInvitationsModel,
    OAuthCallbackModel,
    ResendEmailValidationModel,
    ResetPasswordModel,
    SignupModel,
    UpdatePasswordModel,
    UpdateUser2Model,
    UpdateUserModel,
    ValidateModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class ProfileMethod:
    async def get_o_auth_options(
        self: KoyebAPI,
        action: str | None = None,
        metadata: str | None = None,
    ):
        return await self.request(GetOAuthOptionsModel(action=action, metadata=metadata))

    async def o_auth_callback(
        self: KoyebAPI,
        data: OAuthCallbackRequest,
    ):
        return await self.request(OAuthCallbackModel(data=data))

    async def get_current_organization(self: KoyebAPI):
        return await self.request(GetCurrentOrganizationModel())

    async def list_user_organization_invitations(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        statuses: list[str] | None = None,
    ):
        return await self.request(
            ListUserOrganizationInvitationsModel(limit=limit, offset=offset, statuses=statuses)
        )

    async def get_user_organization_invitation(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetUserOrganizationInvitationModel(id=id))

    async def accept_organization_invitation(
        self: KoyebAPI,
        id: str,
        data: dict,
    ):
        return await self.request(AcceptOrganizationInvitationModel(id=id, data=data))

    async def decline_organization_invitation(
        self: KoyebAPI,
        id: str,
        data: dict,
    ):
        return await self.request(DeclineOrganizationInvitationModel(id=id, data=data))

    async def get_current_user(self: KoyebAPI):
        return await self.request(GetCurrentUserModel())

    async def update_user(
        self: KoyebAPI,
        data: UpdateUserRequestUserUpdateBody,
        update_mask: str | None = None,
    ):
        return await self.request(UpdateUserModel(update_mask=update_mask, data=data))

    async def update_user2(
        self: KoyebAPI,
        data: UpdateUserRequestUserUpdateBody,
        update_mask: str | None = None,
    ):
        return await self.request(UpdateUser2Model(update_mask=update_mask, data=data))

    async def resend_email_validation(
        self: KoyebAPI,
        data: ResendEmailValidationRequest,
    ):
        return await self.request(ResendEmailValidationModel(data=data))

    async def reset_password(
        self: KoyebAPI,
        data: ResetPasswordRequest,
    ):
        return await self.request(ResetPasswordModel(data=data))

    async def signup(
        self: KoyebAPI,
        data: CreateAccountRequest,
    ):
        return await self.request(SignupModel(data=data))

    async def update_password(
        self: KoyebAPI,
        data: UpdatePasswordRequest,
    ):
        return await self.request(UpdatePasswordModel(data=data))

    async def validate(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(ValidateModel(id=id))
