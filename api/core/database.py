from infrastructure.db.base import Base
from infrastructure.db.session import engine

def init_db():
    Base.metadata.create_all(bind=engine)