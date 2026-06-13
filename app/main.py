from fastapi import FastAPI
from pydantic import BaseModel

from app.routers import goals

app = FastAPI()

app.include_router(goals.router)


@app.get('/health')
async def health():
    return {"status": "ok"}


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
