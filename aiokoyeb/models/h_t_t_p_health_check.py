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
    from .h_t_t_p_header import HTTPHeader


class HTTPHealthCheck(KoyebModel):
    port: Optional[int] = Field(alias="port", default=None)
    path: Optional[str] = Field(alias="path", default=None)
    method: Optional[str] = Field(alias="method", default=None)
    headers: Optional[list[HTTPHeader]] = Field(alias="headers", default=None)
