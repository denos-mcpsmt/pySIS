from sqlalchemy import Table, Column, Integer, ForeignKey
from db import Base

enrollments = Table('enrollments', Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)