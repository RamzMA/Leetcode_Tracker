from fastapi import FastAPI
from app.database import engine, Base
from app.Routes.problems import routerProblems
from app.Routes.auth import routerAuth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Leetcode Tracker',
    openapi_tags=[
        {
            'name': 'Home',
            'description': 'General Endpoints'
        },
        {
            'name': 'Auth',
            'description': 'Authentification'
        },
        {
            'name': 'Problems',
            'description': 'Leetcode Problems'
        }
    ]
)

app.include_router(routerProblems)
app.include_router(routerAuth)

@app.get('/', tags=['Home'])
def home():
    return {'message':'Leetcode Tracker API'}

    