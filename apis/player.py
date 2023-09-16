from fastapi import FastAPI, Request, Body
from starlette.responses import JSONResponse
import json

from utils.db import (
    get_db,
)
from utils.error import print_error
from controllers.player import update_leaderboard, get_leaderboard

leaderboard_app = FastAPI()


@leaderboard_app.get("/scores")
async def get_data(request: Request):
    try:
        # Only accept get requests
        if request.method == "GET":
            db = get_db(request)
            leaderboard = get_leaderboard(db)
            return {
                    "result": True,
                    "data": leaderboard,
                }
    except Exception as e:
        print_error("Get scores", e)
        raise Exception("Error trying to get leaderboard")

@leaderboard_app.post("/scores")
async def post_data(request: Request, body=Body(..., media_type="application/json")):
    try:
        # Only accept post requests
        if request.method == "POST":
            db = get_db(request)
            update_leaderboard(db, json.loads(body))
            
            return JSONResponse(
                {
                    "result": True,
                }
            )
    except Exception as e:
        print_error("Post scores", e)
        raise Exception("Error trying to update leaderboard")