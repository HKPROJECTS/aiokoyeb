##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import KoyebModel


class LogEntry(KoyebModel):
    msg: Optional[str] = Field(alias="msg", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    labels: Optional[dict] = Field(alias="labels", default=None)
