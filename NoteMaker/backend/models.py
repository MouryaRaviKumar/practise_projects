
from datetime import datetime

from pydantic import BaseModel, Field


class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)  

class createNote(BaseModel):
    title: str
    content: str

class updateNote(BaseModel):
    title: str | None = None
    content: str | None = None

class noteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

class noteListResponse(BaseModel):
    notes: list[noteResponse]
 
