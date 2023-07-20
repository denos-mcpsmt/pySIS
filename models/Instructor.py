from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from db import Base




class Instructor(Base):
    __tablename__ = 'instructors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)
    tenure = Column(Float)
    class_type = Column(String)

    classes = relationship('Class', back_populates='instructor')

    def propose_class(self, name, cost, class_type, length, min_students, max_students, date, room):
        # Create new class proposal
        pass

    def view_classes(self):
        # Return list of instructor's classes
        return self.classes

    def view_schedule(self):
        # Query database for classes and return schedule
        pass

    def request_substitute(self):
        # Request substitute for a class
        pass