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
    from .credential_type import CredentialType


class Credential(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    type: Optional[CredentialType] = Field(alias="type", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    token: Optional[str] = Field(alias="token", default=None)
    description: Optional[str] = Field(alias="description", default=None)
    user_id: Optional[str] = Field(alias="user_id", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
