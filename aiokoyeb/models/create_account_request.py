##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class CreateAccountRequest(KoyebModel):
    """
    Create new account
    """

    email: str = Field(alias="email", default=None)
    password: str = Field(alias="password", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    captcha: Optional[str] = Field(alias="captcha", default=None)
