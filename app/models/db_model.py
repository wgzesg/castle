from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ARRAY, ForeignKey

Base = declarative_base()

class Strategy(Base):
    __tablename__ = "strategy"
    id = Column(String, primary_key=True)
    creater_id = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False)
    assignemnt = Column(ARRAY(Integer), nullable=False)

class Result(Base):
    __tablename__ = "result"
    id = Column(Integer, primary_key=True)
    strategy1_id = Column(String, ForeignKey("strategy.id"))
    strategy2_id = Column(String, ForeignKey("strategy.id"))
    result = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)

