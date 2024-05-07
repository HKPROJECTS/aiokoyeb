##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from enum import Enum


class VerifyDockerImageReplyErrCode(Enum):
    UNKNOWN = "UNKNOWN"
    AUTH_ACCESS_DENIED = "AUTH_ACCESS_DENIED"
    ANON_ACCESS_DENIED = "ANON_ACCESS_DENIED"
    AUTH_NOT_FOUND = "AUTH_NOT_FOUND"
    ANON_NOT_FOUND = "ANON_NOT_FOUND"
    REGISTRY_ERROR = "REGISTRY_ERROR"
    TIMEOUT = "TIMEOUT"
    DNS = "DNS"
    MALFORMED = "MALFORMED"
    INVALID_OS = "INVALID_OS"
    INVALID_ARCH = "INVALID_ARCH"
