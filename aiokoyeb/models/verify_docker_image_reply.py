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
    from .verify_docker_image_reply_err_code import VerifyDockerImageReplyErrCode


class VerifyDockerImageReply(KoyebModel):
    success: Optional[bool] = Field(alias="success", default=None)
    reason: Optional[str] = Field(alias="reason", default=None)
    code: Optional[VerifyDockerImageReplyErrCode] = Field(alias="code", default=None)
