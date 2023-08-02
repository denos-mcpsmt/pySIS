from sqlalchemy import Column, Integer, String, Date, Text, Float, Time
from sqlalchemy.orm import relationship
from db import Base
from db import get_db_session
from models.course_categories import course_category_link

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    image = Column(String(200))
    min_students = Column(Integer)
    max_students = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    categories = relationship('Category', secondary=course_category_link, back_populates='courses')
    #TO-DO: Validate date and times