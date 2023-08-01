from sqlalchemy import Column, Integer, String, Date, Text, Float, Time
from sqlalchemy.orm import relationship
from db import Base
from db import get_db_session

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    image = Column(String(200))
    start_date = Column(Date)
    end_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)

    #TO-DO: Validate date and times