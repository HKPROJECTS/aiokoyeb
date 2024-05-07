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
    from .datacenter_list_item import DatacenterListItem


class ListDatacentersReply(KoyebModel):
    datacenters: Optional[list[DatacenterListItem]] = Field(alias="datacenters", default=None)
