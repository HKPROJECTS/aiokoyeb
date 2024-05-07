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


class CreateService(KoyebModel):
    app_id: Optional[str] = Field(alias="app_id", default=None)
    definition: Optional[DeploymentDefinition] = Field(alias="definition", default=None)
