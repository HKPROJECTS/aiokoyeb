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
    from .buildpack_builder import BuildpackBuilder
    from .docker_builder import DockerBuilder


class GitSource(KoyebModel):
    repository: Optional[str] = Field(alias="repository", default=None)
    branch: Optional[str] = Field(alias="branch", default=None)
    tag: Optional[str] = Field(alias="tag", default=None)
    sha: Optional[str] = Field(alias="sha", default=None)
    build_command: Optional[str] = Field(alias="build_command", default=None)
    run_command: Optional[str] = Field(alias="run_command", default=None)
    no_deploy_on_push: Optional[bool] = Field(alias="no_deploy_on_push", default=None)
    workdir: Optional[str] = Field(alias="workdir", default=None)
    buildpack: Optional[BuildpackBuilder] = Field(alias="buildpack", default=None)
    docker: Optional[DockerBuilder] = Field(alias="docker", default=None)
