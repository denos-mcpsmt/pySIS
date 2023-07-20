from sqlalchemy import Table, Column, Integer, ForeignKey
from db import Base

enrollments = Table('enrollments', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('class_id', Integer, ForeignKey('classes.id'))
)