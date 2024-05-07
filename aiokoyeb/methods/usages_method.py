##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import GetOrganizationUsageDetailsModel, GetOrganizationUsageModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class UsagesMethod:
    async def get_organization_usage(
        self: KoyebAPI,
        starting_time: str | None = None,
        ending_time: str | None = None,
    ):
        return await self.request(
            GetOrganizationUsageModel(starting_time=starting_time, ending_time=ending_time)
        )

    async def get_organization_usage_details(
        self: KoyebAPI,
        starting_time: str | None = None,
        ending_time: str | None = None,
        limit: str | None = None,
        offset: str | None = None,
        order: str | None = None,
    ):
        return await self.request(
            GetOrganizationUsageDetailsModel(
                starting_time=starting_time,
                ending_time=ending_time,
                limit=limit,
                offset=offset,
                order=order,
            )
        )
