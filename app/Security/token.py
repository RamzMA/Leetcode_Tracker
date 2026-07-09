import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = 'temp-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl = 'login'
)

def create_access_token(data: dict) -> str:
    payload = data.copy()

    expire = data.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload.update({
        'exp': expire
    })

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithm= [ALGORITHM]
        )

        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail='Invalid or expired token'
        )

