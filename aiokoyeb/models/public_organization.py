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
    from .organization_status import OrganizationStatus
    from .plan import Plan


class PublicOrganization(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    plan: Optional[Plan] = Field(alias="plan", default=None)
    status: Optional[OrganizationStatus] = Field(alias="status", default=None)
