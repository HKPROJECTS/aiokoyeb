##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import CreateService, RedeployRequestInfo, UpdateService

from .raw import (
    CreateServiceModel,
    DeleteServiceModel,
    GetServiceModel,
    ListServiceEventsModel,
    ListServicesModel,
    PauseServiceModel,
    ReDeployModel,
    ResumeServiceModel,
    UpdateService2Model,
    UpdateServiceModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class ServicesMethod:
    async def list_service_events(
        self: KoyebAPI,
        service_id: str | None = None,
        types: list[str] | None = None,
        limit: str | None = None,
        offset: str | None = None,
        order: str | None = None,
    ):
        return await self.request(
            ListServiceEventsModel(
                service_id=service_id, types=types, limit=limit, offset=offset, order=order
            )
        )

    async def list_services(
        self: KoyebAPI,
        app_id: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
        name: str | None = None,
        types: list[str] | None = None,
    ):
        return await self.request(
            ListServicesModel(app_id=app_id, limit=limit, offset=offset, name=name, types=types)
        )

    async def create_service(
        self: KoyebAPI,
        data: CreateService,
        dry_run: bool | None = None,
    ):
        return await self.request(CreateServiceModel(dry_run=dry_run, data=data))

    async def get_service(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetServiceModel(id=id))

    async def update_service(
        self: KoyebAPI,
        id: str,
        data: UpdateService,
        dry_run: bool | None = None,
    ):
        return await self.request(UpdateServiceModel(id=id, dry_run=dry_run, data=data))

    async def delete_service(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeleteServiceModel(id=id))

    async def update_service2(
        self: KoyebAPI,
        id: str,
        data: UpdateService,
        dry_run: bool | None = None,
    ):
        return await self.request(UpdateService2Model(id=id, dry_run=dry_run, data=data))

    async def pause_service(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(PauseServiceModel(id=id))

    async def re_deploy(
        self: KoyebAPI,
        id: str,
        data: RedeployRequestInfo,
    ):
        return await self.request(ReDeployModel(id=id, data=data))

    async def resume_service(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(ResumeServiceModel(id=id))
