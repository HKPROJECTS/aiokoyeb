##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class HTTPHeader(KoyebModel):
    key: Optional[str] = Field(alias="key", default=None)
    value: Optional[str] = Field(alias="value", default=None)
