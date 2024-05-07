##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import KoyebModel

if TYPE_CHECKING:
    from .app_usage import AppUsage


class PeriodUsage(KoyebModel):
    starting_time: Optional[datetime] = Field(alias="starting_time", default=None)
    ending_time: Optional[datetime] = Field(alias="ending_time", default=None)
    apps: Optional[list[AppUsage]] = Field(alias="apps", default=None)
