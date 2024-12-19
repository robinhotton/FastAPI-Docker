from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Configurer SQLAlchemy
DATABASE_URL = "mysql+pymysql://user:password@db:3306/mydatabase"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()