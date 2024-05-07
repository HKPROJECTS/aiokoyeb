import aiohttp
from pydantic import BaseModel, TypeAdapter

from aiokoyeb.methods import Methods
from aiokoyeb.methods.raw import KoyebMethod, KoyebType


class KoyebAPI(Methods):
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    async def request(
        self,
        request: KoyebMethod[KoyebType],
        api_key: str = "",
    ) -> KoyebType:
        async with self.session.request(
            method=request.method,
            url=request.uri,
            headers={"Authorization": f"Bearer {api_key or self.api_key}"},
            json=(
                request.payload.model_dump(mode="json")
                if isinstance(request.payload, BaseModel)
                else request.payload
            ),
            params=request.query_params,
        ) as resp:
            if resp_model := request.responses.get(str(resp.status)):
                return TypeAdapter(resp_model).validate_python(await resp.json())

            return TypeAdapter(request.responses.get("default")).validate_python(await resp.json())
