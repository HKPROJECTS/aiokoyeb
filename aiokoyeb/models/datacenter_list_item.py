##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class DatacenterListItem(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    region_id: Optional[str] = Field(alias="region_id", default=None)
    domain: Optional[str] = Field(alias="domain", default=None)
    coordinates: Optional[list[str]] = Field(alias="coordinates", default=None)
    use_kata: Optional[bool] = Field(alias="use_kata", default=None)
    use_gpu: Optional[bool] = Field(alias="use_gpu", default=None)
    use_kuma: Optional[bool] = Field(alias="use_kuma", default=None)
