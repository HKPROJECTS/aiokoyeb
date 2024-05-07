##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import ListBranchesModel, ListRepositoriesModel, ResyncOrganizationModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class RepositoriesMethod:
    async def list_branches(
        self: KoyebAPI,
        repository_id: str | None = None,
        name: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
    ):
        return await self.request(
            ListBranchesModel(repository_id=repository_id, name=name, limit=limit, offset=offset)
        )

    async def list_repositories(
        self: KoyebAPI,
        name: str | None = None,
        name_search_op: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
    ):
        return await self.request(
            ListRepositoriesModel(
                name=name, name_search_op=name_search_op, limit=limit, offset=offset
            )
        )

    async def resync_organization(
        self: KoyebAPI,
        organization_id: str,
    ):
        return await self.request(ResyncOrganizationModel(organization_id=organization_id))
