# pydantic models for the application
from typing import Literal

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: Literal["low", "medium", "high"] = "low"
    status: str = "pending"

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: Literal["low", "medium", "high"] = "low"

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: Literal["low", "medium", "high"] | None = None
    status: str | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: Literal["low", "medium", "high"]
    status: str

class TaskListResponse(BaseModel):
    tasks: list[TaskResponse]