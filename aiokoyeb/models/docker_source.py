##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import KoyebModel


class DockerSource(KoyebModel):
    image: Optional[str] = Field(alias="image", default=None)
    command: Optional[str] = Field(alias="command", default=None)
    args: Optional[list[str]] = Field(alias="args", default=None)
    image_registry_secret: Optional[str] = Field(alias="image_registry_secret", default=None)
    entrypoint: Optional[list[str]] = Field(alias="entrypoint", default=None)
    privileged: Optional[bool] = Field(alias="privileged", default=None)
