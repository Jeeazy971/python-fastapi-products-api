from pydantic import BaseModel


class GoalCreate(BaseModel):
    title: str
    category: str


class GoalUpdate(BaseModel):
    title: str
    category: str


class GoalResponse(BaseModel):
    id: int
    title: str
    category: str
    is_completed: bool


class GoalDeleteResponse(BaseModel):
    message: str
    goal_id: int
