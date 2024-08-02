from database import Base,engine
from models import Item

print("Crieating database ...")

Base.metadata.create_all(engine)