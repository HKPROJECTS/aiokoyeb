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
    from .service_list_item import ServiceListItem


class ListServicesReply(KoyebModel):
    services: Optional[list[ServiceListItem]] = Field(alias="services", default=None)
    limit: Optional[int] = Field(alias="limit", default=None)
    offset: Optional[int] = Field(alias="offset", default=None)
    count: Optional[int] = Field(alias="count", default=None)
