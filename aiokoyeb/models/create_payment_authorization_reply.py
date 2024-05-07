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
    from .payment_method import PaymentMethod


class CreatePaymentAuthorizationReply(KoyebModel):
    payment_method: Optional[PaymentMethod] = Field(alias="payment_method", default=None)
