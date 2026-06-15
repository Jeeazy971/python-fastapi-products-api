from fastapi import HTTPException


class GoalService:

    def __init__(self):
        self.goals = []

    def list_goals(self):
        return self.goals

    def get_goal(self, goal_id: int):
        for goal in self.goals:
            if goal['id'] == goal_id:
                return goal

        raise HTTPException(status_code=404, detail="Goal not found")

    def create_goal(self, goal):
        new_goal = {
            "id": len(self.goals) + 1,
            "title": goal.title,
            "category": goal.category,
            "is_completed": False
        }
        self.goals.append(new_goal)

        return new_goal

    def update_goal(self, goal_id: int, updated_goal):

        for goal in self.goals:
            if goal['id'] == goal_id:
                goal['title'] = updated_goal.title
                goal['category'] = updated_goal.category

                return goal

        raise HTTPException(status_code=404, detail="Goal not found")

    def delete_goal(self, goal_id: int):
        for goal in self.goals:
            if goal['id'] == goal_id:
                self.goals.remove(goal)

                return {
                    "message": "Goal deleted",
                    "goal_id": goal_id
                }

        raise HTTPException(status_code=404, detail="Goal not found")


goal_service = GoalService()


def get_goal_service() -> GoalService:
    return goal_service
