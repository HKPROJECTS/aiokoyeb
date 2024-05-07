##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class ErrorField(KoyebModel):
    field: Optional[str] = Field(alias="field", default=None)
    description: Optional[str] = Field(alias="description", default=None)
