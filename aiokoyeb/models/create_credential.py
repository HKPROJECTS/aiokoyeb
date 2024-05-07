##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import KoyebModel

if TYPE_CHECKING:
    from .credential_type import CredentialType


class CreateCredential(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    description: Optional[str] = Field(alias="description", default=None)
    type: Optional[CredentialType] = Field(alias="type", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
