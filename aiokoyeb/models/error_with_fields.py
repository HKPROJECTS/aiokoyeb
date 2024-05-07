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
    from .error_field import ErrorField


class ErrorWithFields(KoyebModel):
    status: Optional[int] = Field(alias="status", default=None)
    code: Optional[str] = Field(alias="code", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    fields: Optional[list[ErrorField]] = Field(alias="fields", default=None)
