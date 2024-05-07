##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class MembersSummary(KoyebModel):
    total: Optional[int] = Field(alias="total", default=None)
    invitations_by_status: Optional[dict] = Field(alias="invitations_by_status", default=None)
