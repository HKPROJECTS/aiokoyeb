##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class DesiredDeploymentGroup(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    deployment_ids: Optional[list[str]] = Field(alias="deployment_ids", default=None)
