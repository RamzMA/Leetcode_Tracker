from fastapi import FastAPI
from app.database import engine, Base
from app.Routes.problems import routerProblems
from app.Routes.auth import routerAuth
from app.Routes.userProblems import routerUserProblems

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
        },
        {
            'name': 'user Problems:',
            'description': 'Users leetcodes'
        }
    ]
)

app.include_router(routerProblems)
app.include_router(routerAuth)
app.include_router(routerUserProblems)

@app.get('/', tags=['Home'])
def home():
    return {'message':'Leetcode Tracker API'}

    