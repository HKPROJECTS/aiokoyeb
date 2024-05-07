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
    from .neon_postgres_database_neon_database import NeonPostgresDatabaseNeonDatabase
    from .neon_postgres_database_neon_role import NeonPostgresDatabaseNeonRole


class NeonPostgresDatabase(KoyebModel):
    pg_version: Optional[int] = Field(alias="pg_version", default=None)
    region: Optional[str] = Field(alias="region", default=None)
    instance_type: Optional[str] = Field(alias="instance_type", default=None)
    roles: Optional[list[NeonPostgresDatabaseNeonRole]] = Field(alias="roles", default=None)
    databases: Optional[list[NeonPostgresDatabaseNeonDatabase]] = Field(
        alias="databases", default=None
    )
