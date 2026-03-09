from sqlalchemy.orm import Session
import models

def create_player(db: Session, player, score, rec):

    db_player = models.Player(

        name=player.name,
        position=player.position,
        goals=player.goals,
        assists=player.assists,
        passes=player.passes,
        rating=player.rating,
        ai_score=score,
        recommendation=rec
    )

    db.add(db_player)

    db.commit()

    db.refresh(db_player)

    return db_player


def get_players(db: Session):

    return db.query(models.Player).all()