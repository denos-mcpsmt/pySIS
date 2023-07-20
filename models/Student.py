from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db import Base
from models.Enrollments import enrollments
from db import get_db_session
from models.Class import Class

class Student(Base):

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)
    enrolled_course = Column(String)
    address = Column(String)

    classes = relationship('Class', secondary=enrollments, back_populates='students')

    def enroll_in_class(self, class_id, session):


        try:
            # Query the class by its ID
            class_ = session.query(Class).filter(Class.id == class_id).first()

            if not class_:
                return "Class not found"

            # Check if the class is full
            if len(class_.students) >= class_.max_students:
                return "Class is full"

            # Add the class to the student's classes
            self.classes.append(class_)

            # Commit the changes
            session.commit()

            return "Enrollment successful"
        except Exception as e:
            session.rollback()
            return f"An error occurred: {e}"
        finally:
            session.close()

    def enroll(self, cls):
        # Check class availability and add to student's class list
        pass

    def view_class_availability(self):
        # Query database for classes with open slots
        pass

    def drop_class(self, cls):
        # Remove class from student's list
        pass

    def edit_info(self, **kwargs):
        # Update student's info
        pass

    def answer_medical_questions(self):
        # Handle medical question logic
        pass

    def add_to_waitlist(self, cls):
        # Add class to student's waitlist
        pass


    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age}, enrolled_course={self.enrolled_course})"

