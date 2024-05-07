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
    from .auto_release_group import AutoReleaseGroup


class AutoRelease(KoyebModel):
    groups: Optional[list[AutoReleaseGroup]] = Field(alias="groups", default=None)
