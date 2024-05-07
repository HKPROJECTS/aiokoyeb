##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class UpdateUserRequestUserUpdateBody(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    email: Optional[str] = Field(alias="email", default=None)
    current_password: Optional[str] = Field(alias="current_password", default=None)
    password: Optional[str] = Field(alias="password", default=None)
    newsletter_subscribed: Optional[bool] = Field(alias="newsletter_subscribed", default=None)
    name: Optional[str] = Field(alias="name", default=None)
