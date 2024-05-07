##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import KoyebModel

if TYPE_CHECKING:
    from .catalog_g_p_u_details import CatalogGPUDetails


class CatalogInstance(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    description: Optional[str] = Field(alias="description", default=None)
    vcpu: Optional[int] = Field(alias="vcpu", default=None)
    memory: Optional[str] = Field(alias="memory", default=None)
    disk: Optional[str] = Field(alias="disk", default=None)
    price_hourly: Optional[str] = Field(alias="price_hourly", default=None)
    price_monthly: Optional[str] = Field(alias="price_monthly", default=None)
    regions: Optional[list[str]] = Field(alias="regions", default=None)
    status: Optional[str] = Field(alias="status", default=None)
    require_plan: Optional[list[str]] = Field(alias="require_plan", default=None)
    vcpu_shares: Optional[float] = Field(alias="vcpu_shares", default=None)
    display_name: Optional[str] = Field(alias="display_name", default=None)
    aliases: Optional[list[str]] = Field(alias="aliases", default=None)
    type: Optional[str] = Field(alias="type", default=None)
    gpu: Optional[CatalogGPUDetails] = Field(alias="gpu", default=None)
    service_types: Optional[list[str]] = Field(alias="service_types", default=None)
