from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.prediction import Prediction, PredictionResponse 
from ..services import predictions
from ..services.auth import get_current_user
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import func
from ..models.user import User

router = APIRouter()

class MatchData(BaseModel):
    match_id: str
    home_team: str
    away_team: str
    home_stats: List[float]
    away_stats: List[float]

@router.get("/protected")
async def protected_route(current_user = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}"}

@router.post("/predict", response_model=PredictionResponse)  # Update this line
async def create_prediction(
    match_data: MatchData,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        prediction = await predictions.create_prediction(match_data.dict(), db)
        return PredictionResponse.from_orm(prediction)  # Update this line
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/predictions/today", response_model=List[PredictionResponse])  # Update this line
async def get_todays_predictions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    today = datetime.now().date()
    return db.query(Prediction).filter(
        func.date(Prediction.created_at) == today
    ).all()