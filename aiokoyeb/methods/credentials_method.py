##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import CreateCredential, Credential

from .raw import (
    CreateCredentialModel,
    DeleteCredentialModel,
    GetCredentialModel,
    ListCredentialsModel,
    UpdateCredential2Model,
    UpdateCredentialModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class CredentialsMethod:
    async def list_credentials(
        self: KoyebAPI,
        type: str | None = None,
        name: str | None = None,
        organization_id: str | None = None,
        user_id: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
    ):
        return await self.request(
            ListCredentialsModel(
                type=type,
                name=name,
                organization_id=organization_id,
                user_id=user_id,
                limit=limit,
                offset=offset,
            )
        )

    async def create_credential(
        self: KoyebAPI,
        data: CreateCredential,
    ):
        return await self.request(CreateCredentialModel(data=data))

    async def get_credential(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetCredentialModel(id=id))

    async def update_credential(
        self: KoyebAPI,
        id: str,
        data: Credential,
        update_mask: str | None = None,
    ):
        return await self.request(UpdateCredentialModel(id=id, update_mask=update_mask, data=data))

    async def delete_credential(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeleteCredentialModel(id=id))

    async def update_credential2(
        self: KoyebAPI,
        id: str,
        data: Credential,
        update_mask: str | None = None,
    ):
        return await self.request(UpdateCredential2Model(id=id, update_mask=update_mask, data=data))
