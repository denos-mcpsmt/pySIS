from sqlalchemy import Column, Integer, String, Date, Text, Float, Time
from sqlalchemy.orm import relationship
from db import Base
from db import get_db_session
from models.course_categories import course_category_link



class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    image = Column(String(200))
    courses = relationship('Course', secondary=course_category_link, back_populates='categories')
