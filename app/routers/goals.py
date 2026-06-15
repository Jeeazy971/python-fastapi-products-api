from fastapi import APIRouter
from pydantic import BaseModel

from app.services import goal_service


router = APIRouter(prefix="/goals", tags=["goals"])


class CreateGoal(BaseModel):
    title: str
    category: str


@router.get('')
async def list_goals():
    return goal_service.get_goals()


@router.get('/{goal_id}')
async def get_goal(goal_id: int):
    return goal_service.get_goal(goal_id)


@router.post('')
async def create_goal(goal: CreateGoal):
    return goal_service.create_goal(goal)


@router.put('/{goal_id}')
async def update_goal(goal_id: int, updated_goal: CreateGoal):
    return goal_service.update_goal(goal_id, updated_goal)


@router.delete('/{goal_id}')
async def delete_goal(goal_id: int):
    return goal_service.delete_goal(goal_id)
