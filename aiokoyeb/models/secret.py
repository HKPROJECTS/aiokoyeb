##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import KoyebModel

if TYPE_CHECKING:
    from .azure_container_registry_configuration import AzureContainerRegistryConfiguration
    from .database_role_password import DatabaseRolePassword
    from .digital_ocean_registry_configuration import DigitalOceanRegistryConfiguration
    from .docker_hub_registry_configuration import DockerHubRegistryConfiguration
    from .g_c_p_container_registry_configuration import GCPContainerRegistryConfiguration
    from .git_hub_registry_configuration import GitHubRegistryConfiguration
    from .git_lab_registry_configuration import GitLabRegistryConfiguration
    from .private_registry_configuration import PrivateRegistryConfiguration
    from .secret_type import SecretType


class Secret(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    type: Optional[SecretType] = Field(alias="type", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    value: Optional[str] = Field(alias="value", default=None)
    docker_hub_registry: Optional[DockerHubRegistryConfiguration] = Field(
        alias="docker_hub_registry", default=None
    )
    private_registry: Optional[PrivateRegistryConfiguration] = Field(
        alias="private_registry", default=None
    )
    digital_ocean_registry: Optional[DigitalOceanRegistryConfiguration] = Field(
        alias="digital_ocean_registry", default=None
    )
    github_registry: Optional[GitHubRegistryConfiguration] = Field(
        alias="github_registry", default=None
    )
    gitlab_registry: Optional[GitLabRegistryConfiguration] = Field(
        alias="gitlab_registry", default=None
    )
    gcp_container_registry: Optional[GCPContainerRegistryConfiguration] = Field(
        alias="gcp_container_registry", default=None
    )
    azure_container_registry: Optional[AzureContainerRegistryConfiguration] = Field(
        alias="azure_container_registry", default=None
    )
    database_role_password: Optional[DatabaseRolePassword] = Field(
        alias="database_role_password", default=None
    )
