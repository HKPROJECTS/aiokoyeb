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
    from .desired_deployment_group import DesiredDeploymentGroup


class DesiredDeployment(KoyebModel):
    groups: Optional[list[DesiredDeploymentGroup]] = Field(alias="groups", default=None)
