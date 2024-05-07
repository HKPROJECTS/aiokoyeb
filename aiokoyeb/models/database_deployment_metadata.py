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
    from .neon_postgres_database_deployment_metadata import NeonPostgresDatabaseDeploymentMetadata


class DatabaseDeploymentMetadata(KoyebModel):
    neon_postgres: Optional[NeonPostgresDatabaseDeploymentMetadata] = Field(
        alias="neon_postgres", default=None
    )
