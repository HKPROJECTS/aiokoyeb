##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from aiokoyeb.models import LoginRequest

from .raw import LoginModel, LogoutModel, NewSessionModel, RefreshTokenModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class SessionsMethod:
    async def login(
        self: KoyebAPI,
        data: LoginRequest,
    ):
        return await self.request(LoginModel(data=data))

    async def logout(self: KoyebAPI):
        return await self.request(LogoutModel())

    async def refresh_token(self: KoyebAPI):
        return await self.request(RefreshTokenModel())

    async def new_session(self: KoyebAPI):
        return await self.request(NewSessionModel())
