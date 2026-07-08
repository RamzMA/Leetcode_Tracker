from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String,unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Problem(Base):
    __tablename__ = 'problems'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    difficulty = Column(String)
    status = Column(String)
    topic = Column(String)
