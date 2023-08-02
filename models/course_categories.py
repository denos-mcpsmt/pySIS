from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

course_category_link = Table('course_category_link', Base.metadata,
                             Column('course_id', Integer, ForeignKey('courses.id')),
                             Column('category_id', Integer, ForeignKey('categories.id')))

