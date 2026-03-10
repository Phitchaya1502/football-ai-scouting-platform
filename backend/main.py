from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import models
import crud
import schemas

from database import SessionLocal, engine

from ai_model import analyze_player

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/submit-player")

def submit_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):

    score, rec = analyze_player(

        player.goals,
        player.assists,
        player.passes,
        player.rating

    )

    return crud.create_player(db, player, score, rec)


@app.get("/players")

def read_players(db: Session = Depends(get_db)):

    return crud.get_players(db)

@app.get("/model-info")
def model_info():
    return {
        "goals_weight": 35,
        "assists_weight": 25,
        "passes_weight": 20,
        "rating_weight": 20,
        "accuracy": 92
    }
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/player/{player_id}")
def get_player(player_id: int, db: Session = Depends(get_db)):

    player = db.query(models.Player).filter(models.Player.id == player_id).first()

    if not player:
        return {"error": "Player not found"}

    return player

@app.put("/player/{player_id}")
def update_player(player_id: int, player: schemas.PlayerCreate, db: Session = Depends(get_db)):

    db_player = db.query(models.Player).filter(models.Player.id == player_id).first()

    if not db_player:
        return {"error": "Player not found"}

    db_player.name = player.name
    db_player.position = player.position
    db_player.goals = player.goals
    db_player.assists = player.assists
    db_player.passes = player.passes
    db_player.rating = player.rating

    score, rec = analyze_player(
        player.goals,
        player.assists,
        player.passes,
        player.rating
    )

    db_player.ai_score = score
    db_player.recommendation = rec

    db.commit()
    db.refresh(db_player)

    return db_player

@app.delete("/player/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):

    player = db.query(models.Player).filter(models.Player.id == player_id).first()

    if not player:
        return {"error": "Player not found"}

    db.delete(player)
    db.commit()

    return {"message": "Player deleted"}

@app.get("/")
def root():
    return FileResponse("../frontend/index.html")