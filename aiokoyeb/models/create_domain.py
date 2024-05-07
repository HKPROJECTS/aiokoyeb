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
    from .domain_type import DomainType


class CreateDomain(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    type: Optional[DomainType] = Field(alias="type", default=None)
    app_id: Optional[str] = Field(alias="app_id", default=None)
