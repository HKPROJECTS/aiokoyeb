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
    from .deployment_event import DeploymentEvent


class ListDeploymentEventsReply(KoyebModel):
    events: Optional[list[DeploymentEvent]] = Field(alias="events", default=None)
    limit: Optional[int] = Field(alias="limit", default=None)
    offset: Optional[int] = Field(alias="offset", default=None)
    order: Optional[str] = Field(alias="order", default=None)
