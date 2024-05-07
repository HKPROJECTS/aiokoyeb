##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from enum import Enum


class DeploymentStatus(Enum):
    PENDING = "PENDING"
    PROVISIONING = "PROVISIONING"
    SCHEDULED = "SCHEDULED"
    CANCELING = "CANCELING"
    CANCELED = "CANCELED"
    ALLOCATING = "ALLOCATING"
    STARTING = "STARTING"
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    UNHEALTHY = "UNHEALTHY"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERRORING = "ERRORING"
    ERROR = "ERROR"
    STASHED = "STASHED"
