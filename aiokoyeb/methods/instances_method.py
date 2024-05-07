##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import ExecCommandModel, GetInstanceModel, ListInstanceEventsModel, ListInstancesModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class InstancesMethod:
    async def list_instance_events(
        self: KoyebAPI,
        instance_ids: list[str] | None = None,
        types: list[str] | None = None,
        limit: str | None = None,
        offset: str | None = None,
        order: str | None = None,
    ):
        return await self.request(
            ListInstanceEventsModel(
                instance_ids=instance_ids, types=types, limit=limit, offset=offset, order=order
            )
        )

    async def list_instances(
        self: KoyebAPI,
        app_id: str | None = None,
        service_id: str | None = None,
        deployment_id: str | None = None,
        regional_deployment_id: str | None = None,
        allocation_id: str | None = None,
        statuses: list[str] | None = None,
        limit: str | None = None,
        offset: str | None = None,
        order: str | None = None,
        starting_time: str | None = None,
        ending_time: str | None = None,
    ):
        return await self.request(
            ListInstancesModel(
                app_id=app_id,
                service_id=service_id,
                deployment_id=deployment_id,
                regional_deployment_id=regional_deployment_id,
                allocation_id=allocation_id,
                statuses=statuses,
                limit=limit,
                offset=offset,
                order=order,
                starting_time=starting_time,
                ending_time=ending_time,
            )
        )

    async def get_instance(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetInstanceModel(id=id))

    async def exec_command(
        self: KoyebAPI,
        id: str | None = None,
        body_command: list[str] | None = None,
        body_tty_size_height: int | None = None,
        body_tty_size_width: int | None = None,
        body_stdin_data: str | None = None,
        body_stdin_close: bool | None = None,
        body_disableTty: bool | None = None,
        id_type: str | None = None,
    ):
        return await self.request(
            ExecCommandModel(
                id=id,
                body_command=body_command,
                body_tty_size_height=body_tty_size_height,
                body_tty_size_width=body_tty_size_width,
                body_stdin_data=body_stdin_data,
                body_stdin_close=body_stdin_close,
                body_disableTty=body_disableTty,
                id_type=id_type,
            )
        )
