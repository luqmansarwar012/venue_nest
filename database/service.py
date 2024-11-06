from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .constants import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
db_session = sessionmaker(bind=engine)
Base = declarative_base()


def get_database():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
