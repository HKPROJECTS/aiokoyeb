##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import VerifyDockerImageModel

if TYPE_CHECKING:
    from aiokoyeb import KoyebAPI


class DockerHelperMethod:
    async def verify_docker_image(
        self: KoyebAPI,
        image: str | None = None,
        secret_id: str | None = None,
    ):
        return await self.request(VerifyDockerImageModel(image=image, secret_id=secret_id))
