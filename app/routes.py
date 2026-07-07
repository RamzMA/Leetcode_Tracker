from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models import Problem
from app.database import get_db
from app.schemas import ProblemCreate

router = APIRouter()

#problems
@router.get('/problems')
def get_problems(db: Session = Depends(get_db)):
    return db.query(Problem).all()

@router.post('/problems')
def create_problem(
    problem: ProblemCreate,
    db: Session = Depends(get_db)
):
    db_problem = Problem(
        title = problem.title,
        difficulty = problem.difficulty,
        status = problem.status,
        topic = problem.topic,
    )

    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)

    return db_problem