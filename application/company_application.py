from domain.company.company_repository import ICompanyRepository
from domain.company.company import Company
from domain.role.role_repository import IRoleRepository
from api.v1.company.model import CompanyCreateRequest, CompanyAddProviderRequest, CompanyUpdateRequest
from utils.key_generator import KeyGenerator

class CompanyApplication:
    def __init__(self, company_repository: ICompanyRepository, role_repository: IRoleRepository):
        self.company_repository = company_repository
        self.role_repository = role_repository
        
    def auth_company_by_email_password(self, email: str, password: str) -> Company:
        company = self.company_repository.get_company_by_email(email)
        if company is None:
            raise ValueError("Invalid credentials")
        
        if not company.check_password(password):
            raise ValueError("Invalid credentials")
        
        return company
    
    def auth_company_by_keys(self, api_key: str, secret_key: str) -> Company:
        company = self.company_repository.get_company_by_api_key(api_key)
        if company is None:
            raise ValueError("Invalid credentials")
        
        if not company.check_secret_key(secret_key):
            raise ValueError("Invalid credentials")
        
        return company
    
    def get_company_by_email(self, email: str) -> Company:
        company = self.company_repository.get_company_by_email(email)
        if company is None:
            raise ValueError("Company not found")
        
        return company

    def get_companies(self):
        return self.company_repository.get_companies()
    
    def create_company(self, request: CompanyCreateRequest) -> int:
        role = self.role_repository.get_role_by_id(request.role_id)
        if role is None:
            raise ValueError(f"Role with id {request.role_id} not found")
        
        entity_company = Company(
            role_id=request.role_id,
            name=request.name,
            email=request.email,
            phone=request.phone,
            password=request.password
        )
        
        return self.company_repository.create_company(entity_company)
    
    def request_keys(self, company_id: int) -> {str, str}:
        company = self.company_repository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        if company.api_key is not None and company.secret_key is not None:
            raise ValueError("API keys already exist")
        
        api_key, secret_key = KeyGenerator.generate_api_credentials()
        
        company_updated = self.company_repository.update_api_credentials(
            company_id=company_id,
            api_key=api_key,
            secret_key=secret_key
        )
        
        if company_updated is None:
            raise ValueError("Generating keys failed")
        
        return {api_key, secret_key}
    
    def get_company_by_id(self, company_id: int) -> Company:
        company = self.company_repository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        return company
    
    def add_provider_by_company_id(self, request: CompanyAddProviderRequest, company_id: int) -> bool:
        company = self.company_repository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        company.providers = request.providers
        
        company_updated = self.company_repository.add_provider_by_company_id(
            company_id=company_id,
            company=company
        )
        
        if company_updated is None:
            raise ValueError("Add providers failed")
        
    def active_company(self, company_id: int) -> Company:
        company = self.company_repository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        company = self.company_repository.active_company(company_id)
        if company is None:
            raise ValueError("Activating company failed")
        
        return company
    
    def update_company(self, company_id: int, request: CompanyUpdateRequest) -> Company:
        company = self.company_repository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        if request.role_id is not None:
            role = self.role_repository.get_role_by_id(request.role_id)
            if role is None:
                raise ValueError(f"Role with id {request.role_id} not found")
            company.role_id = request.role_id
        
        company.name = request.name or company.name
        company.email = request.email or company.email
        company.phone = request.phone or company.phone
        
        updated_company = self.company_repository.update_company(company)
        if updated_company is None:
            raise ValueError("Updating company failed")
        
        return updated_company
    
    def update_request_keys(self, company_id: int) -> {str, str}:
        company = self.company_repository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        api_key, secret_key = KeyGenerator.generate_api_credentials()
        
        company_updated = self.company_repository.update_api_credentials(
            company_id=company_id,
            api_key=api_key,
            secret_key=secret_key
        )
        
        if company_updated is None:
            raise ValueError("Generating keys failed")
        
        return {api_key, secret_key}
