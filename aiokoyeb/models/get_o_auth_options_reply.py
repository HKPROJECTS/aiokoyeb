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
    from .o_auth_provider import OAuthProvider


class GetOAuthOptionsReply(KoyebModel):
    """
    A list of providers which you can use for single sign-on.
    """

    oauth_providers: Optional[list[OAuthProvider]] = Field(alias="oauth_providers", default=None)
