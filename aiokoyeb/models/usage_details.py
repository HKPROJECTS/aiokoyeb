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


class UsageDetails(KoyebModel):
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    instance_id: Optional[str] = Field(alias="instance_id", default=None)
    app_id: Optional[str] = Field(alias="app_id", default=None)
    app_name: Optional[str] = Field(alias="app_name", default=None)
    service_id: Optional[str] = Field(alias="service_id", default=None)
    service_name: Optional[str] = Field(alias="service_name", default=None)
    regional_deployment_id: Optional[str] = Field(alias="regional_deployment_id", default=None)
    region: Optional[str] = Field(alias="region", default=None)
    deployment_id: Optional[str] = Field(alias="deployment_id", default=None)
    instance_type: Optional[str] = Field(alias="instance_type", default=None)
    duration_seconds: Optional[int] = Field(alias="duration_seconds", default=None)
    started_at: Optional[datetime] = Field(alias="started_at", default=None)
    terminated_at: Optional[datetime] = Field(alias="terminated_at", default=None)
