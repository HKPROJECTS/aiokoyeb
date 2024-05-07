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
    from .deployment_definition import DeploymentDefinition
    from .deployment_metadata import DeploymentMetadata


class UpdateService(KoyebModel):
    definition: Optional[DeploymentDefinition] = Field(alias="definition", default=None)
    metadata: Optional[DeploymentMetadata] = Field(alias="metadata", default=None)
    skip_build: Optional[bool] = Field(alias="skip_build", default=None)
    save_only: Optional[bool] = Field(alias="save_only", default=None)
