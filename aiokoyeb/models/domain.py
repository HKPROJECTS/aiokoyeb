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
    from .domain_status import DomainStatus
    from .domain_type import DomainType


class Domain(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    status: Optional[DomainStatus] = Field(alias="status", default=None)
    type: Optional[DomainType] = Field(alias="type", default=None)
    app_id: Optional[str] = Field(alias="app_id", default=None)
    deployment_group: Optional[str] = Field(alias="deployment_group", default=None)
    verified_at: Optional[datetime] = Field(alias="verified_at", default=None)
    intended_cname: Optional[str] = Field(alias="intended_cname", default=None)
    messages: Optional[list[str]] = Field(alias="messages", default=None)
    version: Optional[int] = Field(alias="version", default=None)
