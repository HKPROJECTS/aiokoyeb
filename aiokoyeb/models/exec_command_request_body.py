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
    from .exec_command_i_o import ExecCommandIO
    from .exec_command_request_terminal_size import ExecCommandRequestTerminalSize


class ExecCommandRequestBody(KoyebModel):
    command: Optional[list[str]] = Field(alias="command", default=None)
    tty_size: Optional[ExecCommandRequestTerminalSize] = Field(alias="tty_size", default=None)
    stdin: Optional[ExecCommandIO] = Field(alias="stdin", default=None)
    disableTty: Optional[bool] = Field(alias="disableTty", default=None)
