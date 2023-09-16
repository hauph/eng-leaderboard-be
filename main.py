from fastapi import FastAPI, Response, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from db.database import SessionLocal
from utils.error import print_error
from apis.player import leaderboard_app

app = FastAPI()

ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    except Exception as e:
        print_error("Unexpected exception", e)
        response = JSONResponse(
            {
                "result": False,
                "error": e
            },
        )
    finally:
        request.state.db.close()
    return response

app.mount("/api", leaderboard_app)