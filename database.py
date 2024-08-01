from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://alysson:senhabanco@localhost/item_db",echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)