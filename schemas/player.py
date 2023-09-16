from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    score: int


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True