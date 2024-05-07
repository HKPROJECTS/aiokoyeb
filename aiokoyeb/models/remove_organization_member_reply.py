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
    from .organization_member import OrganizationMember


class RemoveOrganizationMemberReply(KoyebModel):
    member: Optional[OrganizationMember] = Field(alias="member", default=None)
