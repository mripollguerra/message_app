import secrets
import string

class KeyGenerator:
    @staticmethod
    def generate_key(length=32) -> str:
        """Genera una clave aleatoria segura."""
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    @staticmethod
    def generate_api_credentials():
        """Genera un par (api_key, secret_key)."""
        api_key = KeyGenerator.generate_key(32)
        secret_key = KeyGenerator.generate_key(64)
        return api_key, secret_key
