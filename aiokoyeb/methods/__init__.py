##############################################
#         THIS FILE IS AUTO GENERATED        #
#           DO NOT MODIFY THIS FILE          #
#          Author: Md. Hasibul Kabir         #
##############################################


from .activity_method import ActivityMethod
from .apps_method import AppsMethod
from .billing_method import BillingMethod
from .catalog_datacenters_method import CatalogDatacentersMethod
from .catalog_instances_method import CatalogInstancesMethod
from .catalog_regions_method import CatalogRegionsMethod
from .credentials_method import CredentialsMethod
from .deployments_method import DeploymentsMethod
from .docker_helper_method import DockerHelperMethod
from .domains_method import DomainsMethod
from .instances_method import InstancesMethod
from .invite_method import InviteMethod
from .logs_method import LogsMethod
from .metrics_method import MetricsMethod
from .organization_confirmations_method import OrganizationConfirmationsMethod
from .organization_invitations_method import OrganizationInvitationsMethod
from .organization_members_method import OrganizationMembersMethod
from .organization_method import OrganizationMethod
from .organization_quotas_method import OrganizationQuotasMethod
from .payment_methods_method import PaymentMethodsMethod
from .profile_method import ProfileMethod
from .quotas_method import QuotasMethod
from .regional_deployments_method import RegionalDeploymentsMethod
from .repositories_method import RepositoriesMethod
from .search_method import SearchMethod
from .secrets_method import SecretsMethod
from .services_method import ServicesMethod
from .sessions_method import SessionsMethod
from .sso_method import SsoMethod
from .subscriptions_method import SubscriptionsMethod
from .summary_method import SummaryMethod
from .usages_method import UsagesMethod
from .users_method import UsersMethod


class Methods(
    DockerHelperMethod,
    UsagesMethod,
    RegionalDeploymentsMethod,
    ServicesMethod,
    DeploymentsMethod,
    AppsMethod,
    DomainsMethod,
    InstancesMethod,
    QuotasMethod,
    SecretsMethod,
    CatalogRegionsMethod,
    CatalogInstancesMethod,
    CatalogDatacentersMethod,
    SearchMethod,
    ActivityMethod,
    LogsMethod,
    MetricsMethod,
    SubscriptionsMethod,
    PaymentMethodsMethod,
    OrganizationConfirmationsMethod,
    CredentialsMethod,
    UsersMethod,
    OrganizationInvitationsMethod,
    SessionsMethod,
    InviteMethod,
    ProfileMethod,
    BillingMethod,
    OrganizationMethod,
    SsoMethod,
    OrganizationMembersMethod,
    SummaryMethod,
    OrganizationQuotasMethod,
    RepositoriesMethod,
):
    pass
