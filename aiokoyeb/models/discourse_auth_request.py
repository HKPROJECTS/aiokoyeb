##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class DiscourseAuthRequest(KoyebModel):
    payload: Optional[str] = Field(alias="payload", default=None)
    sig: Optional[str] = Field(alias="sig", default=None)
