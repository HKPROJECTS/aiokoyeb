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
    from .database_source import DatabaseSource
    from .deployment_definition_type import DeploymentDefinitionType
    from .deployment_env import DeploymentEnv
    from .deployment_health_check import DeploymentHealthCheck
    from .deployment_instance_type import DeploymentInstanceType
    from .deployment_port import DeploymentPort
    from .deployment_route import DeploymentRoute
    from .deployment_scaling import DeploymentScaling
    from .docker_source import DockerSource
    from .git_source import GitSource


class DeploymentDefinition(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    type: Optional[DeploymentDefinitionType] = Field(alias="type", default=None)
    routes: Optional[list[DeploymentRoute]] = Field(alias="routes", default=None)
    ports: Optional[list[DeploymentPort]] = Field(alias="ports", default=None)
    env: Optional[list[DeploymentEnv]] = Field(alias="env", default=None)
    regions: Optional[list[str]] = Field(alias="regions", default=None)
    scalings: Optional[list[DeploymentScaling]] = Field(alias="scalings", default=None)
    instance_types: Optional[list[DeploymentInstanceType]] = Field(
        alias="instance_types", default=None
    )
    health_checks: Optional[list[DeploymentHealthCheck]] = Field(
        alias="health_checks", default=None
    )
    skip_cache: Optional[bool] = Field(alias="skip_cache", default=None)
    docker: Optional[DockerSource] = Field(alias="docker", default=None)
    git: Optional[GitSource] = Field(alias="git", default=None)
    database: Optional[DatabaseSource] = Field(alias="database", default=None)
