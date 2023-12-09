from sqlalchemy import Column, Integer, String, VARCHAR, Text, select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


dsn = "sqlite:///hometsk19.db"
engine = create_engine(dsn, echo=True)
session = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(200), unique=True, nullable=False)

    def __str__(self):
        return f"User: {self.username}"


def create_table():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


drop_tables()
create_table()



