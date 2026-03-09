from sqlalchemy import Column, Integer, String, Float
from database import Base

class Player(Base):

    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    position = Column(String)

    goals = Column(Integer)

    assists = Column(Integer)

    passes = Column(Integer)

    rating = Column(Float)

    ai_score = Column(Float)

    recommendation = Column(String)