from sklearn.ensemble import IsolationForest
import joblib

def build_isolation_forest(n_estimators=100, contamination='auto', random_state=42):
    """
    Builds an Isolation Forest model with 100 estimators as defined in the framework methodology.
    """
    model = IsolationForest(
        n_estimators=n_estimators,
        contamination=contamination,
        random_state=random_state,
        n_jobs=-1 # Uses all available CPU cores for faster training
    )
    return model

def save_if_model(model, file_path):
    """Saves the scikit-learn model using joblib."""
    joblib.dump(model, file_path)

def load_if_model(file_path):
    """Loads a saved scikit-learn model."""
    return joblib.load(file_path)