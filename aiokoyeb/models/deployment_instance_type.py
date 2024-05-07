##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class DeploymentInstanceType(KoyebModel):
    scopes: Optional[list[str]] = Field(alias="scopes", default=None)
    type: Optional[str] = Field(alias="type", default=None)
