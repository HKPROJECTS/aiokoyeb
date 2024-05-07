##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class DeploymentNeonPostgresDatabaseInfoRole(KoyebModel):
    name: Optional[str] = Field(alias="name", default=None)
    secret_id: Optional[str] = Field(alias="secret_id", default=None)
