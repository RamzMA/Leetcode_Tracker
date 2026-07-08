from app.encryption import hash_password, verify_password
from fastapi import APIRouter, Depends
from app.models import User
from app.schemas import UserCreate, UserLogin
from sqlalchemy.orm import Session
from app.database import get_db


routerAuth = APIRouter()

@routerAuth.post('/register')
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        email = user.email,
        username = user.username,
        hashed_password = hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        'message': 'User Created'
    }

@routerAuth.post('/login')
def login(
    login_details: UserLogin,
    db : Session = Depends(get_db)
    ):
    user = (
        db.query(User).filter(User.username == login_details.username).first()
    )

    if not user:
        return {'message': 'Invalid Credentials!'}
    
    if not verify_password(login_details.password, user.hashed_password):
        return {'message': 'Invalid Password'}
    
    return {
        'message': 'Login Successful'
    }


    