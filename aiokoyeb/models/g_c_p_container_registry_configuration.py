##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class GCPContainerRegistryConfiguration(KoyebModel):
    keyfile_content: Optional[str] = Field(alias="keyfile_content", default=None)
    url: Optional[str] = Field(alias="url", default=None)
