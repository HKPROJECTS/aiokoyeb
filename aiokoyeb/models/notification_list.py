##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import KoyebModel

if TYPE_CHECKING:
    from .notification import Notification


class NotificationList(KoyebModel):
    notifications: Optional[list[Notification]] = Field(alias="notifications", default=None)
    limit: Optional[int] = Field(alias="limit", default=None)
    offset: Optional[int] = Field(alias="offset", default=None)
    count: Optional[int] = Field(alias="count", default=None)
    is_read: Optional[bool] = Field(alias="is_read", default=None)
    is_seen: Optional[bool] = Field(alias="is_seen", default=None)
    unread: Optional[int] = Field(alias="unread", default=None)
    unseen: Optional[int] = Field(alias="unseen", default=None)
