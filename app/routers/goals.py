from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated

from app.services.goal_service import GoalService, get_goal_service

GoalServiceDep = Annotated[GoalService, Depends(get_goal_service)]

router = APIRouter(prefix="/goals", tags=["goals"])


class CreateGoal(BaseModel):
    title: str
    category: str


@router.get('')
async def list_goals(service: GoalServiceDep):
    return service.list_goals()


@router.get('/{goal_id}')
async def get_goal(goal_id: int, service: GoalServiceDep):
    return service.get_goal(goal_id)


@router.post('')
async def create_goal(goal: CreateGoal, service: GoalServiceDep):
    return service.create_goal(goal)


@router.put('/{goal_id}')
async def update_goal(goal_id: int, updated_goal: CreateGoal, service: GoalServiceDep):
    return service.update_goal(goal_id, updated_goal)


@router.delete('/{goal_id}')
async def delete_goal(goal_id: int, service: GoalServiceDep):
    return service.delete_goal(goal_id)
