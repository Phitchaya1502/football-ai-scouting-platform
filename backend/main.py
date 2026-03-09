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

@app.get("/")
def root():
    return FileResponse("../frontend/index.html")