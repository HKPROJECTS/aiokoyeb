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
    from .deployment_database_info import DeploymentDatabaseInfo
    from .deployment_definition import DeploymentDefinition
    from .deployment_g_p_u_info import DeploymentGPUInfo
    from .deployment_metadata import DeploymentMetadata
    from .deployment_provisioning_info import DeploymentProvisioningInfo
    from .deployment_status import DeploymentStatus


class DeploymentListItem(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    allocated_at: Optional[datetime] = Field(alias="allocated_at", default=None)
    started_at: Optional[datetime] = Field(alias="started_at", default=None)
    succeeded_at: Optional[datetime] = Field(alias="succeeded_at", default=None)
    terminated_at: Optional[datetime] = Field(alias="terminated_at", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    app_id: Optional[str] = Field(alias="app_id", default=None)
    service_id: Optional[str] = Field(alias="service_id", default=None)
    parent_id: Optional[str] = Field(alias="parent_id", default=None)
    child_id: Optional[str] = Field(alias="child_id", default=None)
    status: Optional[DeploymentStatus] = Field(alias="status", default=None)
    metadata: Optional[DeploymentMetadata] = Field(alias="metadata", default=None)
    definition: Optional[DeploymentDefinition] = Field(alias="definition", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    provisioning_info: Optional[DeploymentProvisioningInfo] = Field(
        alias="provisioning_info", default=None
    )
    database_info: Optional[DeploymentDatabaseInfo] = Field(alias="database_info", default=None)
    gpu_info: Optional[DeploymentGPUInfo] = Field(alias="gpu_info", default=None)
    version: Optional[int] = Field(alias="version", default=None)
    deployment_group: Optional[str] = Field(alias="deployment_group", default=None)
