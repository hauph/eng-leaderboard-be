from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from db.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, index=True, nullable=False)
    uploader = Column(String, index=True, nullable=False)
    score = Column(Integer, default=0, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    def __repr__(self) -> str:
        return f"Player(id={self.id}, name={self.name}, uploader={self.uploader}, score={self.score}, created_at={self.created_at}"
