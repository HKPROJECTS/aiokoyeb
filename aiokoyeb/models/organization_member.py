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
    from .organization_member_status import OrganizationMemberStatus
    from .public_organization import PublicOrganization
    from .public_user import PublicUser
    from .user_role_role import UserRoleRole


class OrganizationMember(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    user_id: Optional[str] = Field(alias="user_id", default=None)
    joined_at: Optional[datetime] = Field(alias="joined_at", default=None)
    role: Optional[UserRoleRole] = Field(alias="role", default=None)
    status: Optional[OrganizationMemberStatus] = Field(alias="status", default=None)
    user: Optional[PublicUser] = Field(alias="user", default=None)
    organization: Optional[PublicOrganization] = Field(alias="organization", default=None)
