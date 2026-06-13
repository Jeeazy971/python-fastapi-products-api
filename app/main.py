from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get('/health')
async def health():
    return {
        "status": "ok"
    }


@app.get('/learning-status')
async def learning_status():
    return {
        "module": "FastAPI",
        "block": 1,
        "status": "in_progress"
    }


@app.get('/lessons/{lesson_id}')
async def lessons(lesson_id: int):
    return {
        "lesson_id": lesson_id,
        "title": "Lesson details"
    }


@app.get('/lessons')
async def list_lessons(topic: str | None = None, limit: int = 10):
    return {
        "topic": topic,
        "limit": limit
    }


class CreateStudySession(BaseModel):
    topic: str
    duration_minutes: int
    difficulty: str


@app.post('/study-sessions')
async def study_sessions(session: CreateStudySession):
    return {
        "message": "Study session created",
        "session": session
    }

goals = []


@app.get('/goals')
async def list_goals():
    return goals


class CreateGoal(BaseModel):
    title: str
    category: str


@app.get('/goals/{goal_id}')
async def get_goal(goal_id: int):
    for goal in goals:
        if goal['id'] == goal_id:
            return goal

    raise HTTPException(status_code=404, detail="Goal not found")


@app.post('/goals')
async def create_goal(goal: CreateGoal):
    new_goal = {
        "id": len(goals) + 1,
        "title": goal.title,
        "category": goal.category,
        "is_completed": False
    }

    goals.append(new_goal)

    return new_goal


@app.put('/goals/{goal_id}')
async def update_goal(goal_id: int, updated_goal: CreateGoal):

    for goal in goals:
        if goal['id'] == goal_id:
            goal['title'] = updated_goal.title
            goal['category'] = updated_goal.category

            return goal

    raise HTTPException(status_code=404, detail="Goal not found")


@app.delete('/goals/{goal_id}')
async def delete_goal(goal_id: int):
    for goal in goals:
        if goal['id'] == goal_id:
            goals.remove(goal)

            return {
                "message": "Goal deleted",
                "goal_id": goal_id
            }

    raise HTTPException(status_code=404, detail="Goal not found")
