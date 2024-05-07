##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class NeonPostgresDatabaseDeploymentMetadata(KoyebModel):
    reset_role_passwords: Optional[list[str]] = Field(alias="reset_role_passwords", default=None)
