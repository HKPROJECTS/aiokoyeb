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
    from .deployment_health_check import DeploymentHealthCheck
    from .docker_source import DockerSource
    from .env import Env
    from .git_source import GitSource
    from .port import Port
    from .regional_deployment_definition_type import RegionalDeploymentDefinitionType
    from .route import Route
    from .scaling import Scaling


class RegionalDeploymentDefinition(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    type: Optional[RegionalDeploymentDefinitionType] = Field(alias="type", default=None)
    routes: Optional[list[Route]] = Field(alias="routes", default=None)
    ports: Optional[list[Port]] = Field(alias="ports", default=None)
    env: Optional[list[Env]] = Field(alias="env", default=None)
    region: Optional[str] = Field(alias="region", default=None)
    scaling: Optional[Scaling] = Field(alias="scaling", default=None)
    instance_type: Optional[str] = Field(alias="instance_type", default=None)
    deployment_group: Optional[str] = Field(alias="deployment_group", default=None)
    health_checks: Optional[list[DeploymentHealthCheck]] = Field(
        alias="health_checks", default=None
    )
    skip_cache: Optional[bool] = Field(alias="skip_cache", default=None)
    use_kuma_v2: Optional[bool] = Field(alias="use_kuma_v2", default=None)
    docker: Optional[DockerSource] = Field(alias="docker", default=None)
    git: Optional[GitSource] = Field(alias="git", default=None)
