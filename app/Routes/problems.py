from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.Security.dependencies import get_current_user
from app.Models.models import Problem, User
from app.database import get_db
from app.Schemas.schemas import ProblemCreate

routerProblems = APIRouter(
    prefix='',
    tags=['Problems']
)

#----------------------------------------        Problems        ----------------------------------------
@routerProblems.get('/problems')
def get_problems(current_user: User = Depends(get_current_user) ,db: Session = Depends(get_db)):
    return db.query(Problem).all()

@routerProblems.post('/problems')
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
