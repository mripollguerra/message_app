from dependency_injector import containers, providers
from infrastructure.repositories.company_repository import CompanyRepository
from infrastructure.repositories.role_repository import RoleRepository
from application.company_application import CompanyApplication

class Container(containers.DeclarativeContainer):
    company_service = providers.Factory(
        CompanyApplication,
        companyRepository=providers.Factory(CompanyRepository),
        roleRepository=providers.Factory(RoleRepository)
    )
