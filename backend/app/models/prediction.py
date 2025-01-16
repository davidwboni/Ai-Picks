from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from ..database import Base
from pydantic import BaseModel
from typing import Optional

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(String)
    home_team = Column(String)
    away_team = Column(String)
    prediction = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class PredictionResponse(BaseModel):
    id: int
    match_id: str
    home_team: str
    away_team: str
    prediction: float
    created_at: Optional[datetime]

    class Config:
        from_attributes = True