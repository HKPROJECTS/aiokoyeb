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
    from .object import Object


class Activity(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    actor: Optional[Object] = Field(alias="actor", default=None)
    object: Optional[Object] = Field(alias="object", default=None)
    verb: Optional[str] = Field(alias="verb", default=None)
    metadata: Optional[dict] = Field(alias="metadata", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
