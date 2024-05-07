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
    from .activity import Activity


class Notification(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    activity: Optional[Activity] = Field(alias="activity", default=None)
    is_read: Optional[bool] = Field(alias="is_read", default=None)
    is_seen: Optional[bool] = Field(alias="is_seen", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
