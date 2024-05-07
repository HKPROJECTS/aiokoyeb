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
    from .trigger_git_deployment_metadata_provider import TriggerGitDeploymentMetadataProvider


class TriggerGitDeploymentMetadata(KoyebModel):
    provider: Optional[TriggerGitDeploymentMetadataProvider] = Field(alias="provider", default=None)
    repository: Optional[str] = Field(alias="repository", default=None)
    branch: Optional[str] = Field(alias="branch", default=None)
    sha: Optional[str] = Field(alias="sha", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    sender_username: Optional[str] = Field(alias="sender_username", default=None)
    sender_avatar_url: Optional[str] = Field(alias="sender_avatar_url", default=None)
    sender_profile_url: Optional[str] = Field(alias="sender_profile_url", default=None)
