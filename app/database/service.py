from sqlalchemy.orm import sessionmaker, DeclarativeBase
from database.constants import DATABASE_URL
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL, echo=True)
db_session = sessionmaker(bind=engine)
Base = DeclarativeBase()


def get_database():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
