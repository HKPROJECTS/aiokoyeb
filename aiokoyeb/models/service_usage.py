##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class ServiceUsage(KoyebModel):
    service_id: Optional[str] = Field(alias="service_id", default=None)
    service_name: Optional[str] = Field(alias="service_name", default=None)
    regions: Optional[dict] = Field(alias="regions", default=None)
