##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class CatalogGPUDetails(KoyebModel):
    count: Optional[int] = Field(alias="count", default=None)
    brand: Optional[str] = Field(alias="brand", default=None)
    memory: Optional[str] = Field(alias="memory", default=None)
