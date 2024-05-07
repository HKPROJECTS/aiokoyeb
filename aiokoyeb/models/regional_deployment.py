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
    from .deployment_provisioning_info import DeploymentProvisioningInfo
    from .regional_deployment_definition import RegionalDeploymentDefinition
    from .regional_deployment_metadata import RegionalDeploymentMetadata
    from .regional_deployment_status import RegionalDeploymentStatus


class RegionalDeployment(KoyebModel):
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
    region: Optional[str] = Field(alias="region", default=None)
    parent_id: Optional[str] = Field(alias="parent_id", default=None)
    child_id: Optional[str] = Field(alias="child_id", default=None)
    status: Optional[RegionalDeploymentStatus] = Field(alias="status", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    definition: Optional[RegionalDeploymentDefinition] = Field(alias="definition", default=None)
    datacenters: Optional[list[str]] = Field(alias="datacenters", default=None)
    metadata: Optional[RegionalDeploymentMetadata] = Field(alias="metadata", default=None)
    provisioning_info: Optional[DeploymentProvisioningInfo] = Field(
        alias="provisioning_info", default=None
    )
    use_kuma_v2: Optional[bool] = Field(alias="use_kuma_v2", default=None)
    use_kata: Optional[bool] = Field(alias="use_kata", default=None)
    version: Optional[int] = Field(alias="version", default=None)
    deployment_group: Optional[str] = Field(alias="deployment_group", default=None)
    deployment_id: Optional[str] = Field(alias="deployment_id", default=None)
