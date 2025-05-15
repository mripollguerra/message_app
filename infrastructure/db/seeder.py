import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import datetime
from session import SessionLocal
from infrastructure.models.role import Role
from infrastructure.models.company import Company

def seed():
    session = SessionLocal()

    # Opcional: evitar duplicados
    if session.query(Role).count() == 0:
        roles = [
            Role(name="Super Administrator", created_at=datetime.datetime.utcnow()),
            Role(name="Administrator", created_at=datetime.datetime.utcnow()),
            Role(name="User", created_at=datetime.datetime.utcnow()),
        ]
        session.add_all(roles)
        print("Se insertaron roles.")

    session.commit()
    session.close()

if __name__ == "__main__":
    seed()
