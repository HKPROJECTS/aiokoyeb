##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class NeonPostgresDatabaseNeonRole(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    secret: Optional[str] = Field(alias="secret", default=None)
