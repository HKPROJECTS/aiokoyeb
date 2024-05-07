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
    from .app_status import AppStatus
    from .domain import Domain


class AppListItem(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    domains: Optional[list[Domain]] = Field(alias="domains", default=None)
    status: Optional[AppStatus] = Field(alias="status", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
