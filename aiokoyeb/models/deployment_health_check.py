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
    from .h_t_t_p_health_check import HTTPHealthCheck
    from .t_c_p_health_check import TCPHealthCheck


class DeploymentHealthCheck(KoyebModel):
    grace_period: Optional[int] = Field(alias="grace_period", default=None)
    interval: Optional[int] = Field(alias="interval", default=None)
    restart_limit: Optional[int] = Field(alias="restart_limit", default=None)
    timeout: Optional[int] = Field(alias="timeout", default=None)
    tcp: Optional[TCPHealthCheck] = Field(alias="tcp", default=None)
    http: Optional[HTTPHealthCheck] = Field(alias="http", default=None)
