##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import CreateApp, UpdateApp

from .raw import (
    CreateAppModel,
    DeleteAppModel,
    GetAppModel,
    ListAppEventsModel,
    ListAppsModel,
    PauseAppModel,
    ResumeAppModel,
    UpdateApp2Model,
    UpdateAppModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class AppsMethod:
    async def list_app_events(
        self: KoyebAPI,
        app_id: str | None = None,
        types: list[str] | None = None,
        limit: str | None = None,
        offset: str | None = None,
        order: str | None = None,
    ):
        return await self.request(
            ListAppEventsModel(app_id=app_id, types=types, limit=limit, offset=offset, order=order)
        )

    async def list_apps(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        name: str | None = None,
    ):
        return await self.request(ListAppsModel(limit=limit, offset=offset, name=name))

    async def create_app(
        self: KoyebAPI,
        data: CreateApp,
    ):
        return await self.request(CreateAppModel(data=data))

    async def get_app(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetAppModel(id=id))

    async def update_app(
        self: KoyebAPI,
        id: str,
        data: UpdateApp,
        update_mask: str | None = None,
    ):
        return await self.request(UpdateAppModel(id=id, update_mask=update_mask, data=data))

    async def delete_app(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeleteAppModel(id=id))

    async def update_app2(
        self: KoyebAPI,
        id: str,
        data: UpdateApp,
        update_mask: str | None = None,
    ):
        return await self.request(UpdateApp2Model(id=id, update_mask=update_mask, data=data))

    async def pause_app(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(PauseAppModel(id=id))

    async def resume_app(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(ResumeAppModel(id=id))
