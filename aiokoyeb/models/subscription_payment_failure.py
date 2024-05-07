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
    from .subscription_payment_failure_stripe_s_d_k import SubscriptionPaymentFailureStripeSDK


class SubscriptionPaymentFailure(KoyebModel):
    failed_at: Optional[datetime] = Field(alias="failed_at", default=None)
    next_attempt: Optional[datetime] = Field(alias="next_attempt", default=None)
    attempt_count: Optional[int] = Field(alias="attempt_count", default=None)
    error_code: Optional[str] = Field(alias="error_code", default=None)
    error_reason: Optional[str] = Field(alias="error_reason", default=None)
    error_type: Optional[str] = Field(alias="error_type", default=None)
    error_message: Optional[str] = Field(alias="error_message", default=None)
    payment_method_required: Optional[bool] = Field(alias="payment_method_required", default=None)
    redirect_url: Optional[str] = Field(alias="redirect_url", default=None)
    stripe_sdk: Optional[SubscriptionPaymentFailureStripeSDK] = Field(
        alias="stripe_sdk", default=None
    )
