from domain.company.company_repository import ICompanyRepository
from infrastructure.models.company import Company
from infrastructure.db.session import SessionLocal
from fastapi.encoders import jsonable_encoder
from domain.company.company import Company as CompanyDomain
from typing import List

class CompanyRepository(ICompanyRepository):
    def __init__(self):
        self.session = SessionLocal()
        
    def get_company_by_email(self, email: str) -> CompanyDomain | None:
        company = self.session.query(Company).filter(
            (Company.email == email) & (Company.is_active == True)
        ).first()
        
        if company is None:
            return None
        
        return company.to_domain()
    
    def get_company_by_id(self, company_id: str) -> CompanyDomain | None:
        company = self.session.query(Company).filter(Company.id == company_id).first()
        if company is None:
            return None
        
        return company.to_domain()
    
    def get_companies(self) -> List[CompanyDomain]:
        companies = self.session.query(Company).all()
        
        return [
            company.to_domain()
            for company in companies
        ]
        
    def create_company(self, company: CompanyDomain) -> int:
        entity_company = Company(
            role_id=company.role_id,
            name=company.name,
            email=company.email,
            phone=company.phone,
            password=company.password,
            is_active=company.is_active
        )

        self.session.add(entity_company)
        self.session.commit()
        self.session.refresh(entity_company)
        
        return entity_company.id
    
    def update_api_credentials(self, company_id: int, api_key: str, secret_key: str) -> CompanyDomain | None:
        company = self.session.query(Company).filter(Company.id == company_id and Company.is_active == True).first()

        if not company:
            raise None

        company.api_key = api_key
        company.secret_key = secret_key

        self.session.commit()
        self.session.refresh(company)

        return company.to_domain()
    
    def get_company_by_api_key(self, api_key: str) -> CompanyDomain | None:
        company = self.session.query(Company).filter(
            (Company.api_key == api_key) & (Company.is_active == True)
        ).first()
        
        if company is None:
            return None
        
        return company.to_domain()
    
    def add_provider_by_company_id(self, company_id: int, company: CompanyDomain) -> CompanyDomain | None:
        companyModel = self.session.query(Company).filter(Company.id == company_id and Company.is_active == True).first()

        if not companyModel:
            raise None

        companyModel.providers = jsonable_encoder(company.providers)

        self.session.commit()
        self.session.refresh(companyModel)
        
        return companyModel.to_domain()
    
    def active_company(self, company_id: int) -> CompanyDomain | None:
        company = self.session.query(Company).filter(Company.id == company_id).first()

        if not company:
            raise None

        company.is_active = not company.is_active

        self.session.commit()
        self.session.refresh(company)

        return company.to_domain()
    
    def update_company(self, company: CompanyDomain) -> CompanyDomain | None:
        companyModel = self.session.query(Company).filter(Company.id == company.id).first()
        if not companyModel:
            raise None
        
        companyModel.name = company.name
        companyModel.email = company.email
        companyModel.phone = company.phone
        companyModel.role_id = company.role_id
        
        self.session.commit()
        self.session.refresh(companyModel)
        
        return companyModel.to_domain()