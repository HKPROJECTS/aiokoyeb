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
    from .subscription_payment_failure import SubscriptionPaymentFailure
    from .subscription_status import SubscriptionStatus


class Subscription(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    version: Optional[int] = Field(alias="version", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    stripe_subscription_id: Optional[str] = Field(alias="stripe_subscription_id", default=None)
    status: Optional[SubscriptionStatus] = Field(alias="status", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    has_pending_update: Optional[bool] = Field(alias="has_pending_update", default=None)
    stripe_pending_invoice_id: Optional[str] = Field(
        alias="stripe_pending_invoice_id", default=None
    )
    terminate_at: Optional[datetime] = Field(alias="terminate_at", default=None)
    canceled_at: Optional[datetime] = Field(alias="canceled_at", default=None)
    terminated_at: Optional[datetime] = Field(alias="terminated_at", default=None)
    current_period_start: Optional[datetime] = Field(alias="current_period_start", default=None)
    current_period_end: Optional[datetime] = Field(alias="current_period_end", default=None)
    currency: Optional[str] = Field(alias="currency", default=None)
    amount_payable: Optional[int] = Field(alias="amount_payable", default=None)
    amount_paid: Optional[int] = Field(alias="amount_paid", default=None)
    amount_remaining: Optional[int] = Field(alias="amount_remaining", default=None)
    payment_failure: Optional[SubscriptionPaymentFailure] = Field(
        alias="payment_failure", default=None
    )
