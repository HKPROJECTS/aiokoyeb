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
    from .apps_summary import AppsSummary
    from .domains_summary import DomainsSummary
    from .instances_summary import InstancesSummary
    from .members_summary import MembersSummary
    from .neon_postgres_summary import NeonPostgresSummary
    from .secrets_summary import SecretsSummary


class OrganizationSummary(KoyebModel):
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    instances: Optional[InstancesSummary] = Field(alias="instances", default=None)
    apps: Optional[AppsSummary] = Field(alias="apps", default=None)
    services: Optional[dict] = Field(alias="services", default=None)
    domains: Optional[DomainsSummary] = Field(alias="domains", default=None)
    secrets: Optional[SecretsSummary] = Field(alias="secrets", default=None)
    neon_postgres: Optional[NeonPostgresSummary] = Field(alias="neon_postgres", default=None)
    members: Optional[MembersSummary] = Field(alias="members", default=None)
