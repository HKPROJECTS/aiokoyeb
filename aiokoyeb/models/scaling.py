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
    from .deployment_scaling_target import DeploymentScalingTarget


class Scaling(KoyebModel):
    min: Optional[int] = Field(alias="min", default=None)
    max: Optional[int] = Field(alias="max", default=None)
    targets: Optional[list[DeploymentScalingTarget]] = Field(alias="targets", default=None)
