##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import GetMetricsModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class MetricsMethod:
    async def get_metrics(
        self: KoyebAPI,
        service_id: str | None = None,
        instance_id: str | None = None,
        name: str | None = None,
        start: str | None = None,
        end: str | None = None,
        step: str | None = None,
    ):
        return await self.request(
            GetMetricsModel(
                service_id=service_id,
                instance_id=instance_id,
                name=name,
                start=start,
                end=end,
                step=step,
            )
        )
