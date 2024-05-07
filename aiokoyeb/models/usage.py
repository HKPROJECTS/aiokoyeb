##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class Usage(KoyebModel):
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    periods: Optional[dict] = Field(alias="periods", default=None)
