##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class ReviewOrganizationCapacityReply(KoyebModel):
    has_capacity: Optional[bool] = Field(alias="has_capacity", default=None)
