from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    zip_code = Column(String(10), nullable=True)
    description = Column(Text, nullable=True)

    # Relationships
    courses = relationship('Course', backref='location', lazy=True)

    def __repr__(self):
        return f'<Location {self.name}>'
