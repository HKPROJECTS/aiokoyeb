##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import CreateSecret, Secret

from .raw import (
    CreateSecretModel,
    DeleteSecretModel,
    GetSecretModel,
    ListSecretsModel,
    RevealSecretModel,
    UpdateSecret2Model,
    UpdateSecretModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class SecretsMethod:
    async def list_secrets(
        self: KoyebAPI,
        name: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
        types: list[str] | None = None,
    ):
        return await self.request(
            ListSecretsModel(name=name, limit=limit, offset=offset, types=types)
        )

    async def create_secret(
        self: KoyebAPI,
        data: CreateSecret,
    ):
        return await self.request(CreateSecretModel(data=data))

    async def get_secret(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetSecretModel(id=id))

    async def update_secret(
        self: KoyebAPI,
        id: str,
        data: Secret,
        update_mask: str | None = None,
    ):
        return await self.request(UpdateSecretModel(id=id, update_mask=update_mask, data=data))

    async def delete_secret(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeleteSecretModel(id=id))

    async def update_secret2(
        self: KoyebAPI,
        id: str,
        data: Secret,
        update_mask: str | None = None,
    ):
        return await self.request(UpdateSecret2Model(id=id, update_mask=update_mask, data=data))

    async def reveal_secret(
        self: KoyebAPI,
        id: str,
        data: dict,
    ):
        return await self.request(RevealSecretModel(id=id, data=data))
