import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import datetime
from session import SessionLocal
from infrastructure.models.role import Role
from infrastructure.models.company import Company

def seed():
    session = SessionLocal()

    if session.query(Role).count() == 0:
        roles = [
            Role(name="Super Administrator", created_at=datetime.datetime.utcnow()),
            Role(name="Administrator", created_at=datetime.datetime.utcnow()),
            Role(name="User", created_at=datetime.datetime.utcnow()),
        ]
        session.add_all(roles)
        print("Se insertaron roles.")
        
    if session.query(Company).count() == 0:
        company = Company(
            name="GML Software",
            password="GmlSoftware123",
            is_active=True,
            email="superadminstrator@gmlsoftware.com",
            phone="3013723158",
            description="This is the default company.",
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            role_id=1
        )
        session.add(company)
        print("Se insertó la compañía por defecto.")
        
    session.commit()
    session.close()

if __name__ == "__main__":
    seed()
