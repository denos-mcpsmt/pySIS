from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from models.Course import Course


class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    email = Column(String(64), unique=True)
    password = Column(String(128))  # For simplicity, we are not hashing password here
    type = Column(String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

class Student(User):
    __tablename__ = 'student'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }

    birthday = Column(Date)
    address = Column(String)

    #enrolled_courses = relationship("Course", secondary="student_course")

    def enroll_in_class(self, course_id, session):


        try:
            # Query the course by its ID
            course_ = session.query(Course).filter(Course.id == course_id).first()

            if not course_:
                return "Class not found"

            # Check if the course is full
            if len(course_.students) >= course_.max_students:
                return "Class is full"

            # Add the class to the student's courses
            self.enrolled_courses.append(course_)

            # Commit the changes
            session.commit()

            return "Enrollment successful"
        except Exception as e:
            session.rollback()
            return f"An error occurred: {e}"
        finally:
            session.close()

class Instructor(User):
    __tablename__ = 'instructor'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'instructor',
    }

