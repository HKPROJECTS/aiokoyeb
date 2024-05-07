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
    from .organization_invitation import OrganizationInvitation


class GetUserOrganizationInvitationReply(KoyebModel):
    invitation: Optional[OrganizationInvitation] = Field(alias="invitation", default=None)
