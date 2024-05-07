##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import KoyebModel

if TYPE_CHECKING:
    from .deployment_provisioning_info_stage_build_attempt import (
        DeploymentProvisioningInfoStageBuildAttempt,
    )
    from .deployment_provisioning_info_stage_status import DeploymentProvisioningInfoStageStatus


class DeploymentProvisioningInfoStage(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    status: Optional[DeploymentProvisioningInfoStageStatus] = Field(alias="status", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    started_at: Optional[datetime] = Field(alias="started_at", default=None)
    finished_at: Optional[datetime] = Field(alias="finished_at", default=None)
    build_attempts: Optional[list[DeploymentProvisioningInfoStageBuildAttempt]] = Field(
        alias="build_attempts", default=None
    )
