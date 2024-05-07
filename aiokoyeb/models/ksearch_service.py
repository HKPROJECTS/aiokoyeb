##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class KsearchService(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    app_id: Optional[str] = Field(alias="app_id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
