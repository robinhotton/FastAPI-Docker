from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les variables d'environnement pour la base de données
USER=os.environ["USER"]
PASSWORD=os.environ["PASSWORD"]
DATABASE=os.environ["DATABASE"]
URL = f"mysql+pymysql://{USER}:{PASSWORD}@db:3306/{DATABASE}"
engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()