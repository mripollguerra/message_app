from typing import List, Dict, Any
from domain.message.message_factory import MessageFactory
from domain.message.message_provider import MessageProvider
from domain.company.company_repository import ICompanyRepository

class MessageApplication:
    def __init__(self, message_service_factory: MessageFactory, company_repository: ICompanyRepository):
        self.message_service_factory = message_service_factory
        self.company_repository = company_repository

    def send_messages(self, service_types: str, company_id: int) -> List[Dict[str, Any]]:
        company = self.company_repository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        
        if not company.providers:
            raise ValueError("No providers configured for this company")
        
        allowed_providers = [p.service_name.strip().lower() for p in company.providers]
        types_list = [t.strip().lower() for t in (service_types or "").split(",") if t.strip()]
        
        if not types_list:
            types_list = allowed_providers
        
        results = []
        for service_type in types_list:
            if service_type not in allowed_providers:
                results.append({
                    "service_type": service_type,
                    "error": f"Provider '{service_type}' is not allowed for this company"
                })
                continue
        
            service = self.message_service_factory.get_service(service_type)
            if service is None:
                results.append({
                    "service_type": service_type,
                    "error": "Service type not supported"
                })
            else:
                try:
                    success = service.SendMessage()
                    results.append({
                        "service_type": service_type,
                        "success": success
                    })
                except Exception as e:
                    results.append({
                        "service_type": service_type,
                        "error": str(e)
                    })

        return results
    
    def get_providers(self) -> List[MessageProvider]:
        return MessageProvider.get_providers()