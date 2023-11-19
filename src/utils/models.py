from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime  

Base = declarative_base()

class DepositLog(Base):
    __tablename__ = "deposit_log"

    id = Column(Integer, primary_key=True, index=True)
    deposit_type = Column(String)
    over = Column(Float, nullable=True) 
    under = Column(Float, nullable=True) 
    term = Column(Float, nullable=True)
    currency = Column(String, nullable=True) 
    interest = Column(Float)
    bank = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow) 