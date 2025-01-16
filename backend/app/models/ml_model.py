import numpy as np
from sklearn.ensemble import RandomForestClassifier

class PredictionModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        
    def predict_match(self, home_stats, away_stats):
        features = np.concatenate([home_stats, away_stats])
        probabilities = self.model.predict_proba([features])[0]
        return {
            'home_win': float(probabilities[0]),
            'draw': float(probabilities[1]),
            'away_win': float(probabilities[2])
        }