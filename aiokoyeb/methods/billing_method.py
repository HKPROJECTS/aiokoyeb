##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import HasUnpaidInvoicesModel, ManageModel, NextInvoiceModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class BillingMethod:
    async def has_unpaid_invoices(self: KoyebAPI):
        return await self.request(HasUnpaidInvoicesModel())

    async def manage(self: KoyebAPI):
        return await self.request(ManageModel())

    async def next_invoice(self: KoyebAPI):
        return await self.request(NextInvoiceModel())
