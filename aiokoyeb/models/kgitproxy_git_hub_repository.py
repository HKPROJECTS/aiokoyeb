##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class KgitproxyGitHubRepository(KoyebModel):
    github_id: Optional[str] = Field(alias="github_id", default=None)
