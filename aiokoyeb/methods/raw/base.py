from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

KoyebType = TypeVar("KoyebType", bound=Any)

KOYEB_API_URL = "https://app.koyeb.com"


class KoyebMethod(BaseModel, Generic[KoyebType], ABC):
    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

    @property
    def responses(self) -> dict[str, KoyebType]:
        return {200: Any}

    @property
    def uri(self) -> str:
        raise NotImplementedError

    @property
    def query_params(self) -> dict[str, Any] | None:
        return None

    @property
    def payload(self) -> dict[str, Any] | None:
        return None

    @property
    def method(self) -> str:
        raise NotImplementedError

    def _url_for(self, *args, api: str = KOYEB_API_URL):
        return "/".join([api, *list(map(str, args))])
