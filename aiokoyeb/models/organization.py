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
    from .organization_deactivation_reason import OrganizationDeactivationReason
    from .organization_detailed_status import OrganizationDetailedStatus
    from .organization_status import OrganizationStatus
    from .plan import Plan


class Organization(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    address1: Optional[str] = Field(alias="address1", default=None)
    address2: Optional[str] = Field(alias="address2", default=None)
    city: Optional[str] = Field(alias="city", default=None)
    postal_code: Optional[str] = Field(alias="postal_code", default=None)
    state: Optional[str] = Field(alias="state", default=None)
    country: Optional[str] = Field(alias="country", default=None)
    company: Optional[bool] = Field(alias="company", default=None)
    vat_number: Optional[str] = Field(alias="vat_number", default=None)
    billing_name: Optional[str] = Field(alias="billing_name", default=None)
    billing_email: Optional[str] = Field(alias="billing_email", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    plan: Optional[Plan] = Field(alias="plan", default=None)
    plan_updated_at: Optional[datetime] = Field(alias="plan_updated_at", default=None)
    has_payment_method: Optional[bool] = Field(alias="has_payment_method", default=None)
    subscription_id: Optional[str] = Field(alias="subscription_id", default=None)
    current_subscription_id: Optional[str] = Field(alias="current_subscription_id", default=None)
    latest_subscription_id: Optional[str] = Field(alias="latest_subscription_id", default=None)
    signup_qualification: Optional[dict] = Field(alias="signup_qualification", default=None)
    status: Optional[OrganizationStatus] = Field(alias="status", default=None)
    status_message: Optional[OrganizationDetailedStatus] = Field(
        alias="status_message", default=None
    )
    deactivation_reason: Optional[OrganizationDeactivationReason] = Field(
        alias="deactivation_reason", default=None
    )
    verified: Optional[bool] = Field(alias="verified", default=None)
    qualifies_for_hobby23: Optional[bool] = Field(alias="qualifies_for_hobby23", default=None)
    reprocess_after: Optional[datetime] = Field(alias="reprocess_after", default=None)
