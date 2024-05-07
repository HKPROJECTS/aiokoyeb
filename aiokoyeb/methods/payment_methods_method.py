##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import CreatePaymentAuthorizationRequest

from .raw import (
    ConfirmPaymentAuthorizationModel,
    CreatePaymentAuthorizationModel,
    DeletePaymentMethodModel,
    GetPaymentMethodModel,
    ListPaymentMethodsModel,
)

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class PaymentMethodsMethod:
    async def list_payment_methods(
        self: KoyebAPI,
        limit: str | None = None,
        offset: str | None = None,
        statuses: list[str] | None = None,
    ):
        return await self.request(
            ListPaymentMethodsModel(limit=limit, offset=offset, statuses=statuses)
        )

    async def create_payment_authorization(
        self: KoyebAPI,
        data: CreatePaymentAuthorizationRequest,
    ):
        return await self.request(CreatePaymentAuthorizationModel(data=data))

    async def get_payment_method(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(GetPaymentMethodModel(id=id))

    async def delete_payment_method(
        self: KoyebAPI,
        id: str,
    ):
        return await self.request(DeletePaymentMethodModel(id=id))

    async def confirm_payment_authorization(
        self: KoyebAPI,
        id: str,
        data: dict,
    ):
        return await self.request(ConfirmPaymentAuthorizationModel(id=id, data=data))
