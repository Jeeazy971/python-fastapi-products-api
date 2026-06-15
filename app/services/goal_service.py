from fastapi import HTTPException

goals = []


def get_goals():
    return goals


def get_goal(goal_id: int):
    for goal in goals:
        if goal['id'] == goal_id:
            return goal

    raise HTTPException(status_code=404, detail="Goal not found")


def create_goal(goal):
    new_goal = {
        "id": len(goals) + 1,
        "title": goal.title,
        "category": goal.category,
        "is_completed": False
    }

    goals.append(new_goal)

    return new_goal


def update_goal(goal_id: int, updated_goal):

    for goal in goals:
        if goal['id'] == goal_id:
            goal['title'] = updated_goal.title
            goal['category'] = updated_goal.category

            return goal

    raise HTTPException(status_code=404, detail="Goal not found")


def delete_goal(goal_id: int):
    for goal in goals:
        if goal['id'] == goal_id:
            goals.remove(goal)

            return {
                "message": "Goal deleted",
                "goal_id": goal_id
            }

    raise HTTPException(status_code=404, detail="Goal not found")
