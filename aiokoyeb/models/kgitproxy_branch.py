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
    from .kgitproxy_repository_provider import KgitproxyRepositoryProvider


class KgitproxyBranch(KoyebModel):
    id: Optional[str] = Field(alias="id", default=None)
    organization_id: Optional[str] = Field(alias="organization_id", default=None)
    repository_id: Optional[str] = Field(alias="repository_id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    is_default: Optional[bool] = Field(alias="is_default", default=None)
    is_protected: Optional[bool] = Field(alias="is_protected", default=None)
    provider: Optional[KgitproxyRepositoryProvider] = Field(alias="provider", default=None)
