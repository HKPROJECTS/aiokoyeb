##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class BuildpackBuilder(KoyebModel):
    build_command: Optional[str] = Field(alias="build_command", default=None)
    run_command: Optional[str] = Field(alias="run_command", default=None)
    privileged: Optional[bool] = Field(alias="privileged", default=None)
