##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class SubscriptionPaymentFailureStripeSDK(KoyebModel):
    client_secret_key: Optional[str] = Field(alias="client_secret_key", default=None)
    raw_json: Optional[str] = Field(alias="raw_json", default=None)
