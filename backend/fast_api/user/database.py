# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/airline"

class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    def get_engine(self):
        return self.engine
    
    def get_session(self):
        return self.session
    
    def get_db(self):
        db = self.session()
        try:
            yield db
        finally:
            db.close()  


