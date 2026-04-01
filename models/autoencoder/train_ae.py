import numpy as np
import os
import sys

# Add the project root to the system path so Python can find the 'models' module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.autoencoder.ae_model import build_lstm_autoencoder

def train_model_for_dataset(dataset_name, epochs=15, batch_size=128):
    print(f"\n=== Training AutoEncoder for {dataset_name.upper()} ===")
    
    # 1. Load the preprocessed training data
    train_path = f"data/processed/{dataset_name}/X_train.npy"
    if not os.path.exists(train_path):
        print(f"Error: {train_path} not found. Are you running this from the root directory?")
        return
        
    X_train = np.load(train_path)
    
    # Input shape is (Timesteps, Features). E.g., (60, 86) for SWaT
    input_shape = (X_train.shape[1], X_train.shape[2]) 
    print(f"Data loaded. Shape: {X_train.shape}")
    
    # 2. Build the model
    model = build_lstm_autoencoder(input_shape, latent_dim=16, dropout_rate=0.2)
    model.summary()
    
    # 3. Train the model
    print("\nStarting training...")
    history = model.fit(
        X_train, X_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.1,
        verbose=1
    )
    
    # 4. Save the trained model
    save_dir = f"models/autoencoder/checkpoints/{dataset_name}"
    os.makedirs(save_dir, exist_ok=True)
    model_path = os.path.join(save_dir, "ae_model.h5")
    model.save(model_path)
    
    print(f"\n[SUCCESS] Model saved to {model_path}")

if __name__ == "__main__":
    train_model_for_dataset("batadal", epochs=10) 
    train_model_for_dataset("swat", epochs=15)