from domain.company.company_repository import ICompanyRepository
from domain.company.company import Company
from domain.role.role_repository import IRoleRepository
from api.v1.company.model import CompanyCreateRequest
from utils.key_generator import KeyGenerator

class CompanyApplication:
    def __init__(self, companyRepository: ICompanyRepository, roleRepository: IRoleRepository):
        self.companyRepository = companyRepository
        self.roleRepository = roleRepository
        
    def auth_company_by_email_password(self, email: str, password: str) -> Company:
        company = self.companyRepository.get_company_by_email(email)
        if company is None:
            raise ValueError("Invalid credentials")
        
        if not company.check_password(password):
            raise ValueError("Invalid credentials")
        
        return company
    
    def auth_company_by_keys(self, api_key: str, secret_key: str) -> Company:
        company = self.companyRepository.get_company_by_api_key(api_key)
        if company is None:
            raise ValueError("Invalid credentials")
        
        if not company.check_secret_key(secret_key):
            raise ValueError("Invalid credentials")
        
        return company
    
    def get_company_by_email(self, email: str) -> Company:
        company = self.companyRepository.get_company_by_email(email)
        if company is None:
            raise ValueError("Company not found")
        
        return company

    def get_companies(self):
        return self.companyRepository.get_companies()
    
    def create_company(self, request: CompanyCreateRequest) -> int:
        role = self.roleRepository.get_role_by_id(request.role_id)
        if role is None:
            raise ValueError(f"Role with id {request.role_id} not found")
        
        entity_company = Company(
            role_id=request.role_id,
            name=request.name,
            email=request.email,
            phone=request.phone,
            password=request.password
        )
        
        return self.companyRepository.create_company(entity_company)
    
    def request_keys(self, company_id: int) -> {str, str}:
        company = self.companyRepository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        if company.api_key is not None and company.secret_key is not None:
            raise ValueError("API keys already exist")
        
        api_key, secret_key = KeyGenerator.generate_api_credentials()
        
        company_updated = self.companyRepository.update_api_credentials(
            company_id=company_id,
            api_key=api_key,
            secret_key=secret_key
        )
        
        if company_updated is None:
            raise ValueError("Generating keys failed")
        
        return {api_key, secret_key}
    
    def get_company_by_id(self, company_id: int) -> Company:
        company = self.companyRepository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        return company
