##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class LoginRequest(KoyebModel):
    email: Optional[str] = Field(alias="email", default=None)
    password: Optional[str] = Field(alias="password", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
