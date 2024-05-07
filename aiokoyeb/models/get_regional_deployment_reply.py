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
    from .regional_deployment import RegionalDeployment


class GetRegionalDeploymentReply(KoyebModel):
    regional_deployment: Optional[RegionalDeployment] = Field(
        alias="regional_deployment", default=None
    )
