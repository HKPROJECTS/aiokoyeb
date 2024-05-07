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
    from .ksearch_app import KsearchApp
    from .ksearch_global_deployment import KsearchGlobalDeployment
    from .ksearch_instance import KsearchInstance
    from .ksearch_organization import KsearchOrganization
    from .ksearch_regional_deployment import KsearchRegionalDeployment
    from .ksearch_service import KsearchService
    from .ksearch_user import KsearchUser


class KsearchSearchReply(KoyebModel):
    organizations: Optional[list[KsearchOrganization]] = Field(alias="organizations", default=None)
    users: Optional[list[KsearchUser]] = Field(alias="users", default=None)
    apps: Optional[list[KsearchApp]] = Field(alias="apps", default=None)
    services: Optional[list[KsearchService]] = Field(alias="services", default=None)
    global_deployments: Optional[list[KsearchGlobalDeployment]] = Field(
        alias="global_deployments", default=None
    )
    regional_deployments: Optional[list[KsearchRegionalDeployment]] = Field(
        alias="regional_deployments", default=None
    )
    instances: Optional[list[KsearchInstance]] = Field(alias="instances", default=None)
