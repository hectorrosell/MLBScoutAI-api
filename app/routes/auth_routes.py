
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import Player
from app.database import get_db
from app.schemas import PlayersRead
from app.logger import logger
from app.data.dataset import get_players

router = APIRouter()

get_db()

@router.get("/mlb_players", response_model=list[PlayersRead],
    responses={
        200: {"description": "List of mlb_players retrieved successfully"},
        404: {"description": "No mlb_players found"},
        500: {"description": "Internal Server Error: Failed to retrieve mlb_players"}
    })
def list_mlb_players  (
    #skip: int,
    #limit: int = 5,
    #db: Session = Depends(get_db)
        season: int,
        sport: int
):

    #offset = (skip - 1) * limit
    #player_res = db.query(Player).offset(offset).limit(limit).all()

    player_res = get_players (season, sport)
    # Convertir DataFrame a lista de diccionarios

    # Convertir DataFrame a lista de diccionarios

    player_res_list = player_res[['id', 'fullName']].to_dict(orient='records')

    #if not player_res:
    #    raise HTTPException(status_code=404, detail="No mlb_players found")
    return player_res_list
