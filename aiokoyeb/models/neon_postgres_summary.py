##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class NeonPostgresSummary(KoyebModel):
    total: Optional[int] = Field(alias="total", default=None)
    by_instance_type: Optional[dict] = Field(alias="by_instance_type", default=None)
