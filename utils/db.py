from fastapi import Request
from typing import Optional
from db.database import SessionLocal

def get_db(request: Optional[Request] = None):
    if request:
        return request.state.db
    else:
        return SessionLocal()