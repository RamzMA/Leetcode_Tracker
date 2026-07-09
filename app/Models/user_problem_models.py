from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    Boolean,
    DateTime
)

from app.database import Base

class UserProblem(Base):
    __tablename__ = 'user_problems'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable=False)
    status = Column(String, default="Not Started")
    notes = Column(Text)
    attempts = Column(Integer, default=0)
    first_attempted_at = Column(DateTime)
    solved_at = Column(DateTime)
    time_spent_minutes = Column(Integer, default=0)
    rating = Column(Integer)  # user rating 
    favorite = Column(Boolean, default=False)

    problem = relationship("Problem", back_populates="user_problem")
