##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class ExecCommandIO(KoyebModel):
    data: Optional[bytes] = Field(alias="data", default=None)
    close: Optional[bool] = Field(alias="close", default=None)
