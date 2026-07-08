from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router
from app.auth import routerAuth

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Leetcode Tracker')

app.include_router(router)
app.include_router(routerAuth)

@app.get('/')
def home():
    return {'message':'Leetcode Tracker API'}

    