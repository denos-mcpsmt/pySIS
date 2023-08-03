from sqlalchemy import Table, Column, Integer, ForeignKey
from db import Base

teaching = Table('teaching', Base.metadata,
    Column('instructor_id', Integer, ForeignKey('instructor.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)