##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import KoyebModel


class Token(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    user_id: Optional[str] = Field(alias="user_id", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    expires_at: Optional[datetime] = Field(alias="expires_at", default=None)
