from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db import Base
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user



class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    password = Column(String(128))  # For simplicity, we are not hashing password here
