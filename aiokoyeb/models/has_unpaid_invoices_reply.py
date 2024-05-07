##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class HasUnpaidInvoicesReply(KoyebModel):
    has_unpaid_invoices: Optional[bool] = Field(alias="has_unpaid_invoices", default=None)
