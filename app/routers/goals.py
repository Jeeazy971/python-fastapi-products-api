from typing import Annotated

from fastapi import APIRouter, Depends

from app.services.goal_service import GoalService, get_goal_service
from app.schemas.goal import GoalCreate, GoalUpdate, GoalResponse, GoalDeleteResponse

GoalServiceDep = Annotated[GoalService, Depends(get_goal_service)]

router = APIRouter(prefix="/goals", tags=["goals"])


@router.get('', response_model=list[GoalResponse])
async def list_goals(service: GoalServiceDep):
    return service.list_goals()


@router.get('/{goal_id}', response_model=GoalResponse)
async def get_goal(goal_id: int, service: GoalServiceDep):
    return service.get_goal(goal_id)


@router.post('', response_model=GoalResponse)
async def create_goal(goal: GoalCreate, service: GoalServiceDep):
    return service.create_goal(goal)


@router.put('/{goal_id}', response_model=GoalResponse)
async def update_goal(goal_id: int, updated_goal: GoalUpdate, service: GoalServiceDep):
    return service.update_goal(goal_id, updated_goal)


@router.delete('/{goal_id}', response_model=GoalDeleteResponse)
async def delete_goal(goal_id: int, service: GoalServiceDep):
    return service.delete_goal(goal_id)
