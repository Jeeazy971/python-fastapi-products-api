from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from app.routers import goals
from app.core.config import Settings, get_settings

app = FastAPI()

app.include_router(goals.router)

SettingsDep = Annotated[Settings, Depends(get_settings)]


@app.get('/health')
async def health():
    return {"status": "ok"}


@app.get('/config')
async def get_config(settings: SettingsDep):
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "debug": settings.debug,
        "api_version": settings.api_version,
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
