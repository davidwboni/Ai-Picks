from sqlalchemy.orm import Session
from ..models.prediction import Prediction
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class PredictionService:
    def __init__(self):
        self.model = RandomForestClassifier()
        
    def predict(self, home_stats: list, away_stats: list) -> float:
        features = np.concatenate([home_stats, away_stats]).reshape(1, -1)
        return 0.7

async def create_prediction(match_data: dict, db: Session) -> Prediction:
    prediction = Prediction(
        match_id=match_data['match_id'],
        home_team=match_data['home_team'],
        away_team=match_data['away_team'],
        prediction=0.7,  # Placeholder
        user_id=1  # Add user_id
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction
    
    prediction = Prediction(
        match_id=match_data['match_id'],
        home_team=match_data['home_team'],
        away_team=match_data['away_team'],
        prediction=prediction_value
    )
    
    return prediction