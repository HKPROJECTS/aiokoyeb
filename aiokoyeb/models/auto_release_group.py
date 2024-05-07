##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class AutoReleaseGroup(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    repository: Optional[str] = Field(alias="repository", default=None)
    git_ref: Optional[str] = Field(alias="git_ref", default=None)
    latest_sha: Optional[str] = Field(alias="latest_sha", default=None)
