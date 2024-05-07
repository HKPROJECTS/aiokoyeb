##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import (
    CreateOrganizationRequest,
    GithubInstallationCallbackRequest,
    GithubInstallationRequest,
    Organization,
    UpdateOrganizationPlanRequest,
    UpsertSignupQualificationRequest,
)

from .raw import (
    CreateOrganizationModel,
    DeactivateOrganizationModel,
    DeleteOrganizationModel,
    GetGithubInstallationModel,
    GetOrganizationModel,
    GithubInstallationCallbackModel,
    GithubInstallationModel,
    ReactivateOrganizationModel,
    SwitchOrganizationModel,
    UpdateOrganization2Model,
    UpdateOrganizationModel,
    UpdateOrganizationPlanModel,
    UpsertSignupQualificationModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class OrganizationMethod:
    async def get_github_installation(self: KoyebAPI):
        return await self.request(GetGithubInstallationModel())

    async def github_installation(
        self: KoyebAPI,
        data: GithubInstallationRequest,
    ):
        return await self.request(GithubInstallationModel(data=data))

    async def github_installation_callback(
        self: KoyebAPI,
        data: GithubInstallationCallbackRequest,
    ):
        return await self.request(GithubInstallationCallbackModel(data=data))

    async def create_organization(
        self: KoyebAPI,
        data: CreateOrganizationRequest,
    ):
        return await self.request(CreateOrganizationModel(data=data))

    async def get_organization(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetOrganizationModel(id=id))

    async def update_organization(
        self: KoyebAPI,
        id: str,
        data: Organization,
        update_mask: str | None = None,
    ):
        return await self.request(
            UpdateOrganizationModel(id=id, update_mask=update_mask, data=data)
        )

    async def delete_organization(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeleteOrganizationModel(id=id))

    async def update_organization2(
        self: KoyebAPI,
        id: str,
        data: Organization,
        update_mask: str | None = None,
    ):
        return await self.request(
            UpdateOrganization2Model(id=id, update_mask=update_mask, data=data)
        )

    async def deactivate_organization(
        self: KoyebAPI,
        id: str,
        data: dict,
    ):
        return await self.request(DeactivateOrganizationModel(id=id, data=data))

    async def update_organization_plan(
        self: KoyebAPI,
        id: str,
        data: UpdateOrganizationPlanRequest,
    ):
        return await self.request(UpdateOrganizationPlanModel(id=id, data=data))

    async def reactivate_organization(
        self: KoyebAPI,
        id: str,
        data: dict,
    ):
        return await self.request(ReactivateOrganizationModel(id=id, data=data))

    async def upsert_signup_qualification(
        self: KoyebAPI,
        id: str,
        data: UpsertSignupQualificationRequest,
    ):
        return await self.request(UpsertSignupQualificationModel(id=id, data=data))

    async def switch_organization(
        self: KoyebAPI,
        id: str,
        data: dict,
    ):
        return await self.request(SwitchOrganizationModel(id=id, data=data))
