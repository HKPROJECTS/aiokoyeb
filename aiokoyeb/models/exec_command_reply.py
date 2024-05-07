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


class ExecCommandReply(KoyebModel):
    stdout: Optional[ExecCommandIO] = Field(alias="stdout", default=None)
    stderr: Optional[ExecCommandIO] = Field(alias="stderr", default=None)
    exited: Optional[bool] = Field(alias="exited", default=None)
    exit_code: Optional[int] = Field(alias="exit_code", default=None)
