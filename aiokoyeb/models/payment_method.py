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
    from .payment_method_status import PaymentMethodStatus


class PaymentMethod(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    version: Optional[int] = Field(alias="version", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    type: Optional[str] = Field(alias="type", default=None)
    provider: Optional[str] = Field(alias="provider", default=None)
    status: Optional[PaymentMethodStatus] = Field(alias="status", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    stripe_payment_method_id: Optional[str] = Field(alias="stripe_payment_method_id", default=None)
    authorization_verified_at: Optional[datetime] = Field(
        alias="authorization_verified_at", default=None
    )
    authorization_canceled_at: Optional[datetime] = Field(
        alias="authorization_canceled_at", default=None
    )
    authorization_stripe_payment_intent_id: Optional[str] = Field(
        alias="authorization_stripe_payment_intent_id", default=None
    )
    authorization_stripe_payment_intent_client_secret: Optional[str] = Field(
        alias="authorization_stripe_payment_intent_client_secret", default=None
    )
    card_brand: Optional[str] = Field(alias="card_brand", default=None)
    card_country: Optional[str] = Field(alias="card_country", default=None)
    card_funding: Optional[str] = Field(alias="card_funding", default=None)
    card_fingerprint: Optional[str] = Field(alias="card_fingerprint", default=None)
    card_last_digits: Optional[str] = Field(alias="card_last_digits", default=None)
    card_expiration_month: Optional[int] = Field(alias="card_expiration_month", default=None)
    card_expiration_year: Optional[int] = Field(alias="card_expiration_year", default=None)
