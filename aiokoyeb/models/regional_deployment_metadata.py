##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class RegionalDeploymentMetadata(KoyebModel):
    runtime_job_id: Optional[str] = Field(alias="runtime_job_id", default=None)
