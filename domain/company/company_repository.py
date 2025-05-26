from abc import ABC, abstractmethod
from typing import List
from domain.company.company import Company

class ICompanyRepository(ABC):
    @abstractmethod
    def get_company_by_email(self, email: str) -> Company | None:
       pass
    
    @abstractmethod
    def get_company_by_api_key(self, api_key: str) -> Company | None:
        pass
   
    @abstractmethod
    def get_companies(self) -> List[Company]:
        pass
    
    @abstractmethod
    def create_company(self, company: Company) -> Company: 
        pass
    
    @abstractmethod
    def get_company_by_id(self, company_id: int) -> Company | None:
        pass
    
    @abstractmethod
    def update_api_credentials(self, company_id: int, api_key: str, secret_key: str) -> Company | None:
        pass
    
    @abstractmethod
    def add_provider_by_company_id(self, company_id: int, company: Company) -> Company | None:
        pass
    
    @abstractmethod
    def active_company(self, company_id: int) -> Company | None:
        pass
    
    def update_company(self, company: Company) -> Company | None:
        pass