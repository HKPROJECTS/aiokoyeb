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
    from .user_flags import UserFlags


class User(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    email: Optional[str] = Field(alias="email", default=None)
    avatar_url: Optional[str] = Field(alias="avatar_url", default=None)
    two_factor_authentication: Optional[bool] = Field(
        alias="two_factor_authentication", default=None
    )
    last_login: Optional[datetime] = Field(alias="last_login", default=None)
    last_login_ip: Optional[str] = Field(alias="last_login_ip", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    newsletter_subscribed: Optional[bool] = Field(alias="newsletter_subscribed", default=None)
    github_id: Optional[str] = Field(alias="github_id", default=None)
    github_user: Optional[str] = Field(alias="github_user", default=None)
    flags: Optional[list[UserFlags]] = Field(alias="flags", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    email_validated: Optional[bool] = Field(alias="email_validated", default=None)
