##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class RegionListItem(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    coordinates: Optional[list[str]] = Field(alias="coordinates", default=None)
    status: Optional[str] = Field(alias="status", default=None)
    instances: Optional[list[str]] = Field(alias="instances", default=None)
    datacenters: Optional[list[str]] = Field(alias="datacenters", default=None)
