##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class InviteUserRequest(KoyebModel):
    email: Optional[str] = Field(alias="email", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    message: Optional[str] = Field(alias="message", default=None)
