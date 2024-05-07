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
    from .deployment_neon_postgres_database_info_role import DeploymentNeonPostgresDatabaseInfoRole


class DeploymentNeonPostgresDatabaseInfo(KoyebModel):
    active_time_seconds: Optional[int] = Field(alias="active_time_seconds", default=None)
    compute_time_seconds: Optional[int] = Field(alias="compute_time_seconds", default=None)
    written_data_bytes: Optional[int] = Field(alias="written_data_bytes", default=None)
    data_transfer_bytes: Optional[int] = Field(alias="data_transfer_bytes", default=None)
    data_storage_bytes_hour: Optional[int] = Field(alias="data_storage_bytes_hour", default=None)
    server_host: Optional[str] = Field(alias="server_host", default=None)
    server_port: Optional[int] = Field(alias="server_port", default=None)
    endpoint_state: Optional[str] = Field(alias="endpoint_state", default=None)
    endpoint_last_active: Optional[datetime] = Field(alias="endpoint_last_active", default=None)
    default_branch_id: Optional[str] = Field(alias="default_branch_id", default=None)
    default_branch_name: Optional[str] = Field(alias="default_branch_name", default=None)
    default_branch_state: Optional[str] = Field(alias="default_branch_state", default=None)
    default_branch_logical_size: Optional[int] = Field(
        alias="default_branch_logical_size", default=None
    )
    roles: Optional[list[DeploymentNeonPostgresDatabaseInfoRole]] = Field(
        alias="roles", default=None
    )
