##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class OAuthProvider(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    url: Optional[str] = Field(alias="url", default=None)
    state: Optional[str] = Field(alias="state", default=None)
