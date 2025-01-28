from pydantic import BaseModel, Field
from datetime import datetime

from pydantic import BaseModel, constr

class PlayersRead(BaseModel):
    id: int
    fullName: str

class Config:
    from_attributes = True
