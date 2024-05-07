##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class InstanceUsage(KoyebModel):
    duration_seconds: Optional[int] = Field(alias="duration_seconds", default=None)
