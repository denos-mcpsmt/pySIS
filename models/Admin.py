from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Admin(Base):
    __tablename__ = 'administrators'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def create_class(self, name, cost, class_type, length, min_students, max_students, date, room):
        # Create new class and add to database
        pass

    def edit_class(self, cls):
        # Edit class information
        pass

    def delete_class(self, cls):
        # Delete class from database
        pass

    def enroll_student(self, student, cls):
        # Enroll student in class
        pass

    def register_student(self, name, birthday, address):
        # Create new student and add to database
        pass

    def issue_refund(self, student, amount):
        # Issue refund to student
        pass