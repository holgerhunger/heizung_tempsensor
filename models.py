from database import Base
from sqlalchemy import  Column, Integer, String, DateTime, Float

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    sensor_code = Column(String)
    time_stamp = Column(DateTime)
    value = Column(Float)
