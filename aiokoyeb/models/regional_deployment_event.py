##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import KoyebModel


class RegionalDeploymentEvent(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    when: Optional[datetime] = Field(alias="when", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    regional_deployment_id: Optional[str] = Field(alias="regional_deployment_id", default=None)
    type: Optional[str] = Field(alias="type", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    metadata: Optional[dict] = Field(alias="metadata", default=None)
