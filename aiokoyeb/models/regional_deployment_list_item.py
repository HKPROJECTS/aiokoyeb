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
    from .regional_deployment_definition import RegionalDeploymentDefinition
    from .regional_deployment_status import RegionalDeploymentStatus


class RegionalDeploymentListItem(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    region: Optional[str] = Field(alias="region", default=None)
    status: Optional[RegionalDeploymentStatus] = Field(alias="status", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    definition: Optional[RegionalDeploymentDefinition] = Field(alias="definition", default=None)
    use_kuma_v2: Optional[bool] = Field(alias="use_kuma_v2", default=None)
    use_kata: Optional[bool] = Field(alias="use_kata", default=None)
