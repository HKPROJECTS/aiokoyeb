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
    from .deployment_provisioning_info_stage import DeploymentProvisioningInfoStage


class DeploymentProvisioningInfo(KoyebModel):
    sha: Optional[str] = Field(alias="sha", default=None)
    image: Optional[str] = Field(alias="image", default=None)
    stages: Optional[list[DeploymentProvisioningInfoStage]] = Field(alias="stages", default=None)
