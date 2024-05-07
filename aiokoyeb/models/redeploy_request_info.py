##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class RedeployRequestInfo(KoyebModel):
    deployment_group: Optional[str] = Field(alias="deployment_group", default=None)
    sha: Optional[str] = Field(alias="sha", default=None)
    use_cache: Optional[bool] = Field(alias="use_cache", default=None)
    skip_build: Optional[bool] = Field(alias="skip_build", default=None)
