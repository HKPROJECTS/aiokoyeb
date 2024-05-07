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
    from .deployment_scaling_target_average_c_p_u import DeploymentScalingTargetAverageCPU
    from .deployment_scaling_target_average_mem import DeploymentScalingTargetAverageMem
    from .deployment_scaling_target_requests_per_second import (
        DeploymentScalingTargetRequestsPerSecond,
    )


class DeploymentScalingTarget(KoyebModel):
    average_cpu: Optional[DeploymentScalingTargetAverageCPU] = Field(
        alias="average_cpu", default=None
    )
    average_mem: Optional[DeploymentScalingTargetAverageMem] = Field(
        alias="average_mem", default=None
    )
    requests_per_second: Optional[DeploymentScalingTargetRequestsPerSecond] = Field(
        alias="requests_per_second", default=None
    )
