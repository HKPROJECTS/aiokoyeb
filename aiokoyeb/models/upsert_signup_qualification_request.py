##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class UpsertSignupQualificationRequest(KoyebModel):
    signup_qualification: Optional[dict] = Field(alias="signup_qualification", default=None)
