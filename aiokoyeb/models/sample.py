##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class Sample(KoyebModel):
    timestamp: Optional[str] = Field(alias="timestamp", default=None)
    value: Optional[float] = Field(alias="value", default=None)
