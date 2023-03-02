from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class Database():
    def __init__(self, db_url):
        # postgresql://postgres:postgres@localhost:5432
        self.db_engine = create_engine("postgresql://postgres:postgres@localhost:5432", pool_pre_ping=True)
        self.Session = sessionmaker(bind=self.db_engine, autocommit=False, autoflush=False)

    @contextmanager
    def get_db(self):
        print("session creating")
        session = self.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()