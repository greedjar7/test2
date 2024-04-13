from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base

class Jobkorea(Base):
    __tablename__ = 'jobkorea'

    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)
    cruit_detail = Column(String, nullable=False)
    tech_detail = Column(String, nullable=False)
    link = Column(String, nullable=False)
    create_time = Column(DateTime, nullable=False)

class Saramin(Base):
    __tablename__ = 'saramin'

    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)
    cruit_detail = Column(String, nullable=False)
    tech_detail = Column(String, nullable=False)
    link = Column(String, nullable=False)
    create_time = Column(DateTime, nullable=False)

class Wanted(Base):
    __tablename__ = 'wanted'

    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)
    cruit_detail = Column(String, nullable=False)
    tech_detail = Column(String, nullable=False)
    link = Column(String, nullable=False)
    create_time = Column(DateTime, nullable=False)