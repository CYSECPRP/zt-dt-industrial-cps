import numpy as np
import os
import sys

# Add the project root to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.isolation_forest.if_model import build_isolation_forest, save_if_model

def train_if_for_dataset(dataset_name):
    print(f"\n=== Training Isolation Forest for {dataset_name.upper()} ===")
    
    # 1. Load the preprocessed training data
    train_path = f"data/processed/{dataset_name}/X_train.npy"
    if not os.path.exists(train_path):
        print(f"Error: {train_path} not found.")
        return
        
    X_train_3d = np.load(train_path)
    print(f"Loaded 3D Data Shape: {X_train_3d.shape}")
    
    # 2. Reshape (Flatten) the data from 3D to 2D for scikit-learn
    # Shape becomes: (Samples, Timesteps * Features)
    num_samples = X_train_3d.shape[0]
    num_timesteps = X_train_3d.shape[1]
    num_features = X_train_3d.shape[2]
    
    X_train_2d = X_train_3d.reshape((num_samples, num_timesteps * num_features))
    print(f"Flattened 2D Data Shape: {X_train_2d.shape}")
    
    # 3. Build and train the model
    # Using 100 estimators as per the paper's specification
    print("Starting training (this may take a moment for SWaT)...")
    model = build_isolation_forest(n_estimators=100)
    model.fit(X_train_2d)
    
    # 4. Save the trained model
    save_dir = f"models/isolation_forest/checkpoints/{dataset_name}"
    os.makedirs(save_dir, exist_ok=True)
    model_path = os.path.join(save_dir, "if_model.pkl")
    
    save_if_model(model, model_path)
    print(f"[SUCCESS] Isolation Forest saved to {model_path}")

if __name__ == "__main__":
    train_if_for_dataset("batadal")
    train_if_for_dataset("swat")