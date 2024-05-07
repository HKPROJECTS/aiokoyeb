##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class Object(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    type: Optional[str] = Field(alias="type", default=None)
    metadata: Optional[dict] = Field(alias="metadata", default=None)
    deleted: Optional[bool] = Field(alias="deleted", default=None)
