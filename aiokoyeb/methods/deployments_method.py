##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import (
    CancelDeploymentModel,
    GetDeploymentModel,
    ListDeploymentEventsModel,
    ListDeploymentsModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class DeploymentsMethod:
    async def list_deployment_events(
        self: KoyebAPI,
        deployment_id: str | None = None,
        types: list[str] | None = None,
        limit: str | None = None,
        offset: str | None = None,
        order: str | None = None,
    ):
        return await self.request(
            ListDeploymentEventsModel(
                deployment_id=deployment_id, types=types, limit=limit, offset=offset, order=order
            )
        )

    async def list_deployments(
        self: KoyebAPI,
        app_id: str | None = None,
        service_id: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
        statuses: list[str] | None = None,
    ):
        return await self.request(
            ListDeploymentsModel(
                app_id=app_id, service_id=service_id, limit=limit, offset=offset, statuses=statuses
            )
        )

    async def get_deployment(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetDeploymentModel(id=id))

    async def cancel_deployment(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(CancelDeploymentModel(id=id))
