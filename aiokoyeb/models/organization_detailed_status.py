##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from enum import Enum


class OrganizationDetailedStatus(Enum):
    NEW = "NEW"
    EMAIL_NOT_VALIDATED = "EMAIL_NOT_VALIDATED"
    BILLING_INFO_MISSING = "BILLING_INFO_MISSING"
    LOCKED = "LOCKED"
    PAYMENT_FAILURE = "PAYMENT_FAILURE"
    VALID = "VALID"
    PENDING_VERIFICATION = "PENDING_VERIFICATION"
    VERIFICATION_FAILED = "VERIFICATION_FAILED"
    REVIEWING_ACCOUNT = "REVIEWING_ACCOUNT"
    PLAN_UPGRADE_REQUIRED = "PLAN_UPGRADE_REQUIRED"
