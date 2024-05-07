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
    from .deployment_neon_postgres_database_info import DeploymentNeonPostgresDatabaseInfo


class DeploymentDatabaseInfo(KoyebModel):
    neon_postgres: Optional[DeploymentNeonPostgresDatabaseInfo] = Field(
        alias="neon_postgres", default=None
    )
