from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import urllib.parse


password='bhuviSAHU@12'
encoded_password = urllib.parse.quote_plus(password)
database_url = f'postgresql://postgres:{encoded_password}@localhost:5432/FastAPI App1 '

engine = create_engine(database_url)

session_factory = sessionmaker(bind=engine,autocommit=False,autoflush=False)

def get_db():
    db=session_factory()
    try:
        yield db
    finally:
        db.close()