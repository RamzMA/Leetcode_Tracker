from fastapi import FastAPI
from app.routes import router

app = FastAPI(title='Leetcode Tracker')

app.include_router(router)

@app.get('/')
def home():
    return {'message':'Leetcode Tracker API'}

    