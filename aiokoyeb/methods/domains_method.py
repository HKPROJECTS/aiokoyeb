##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import CreateDomain, UpdateDomain

from .raw import (
    CreateDomainModel,
    DeleteDomainModel,
    GetDomainModel,
    ListDomainsModel,
    RefreshDomainStatusModel,
    UpdateDomainModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class DomainsMethod:
    async def list_domains(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        types: list[str] | None = None,
        statuses: list[str] | None = None,
        app_ids: list[str] | None = None,
        name: str | None = None,
    ):
        return await self.request(
            ListDomainsModel(
                limit=limit,
                offset=offset,
                types=types,
                statuses=statuses,
                app_ids=app_ids,
                name=name,
            )
        )

    async def create_domain(
        self: KoyebAPI,
        data: CreateDomain,
    ):
        return await self.request(CreateDomainModel(data=data))

    async def get_domain(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetDomainModel(id=id))

    async def delete_domain(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeleteDomainModel(id=id))

    async def update_domain(
        self: KoyebAPI,
        id: str,
        data: UpdateDomain,
        update_mask: str | None = None,
        dry_run: bool | None = None,
    ):
        return await self.request(
            UpdateDomainModel(id=id, update_mask=update_mask, dry_run=dry_run, data=data)
        )

    async def refresh_domain_status(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(RefreshDomainStatusModel(id=id))
