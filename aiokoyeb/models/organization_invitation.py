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
    from .organization_invitation_status import OrganizationInvitationStatus
    from .public_organization import PublicOrganization
    from .public_user import PublicUser
    from .user_role_role import UserRoleRole


class OrganizationInvitation(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    email: Optional[str] = Field(alias="email", default=None)
    role: Optional[UserRoleRole] = Field(alias="role", default=None)
    status: Optional[OrganizationInvitationStatus] = Field(alias="status", default=None)
    expires_at: Optional[datetime] = Field(alias="expires_at", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    organization: Optional[PublicOrganization] = Field(alias="organization", default=None)
    invitee_id: Optional[str] = Field(alias="invitee_id", default=None)
    invitee: Optional[PublicUser] = Field(alias="invitee", default=None)
    inviter_id: Optional[str] = Field(alias="inviter_id", default=None)
    inviter: Optional[PublicUser] = Field(alias="inviter", default=None)
