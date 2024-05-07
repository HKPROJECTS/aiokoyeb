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
    from .googleprotobuf_any import GoogleprotobufAny


class GooglerpcStatus(KoyebModel):
    code: Optional[int] = Field(alias="code", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    details: Optional[list[GoogleprotobufAny]] = Field(alias="details", default=None)
