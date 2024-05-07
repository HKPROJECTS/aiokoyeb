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
    from .instance_status import InstanceStatus


class InstanceListItem(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    app_id: Optional[str] = Field(alias="app_id", default=None)
    service_id: Optional[str] = Field(alias="service_id", default=None)
    regional_deployment_id: Optional[str] = Field(alias="regional_deployment_id", default=None)
    allocation_id: Optional[str] = Field(alias="allocation_id", default=None)
    region: Optional[str] = Field(alias="region", default=None)
    datacenter: Optional[str] = Field(alias="datacenter", default=None)
    status: Optional[InstanceStatus] = Field(alias="status", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    xyz_deployment_id: Optional[str] = Field(alias="xyz_deployment_id", default=None)
