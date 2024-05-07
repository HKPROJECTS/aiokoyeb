##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import KoyebModel

if TYPE_CHECKING:
    from .service_state import ServiceState
    from .service_status import ServiceStatus
    from .service_type import ServiceType


class Service(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    started_at: Optional[datetime] = Field(alias="started_at", default=None)
    succeeded_at: Optional[datetime] = Field(alias="succeeded_at", default=None)
    paused_at: Optional[datetime] = Field(alias="paused_at", default=None)
    resumed_at: Optional[datetime] = Field(alias="resumed_at", default=None)
    terminated_at: Optional[datetime] = Field(alias="terminated_at", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    type: Optional[ServiceType] = Field(alias="type", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    app_id: Optional[str] = Field(alias="app_id", default=None)
    status: Optional[ServiceStatus] = Field(alias="status", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    version: Optional[int] = Field(alias="version", default=None)
    active_deployment_id: Optional[str] = Field(alias="active_deployment_id", default=None)
    latest_deployment_id: Optional[str] = Field(alias="latest_deployment_id", default=None)
    last_provisioned_deployment_id: Optional[str] = Field(
        alias="last_provisioned_deployment_id", default=None
    )
    state: Optional[ServiceState] = Field(alias="state", default=None)
