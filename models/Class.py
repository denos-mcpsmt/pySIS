from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from db import Base
from sqlalchemy.orm import relationship
from models.Enrollments import enrollments

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Float)
    class_type = Column(String)
    length = Column(Integer)
    min_students = Column(Integer)
    max_students = Column(Integer)
    date = Column(Date)
    room = Column(String)

    instructor_id = Column(Integer, ForeignKey('instructors.id'))
    instructor = relationship('Instructor', back_populates='classes')
    students = relationship('Student', secondary=enrollments, back_populates='classes')

    def add_student(self, student):
        # Add student to class
        pass

    def remove_student(self, student):
        # Remove student from class
        pass

    def add_to_waitlist(self, student):
        # Add student to waitlist
        pass

    def discount_class(self, percentage):
        # Apply discount to class cost
        self.cost *= (1 - percentage / 100)

    def cancel_class(self):
        # Handle class cancellation logic
        pass
