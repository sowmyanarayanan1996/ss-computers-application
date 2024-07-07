from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base



conn = "postgresql://postgres:password@postgresdb:5432/postgres"

postgres_engine = create_engine(conn)


postgres_session_local = sessionmaker(bind=postgres_engine,autocommit=False, autoflush=False)


Base = declarative_base()

AutomapBase = automap_base()


def get_db():
    db=postgres_session_local()
    try:
        yield  db
    finally:
        db.close()
