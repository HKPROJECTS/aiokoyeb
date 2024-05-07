##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class ExecCommandRequestTerminalSize(KoyebModel):
    height: Optional[int] = Field(alias="height", default=None)
    width: Optional[int] = Field(alias="width", default=None)
