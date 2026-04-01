import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, RepeatVector, TimeDistributed, Dense

def build_lstm_autoencoder(input_shape, latent_dim=16, dropout_rate=0.2):
    """
    Builds an LSTM AutoEncoder for time-series anomaly detection.
    Matches the paper's hyperparameter specifications (latent_dim: 8-32, dropout: 0.1-0.3).
    """
    model = Sequential([
        # Encoder
        LSTM(64, activation='relu', input_shape=input_shape, return_sequences=True),
        LSTM(latent_dim, activation='relu', return_sequences=False),
        Dropout(dropout_rate),
        
        # Bridge
        RepeatVector(input_shape[0]), # Repeats the latent vector for the window size (60)
        
        # Decoder
        LSTM(latent_dim, activation='relu', return_sequences=True),
        LSTM(64, activation='relu', return_sequences=True),
        Dropout(dropout_rate),
        
        # Output Layer (Reconstructs the original features)
        TimeDistributed(Dense(input_shape[1]))
    ])
    
    model.compile(optimizer='adam', loss='mse')
    return model