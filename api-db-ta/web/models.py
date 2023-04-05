#models.py

from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



Base = declarative_base()


class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    binance_key = Column(String, unique=True, index=True)
    binance_secret = Column(String, unique=True, index=True)
    __table_args__ = (UniqueConstraint("binance_key"), UniqueConstraint("binance_secret"),)
