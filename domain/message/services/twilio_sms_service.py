from domain.message.message_service import IMessageService
from config.settings import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

class TwilioSmsService(IMessageService):
    def __init__(self):
        self.account_sid = settings.TWILIO_ACCOUNT_SID
        self.account_token = settings.TWILIO_ACCOUNT_TOKEN
        self.phone_number = settings.TWILIO_PHONE_NUMBER

    def SendMessage(self) -> bool:
        
        try:
            client = Client(self.account_sid, self.account_token)
            client.messages.create(
                body="Hola desde fast-api",
                from_=self.phone_number,
                to="+573114718653"
            )
            
            print(f"SMS enviado a 3114718653 con Twilio.")
        except TwilioRestException as e:
            print(f"Error al enviar SMS con Twilio: Código {e.code}, Mensaje: {e.msg}, Más detalles: {str(e)}")
            return False
        except Exception as e:
            print(f"Error inesperado al enviar SMS con Twilio: {str(e)}")
            return False
            
        print("Sending SMS via Twilio")
        return True