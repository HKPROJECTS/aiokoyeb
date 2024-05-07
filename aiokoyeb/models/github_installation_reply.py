##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class GithubInstallationReply(KoyebModel):
    app_name: Optional[str] = Field(alias="app_name", default=None)
    app_id: Optional[int] = Field(alias="app_id", default=None)
    url: Optional[str] = Field(alias="url", default=None)
    state: Optional[str] = Field(alias="state", default=None)
