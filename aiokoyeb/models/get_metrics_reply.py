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
    from .get_metrics_reply_metric import GetMetricsReplyMetric


class GetMetricsReply(KoyebModel):
    metrics: Optional[list[GetMetricsReplyMetric]] = Field(alias="metrics", default=None)
