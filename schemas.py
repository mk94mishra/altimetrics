from pydantic import BaseModel
from datetime import datetime

class ToggleBase(BaseModel):
    name: str
    description: str
    state: bool = False
    environment: str = None
    owner: str = None
    is_active: bool = True

class ToggleCreate(BaseModel):
    name: str
    description: str
    state: bool = False
    environment: str = None
    owner: str = None

class ToggleUpdate(BaseModel):
    state: bool 
    is_active: bool

class Toggle(ToggleBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
