##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import TailLogsModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class LogsMethod:
    async def tail_logs(
        self: KoyebAPI,
        type: str | None = None,
        app_id: str | None = None,
        service_id: str | None = None,
        deployment_id: str | None = None,
        regional_deployment_id: str | None = None,
        instance_id: str | None = None,
        stream: str | None = None,
        start: str | None = None,
        limit: str | None = None,
    ):
        return await self.request(
            TailLogsModel(
                type=type,
                app_id=app_id,
                service_id=service_id,
                deployment_id=deployment_id,
                regional_deployment_id=regional_deployment_id,
                instance_id=instance_id,
                stream=stream,
                start=start,
                limit=limit,
            )
        )
