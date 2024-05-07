##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class PublicUser(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    email: Optional[str] = Field(alias="email", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    avatar_url: Optional[str] = Field(alias="avatar_url", default=None)
    github_id: Optional[str] = Field(alias="github_id", default=None)
    github_user: Optional[str] = Field(alias="github_user", default=None)
