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
    from .service_usage import ServiceUsage


class AppUsage(KoyebModel):
    app_id: Optional[str] = Field(alias="app_id", default=None)
    app_name: Optional[str] = Field(alias="app_name", default=None)
    services: Optional[list[ServiceUsage]] = Field(alias="services", default=None)
