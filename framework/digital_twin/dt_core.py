from sklearn.ensemble import IsolationForest
import numpy as np
import sys
import os

# Add the parent directory to the path so we can import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.preprocess import get_simulated_stream

class DigitalTwin:
    def __init__(self):
        # Initialize IsolationForest and train on a small batch of normal data
        self.model = IsolationForest(contamination=0.05, random_state=42)
        print("Digital Twin initializing: Baseline training on synthetic data...")
        self._baseline_training()
        
    def _baseline_training(self):
        # Briefly train on a small batch of normal synthetic data
        training_stream = get_simulated_stream(num_steps=50) 
        train_data = []
        for data_dict in training_stream:
            features = list(data_dict.values())
            train_data.append(features)
            
        self.model.fit(train_data)
        
    def evaluate(self, sensor_data):
        """
        Takes real-time data, predicts anomaly, returns anomaly_score 
        (0 for normal, 1 for anomaly).
        """
        features = np.array([list(sensor_data.values())])
        
        # IsolationForest returns 1 for inliers (normal) and -1 for outliers (anomaly)
        prediction = self.model.predict(features)[0]
        
        # Convert to 1 for anomaly, 0 for normal
        if prediction == -1:
            anomaly_score = 1
        else:
            anomaly_score = 0
            
        return anomaly_score