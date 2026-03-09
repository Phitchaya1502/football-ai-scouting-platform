from pydantic import BaseModel

class PlayerCreate(BaseModel):

    name: str
    position: str
    goals: int
    assists: int
    passes: int
    rating: float