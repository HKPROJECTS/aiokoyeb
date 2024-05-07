##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class UpdateDomain(KoyebModel):
    app_id: Optional[str] = Field(alias="app_id", default=None)
    subdomain: Optional[str] = Field(alias="subdomain", default=None)
