from fastapi import APIRouter
from app.models import Problem, Stats

router = APIRouter()

problems = []
stats = []

#problems
@router.get('/problems')
def get_problems():
    return problems

@router.post('/problems')
def add_problem(problem: Problem):
    problems.append(problem)
    return {
        'message': 'Problem added',
        'problem': problem
    }

#Stats
@router.get('/stats')
def get_stats(stat: Stats):
    return stats

