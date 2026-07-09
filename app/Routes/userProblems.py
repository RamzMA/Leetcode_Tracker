from app.database import get_db
from app.Security.dependencies import get_current_user
from app.database import get_db

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.Schemas.user_problem_schema import UserProblemCreate, UserProblemResponse, UserProblemUpdate
from app.Models.user_problem_models import UserProblem
from app.Models.models import User

routerUserProblems = APIRouter(
    prefix='',
    tags=['User Problems']
)

@routerUserProblems.post('/user-problems')
def add_problem(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    user_problem = UserProblemCreate,
):
    db_problem = UserProblem(
        user_id = current_user.id,
        problem_id = user_problem.problem_id,
        status='Not Started'
    )

    db.add(db_problem)
    db.commit()

    return db_problem
