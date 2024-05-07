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
    from .kgitproxy_git_hub_repository import KgitproxyGitHubRepository
    from .kgitproxy_repository_provider import KgitproxyRepositoryProvider


class KgitproxyRepository(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    url: Optional[str] = Field(alias="url", default=None)
    description: Optional[str] = Field(alias="description", default=None)
    is_private: Optional[bool] = Field(alias="is_private", default=None)
    is_disabled: Optional[bool] = Field(alias="is_disabled", default=None)
    default_branch: Optional[str] = Field(alias="default_branch", default=None)
    provider: Optional[KgitproxyRepositoryProvider] = Field(alias="provider", default=None)
    last_push_date: Optional[datetime] = Field(alias="last_push_date", default=None)
    github: Optional[KgitproxyGitHubRepository] = Field(alias="github", default=None)
