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
    from .regional_deployment_list_item import RegionalDeploymentListItem


class ListRegionalDeploymentsReply(KoyebModel):
    regional_deployments: Optional[list[RegionalDeploymentListItem]] = Field(
        alias="regional_deployments", default=None
    )
    limit: Optional[int] = Field(alias="limit", default=None)
    offset: Optional[int] = Field(alias="offset", default=None)
    count: Optional[int] = Field(alias="count", default=None)
