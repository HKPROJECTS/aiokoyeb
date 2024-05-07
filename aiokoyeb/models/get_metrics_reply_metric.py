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
    from .sample import Sample


class GetMetricsReplyMetric(KoyebModel):
    labels: Optional[dict] = Field(alias="labels", default=None)
    samples: Optional[list[Sample]] = Field(alias="samples", default=None)
