##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class Quotas(KoyebModel):
    apps: Optional[int] = Field(alias="apps", default=None)
    services: Optional[int] = Field(alias="services", default=None)
    domains: Optional[int] = Field(alias="domains", default=None)
    services_by_app: Optional[int] = Field(alias="services_by_app", default=None)
    service_provisioning_concurrency: Optional[int] = Field(
        alias="service_provisioning_concurrency", default=None
    )
    memory_mb: Optional[int] = Field(alias="memory_mb", default=None)
    instance_types: Optional[list[str]] = Field(alias="instance_types", default=None)
    regions: Optional[list[str]] = Field(alias="regions", default=None)
    max_organization_members: Optional[int] = Field(alias="max_organization_members", default=None)
    max_instances_by_type: Optional[dict] = Field(alias="max_instances_by_type", default=None)
