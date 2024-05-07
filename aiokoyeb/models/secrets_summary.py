##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class SecretsSummary(KoyebModel):
    total: Optional[int] = Field(alias="total", default=None)
    by_type: Optional[dict] = Field(alias="by_type", default=None)
