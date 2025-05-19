from typing import List, Dict, Any
from domain.message.message_factory import MessageFactory
from domain.message_provider.message_provider import MessageProvider
from domain.company.company_repository import ICompanyRepository
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError

class MessageApplication:
    def __init__(self, message_service_factory: MessageFactory, company_repository: ICompanyRepository):
        self.message_service_factory = message_service_factory
        self.company_repository = company_repository

    def send_messages(self, service_types: str, company_id: int, raw_body: Dict[str, Any]) -> List[Dict[str, Any]]:
        company = self._get_company(company_id)
        allowed_providers = self._get_allowed_providers(company)
        type_service_list = self._parse_service_types(service_types, allowed_providers)

        results = []
        for service_type in type_service_list:
            if service_type not in allowed_providers:
                results.append(self._provider_not_allowed_response(service_type))
                continue

            service = self.message_service_factory.get_service(service_type)
            if service is None:
                results.append(self._unsupported_service_response(service_type))
                continue

            try:
                ParamModel = service.get_param_model()
                validated_data = ParamModel(**raw_body)
                success = service.send_message(validated_data)
                results.append({"service_type": service_type, "success": success})
            except Exception as e:
                results.append(self._parameter_error_response(service_type, e))

        return results
    
    def get_providers(self) -> List[MessageProvider]:
        return MessageProvider.get_providers()
    
    def _get_company(self, company_id: int):
        company = self.company_repository.get_company_by_id(company_id)
        if company is None:
            raise ValueError("Company not found")
        return company

    def _get_allowed_providers(self, company) -> List[str]:
        if not company.providers:
            raise ValueError("No providers configured for this company")
        return [p.service_name.strip().lower() for p in company.providers]

    def _parse_service_types(self, service_types: str, allowed_providers: List[str]) -> List[str]:
        types_list = [t.strip().lower() for t in (service_types or "").split(",") if t.strip()]
        return types_list if types_list else allowed_providers

    def _provider_not_allowed_response(self, service_type: str) -> Dict[str, Any]:
        return {
            "service_type": service_type,
            "error": f"Provider '{service_type}' is not allowed for this company"
        }

    def _unsupported_service_response(self, service_type: str) -> Dict[str, Any]:
        return {
            "service_type": service_type,
            "error": "Service type not supported"
        }

    def _parameter_error_response(self, service_type: str, error: Exception) -> Dict[str, Any]:
        if isinstance(error, (ValidationError, RequestValidationError)):
            errors = [
                {
                    "field": str(err["loc"][-1]) if err["loc"] else "",
                    "message": err["msg"]
                }
                for err in error.errors()
            ]
            return {
                "service_type": service_type,
                "error": "Error en parámetros",
                "details": errors
            }

        return {
            "service_type": service_type,
            "error": f"Error inesperado: {str(error)}"
        }