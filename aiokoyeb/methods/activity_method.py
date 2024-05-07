##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import GetAccountActivitiesModel, ListActivitiesModel, ListNotificationsModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class ActivityMethod:
    async def list_activities(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
    ):
        return await self.request(ListActivitiesModel(limit=limit, offset=offset))

    async def list_notifications(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        mark_read: str | None = None,
        mark_seen: str | None = None,
        unread: str | None = None,
        unseen: str | None = None,
    ):
        return await self.request(
            ListNotificationsModel(
                limit=limit,
                offset=offset,
                mark_read=mark_read,
                mark_seen=mark_seen,
                unread=unread,
                unseen=unseen,
            )
        )

    async def get_account_activities(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
    ):
        return await self.request(GetAccountActivitiesModel(limit=limit, offset=offset))
