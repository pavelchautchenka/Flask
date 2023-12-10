from sqlalchemy import Column, Integer, String, VARCHAR, Text, select, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import uuid
from datetime import datetime

dsn = "sqlite:///hometsk19.db"
engine = create_engine(dsn, echo=True)
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(VARCHAR(100))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now())


def create_table():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)







