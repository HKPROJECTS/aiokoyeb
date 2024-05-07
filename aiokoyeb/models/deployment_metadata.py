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
    from .database_deployment_metadata import DatabaseDeploymentMetadata
    from .git_deployment_metadata import GitDeploymentMetadata
    from .trigger_deployment_metadata import TriggerDeploymentMetadata


class DeploymentMetadata(KoyebModel):
    trigger: Optional[TriggerDeploymentMetadata] = Field(alias="trigger", default=None)
    database: Optional[DatabaseDeploymentMetadata] = Field(alias="database", default=None)
    git: Optional[GitDeploymentMetadata] = Field(alias="git", default=None)
