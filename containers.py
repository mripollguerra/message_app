from dependency_injector import containers, providers
from infrastructure.repositories.company_repository import CompanyRepository
from infrastructure.repositories.role_repository import RoleRepository
from application.company_application import CompanyApplication
from application.message_application import MessageApplication
from domain.message.factory import MessageServiceFactory

class Container(containers.DeclarativeContainer):
    company_service = providers.Factory(
        CompanyApplication,
        company_repository=providers.Factory(CompanyRepository),
        role_repository=providers.Factory(RoleRepository)
    )
    message_application = providers.Factory(
        MessageApplication,
        message_service_factory=providers.Factory(MessageServiceFactory)
    )
