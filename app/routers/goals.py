from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix="/goals", tags=["goals"])

goals = []

class CreateGoal(BaseModel):
    title: str
    category: str


@router.get('')
async def list_goals():
    return goals


@router.get('/{goal_id}')
async def get_goal(goal_id: int):
    for goal in goals:
        if goal['id'] == goal_id:
            return goal

    raise HTTPException(status_code=404, detail="Goal not found")


@router.post('')
async def create_goal(goal: CreateGoal):
    new_goal = {
        "id": len(goals) + 1,
        "title": goal.title,
        "category": goal.category,
        "is_completed": False
    }

    goals.append(new_goal)

    return new_goal


@router.put('/{goal_id}')
async def update_goal(goal_id: int, updated_goal: CreateGoal):

    for goal in goals:
        if goal['id'] == goal_id:
            goal['title'] = updated_goal.title
            goal['category'] = updated_goal.category

            return goal

    raise HTTPException(status_code=404, detail="Goal not found")


@router.delete('/{goal_id}')
async def delete_goal(goal_id: int):
    for goal in goals:
        if goal['id'] == goal_id:
            goals.remove(goal)

            return {
                "message": "Goal deleted",
                "goal_id": goal_id
            }

    raise HTTPException(status_code=404, detail="Goal not found")
