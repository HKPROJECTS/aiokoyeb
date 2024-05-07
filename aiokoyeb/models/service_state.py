##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import KoyebModel

if TYPE_CHECKING:
    from .auto_release import AutoRelease
    from .desired_deployment import DesiredDeployment


class ServiceState(KoyebModel):
    desired_deployment: Optional[DesiredDeployment] = Field(
        alias="desired_deployment", default=None
    )
    auto_release: Optional[AutoRelease] = Field(alias="auto_release", default=None)
