from models.Course import Course
from models.Category import Category
from models.course_categories import course_category_link
from db import ScopedSession

def get_courses_by_category(category_id):
    """Returns a list of courses for a given category."""
    session = ScopedSession()
    print("searching for category "+str(category_id))
    return session.query(Course)\
                  .join(course_category_link)\
                  .filter(course_category_link.c.category_id==category_id)\
                  .all()