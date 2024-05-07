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
    from .kgitproxy_github_installation_status import KgitproxyGithubInstallationStatus
    from .kgitproxy_indexing_status import KgitproxyIndexingStatus


class GetGithubInstallationReply(KoyebModel):
    installation_id: Optional[str] = Field(alias="installation_id", default=None)
    installation_url: Optional[str] = Field(alias="installation_url", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    avatar_url: Optional[str] = Field(alias="avatar_url", default=None)
    status: Optional[KgitproxyGithubInstallationStatus] = Field(alias="status", default=None)
    installed_at: Optional[datetime] = Field(alias="installed_at", default=None)
    suspended_at: Optional[datetime] = Field(alias="suspended_at", default=None)
    indexing_status: Optional[KgitproxyIndexingStatus] = Field(
        alias="indexing_status", default=None
    )
    indexed_repositories: Optional[int] = Field(alias="indexed_repositories", default=None)
    total_repositories: Optional[int] = Field(alias="total_repositories", default=None)
