from sqlalchemy.orm import Session
from typing import List
from models import Player
from utils.error import print_error

def update_leaderboard(db: Session, body: List[Player]):
    try:
        # Truncate the 'Player' table
        db.query(Player).delete()
        
        # Insert the new scores
        for player in body:
            db.add(Player(**player))

        # Commit the transaction
        db.commit()
    except Exception as e:
        print_error("Update leaderboard", e)
        # Handle any exceptions if necessary
        db.rollback()
        raise Exception("Error trying to update leaderboard")
    finally:
        # Close the session
        db.close()

def get_leaderboard(db: Session):
    try:
        leaderboard = db.query(Player).all()
        return leaderboard
    except Exception as e:
        print_error("Get leaderboard", e)
        # Handle any exceptions if necessary
        raise Exception("Error trying to get leaderboard")
    finally:
        # Close the session
        db.close()
