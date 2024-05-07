##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import (
    GetRegionalDeploymentModel,
    ListRegionalDeploymentEventsModel,
    ListRegionalDeploymentsModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class RegionalDeploymentsMethod:
    async def list_regional_deployment_events(
        self: KoyebAPI,
        regional_deployment_id: str | None = None,
        types: list[str] | None = None,
        limit: str | None = None,
        offset: str | None = None,
        order: str | None = None,
    ):
        return await self.request(
            ListRegionalDeploymentEventsModel(
                regional_deployment_id=regional_deployment_id,
                types=types,
                limit=limit,
                offset=offset,
                order=order,
            )
        )

    async def list_regional_deployments(
        self: KoyebAPI,
        deployment_id: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
    ):
        return await self.request(
            ListRegionalDeploymentsModel(deployment_id=deployment_id, limit=limit, offset=offset)
        )

    async def get_regional_deployment(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetRegionalDeploymentModel(id=id))
