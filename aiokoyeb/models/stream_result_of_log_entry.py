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
    from .googlerpc_status import GooglerpcStatus
    from .log_entry import LogEntry


class StreamResultOfLogEntry(KoyebModel):
    result: Optional[LogEntry] = Field(alias="result", default=None)
    error: Optional[GooglerpcStatus] = Field(alias="error", default=None)
