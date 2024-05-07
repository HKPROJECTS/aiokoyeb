##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class DiscourseAuthReply(KoyebModel):
    sso: Optional[str] = Field(alias="sso", default=None)
    sig: Optional[str] = Field(alias="sig", default=None)
