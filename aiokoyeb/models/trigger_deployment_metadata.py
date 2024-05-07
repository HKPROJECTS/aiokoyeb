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
    from .trigger_deployment_metadata_actor_type import TriggerDeploymentMetadataActorType
    from .trigger_deployment_metadata_trigger_type import TriggerDeploymentMetadataTriggerType
    from .trigger_git_deployment_metadata import TriggerGitDeploymentMetadata


class TriggerDeploymentMetadata(KoyebModel):
    type: Optional[TriggerDeploymentMetadataTriggerType] = Field(alias="type", default=None)
    actor: Optional[TriggerDeploymentMetadataActorType] = Field(alias="actor", default=None)
    git: Optional[TriggerGitDeploymentMetadata] = Field(alias="git", default=None)
