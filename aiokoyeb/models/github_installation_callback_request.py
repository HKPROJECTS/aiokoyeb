##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class GithubInstallationCallbackRequest(KoyebModel):
    installation_id: Optional[str] = Field(alias="installation_id", default=None)
    setup_action: Optional[str] = Field(alias="setup_action", default=None)
    state: Optional[str] = Field(alias="state", default=None)
