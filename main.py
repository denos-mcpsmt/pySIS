from db import get_db_session, Base
from models.Student import Student
from models.Class import Class
from models.Instructor import Instructor
from datetime import date
from flask import Flask
from db import ScopedSession
from routes import set_up_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xd4\xc5\xf2\xae\xaa\xb7\xc7\xd9}\xf3}\xebHG\xa4\x96'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
#db = SQLAlchemy(app)

@app.before_request
def create_session():
    ScopedSession()


@app.teardown_appcontext
def shutdown_session(response_or_exc):
    ScopedSession.remove()


set_up_routes(app)


def main():
    app = Flask(__name__)
    app.run(debug=True)
   # session = get_db_session()  # get a Session instance

    # create a student, a class, and an instructor
   # student = Student(name='John Doe', birthday=date.today(), address='123 Main St')
   # cls = Class(name='Math 101', max_students=8)
   # instructor = Instructor(name='Jane Doe', birthday=date.today(), tenure=5, class_type='Math')

    # enroll the student in the class and assign the instructor to the class
   # student.classes.append(cls)
   # cls.instructor = instructor

    # add the new student, class, and instructor to the session and commit the session
   # session.add(student)
   # session.add(cls)
   # session.add(instructor)

   # message = student.enroll_in_class(1,session)
   # print(message)


   # session.commit()

    # print all students
   # students = session.query(Student).all()
   # for student in students:
    #    print(f"Student Name: {student.name}, Birthday: {student.birthday}, Address: {student.address}")

    # print all classes
   # classes = session.query(Class).all()
   # for class_ in classes:
    #    print(f"Class Name: {class_.name}, Instructor: {class_.instructor.name}")


if __name__ == '__main__':
    app.run(debug=True)