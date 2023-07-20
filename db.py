from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///school.db"

engine = create_engine(DATABASE_URL)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ScopedSession = scoped_session(session_factory)


Base = declarative_base()


def get_db_session():
    engine = create_engine('sqlite:///school.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
