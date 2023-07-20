from tkinter import *
from db import get_db_session
from models.Student import Student
from models.Instructor import Instructor
from datetime import datetime

def new_student_submit():
    name = name_entry.get()
    birthday = datetime.strptime(birthday_entry.get(), '%Y-%m-%d')  # parsing date from string
    address = address_entry.get()

    session = get_db_session()
    new_student = Student(name=name, birthday=birthday, address=address)
    session.add(new_student)
    session.commit()
    session.close()

    # Clear the input fields
    name_entry.delete(0, 'end')
    birthday_entry.delete(0, 'end')
    address_entry.delete(0, 'end')


root = Tk()

Label(root, text="Name").grid(row=0)
Label(root, text="Birthday (YYYY-MM-DD)").grid(row=1)
Label(root, text="Address").grid(row=2)

name_entry = Entry(root)
birthday_entry = Entry(root)
address_entry = Entry(root)

name_entry.grid(row=0, column=1)
birthday_entry.grid(row=1, column=1)
address_entry.grid(row=2, column=1)

Button(root, text='Submit', command=new_student_submit).grid(row=3, column=1, sticky=W, pady=4)

root.mainloop()