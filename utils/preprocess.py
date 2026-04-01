import numpy as np

def get_simulated_stream(num_steps=100):
    """
    Generator yielding synthetic sensor readings for a CPS.
    Simulates 'normal' behavior of 5 sensors (e.g., flow rate, pressure, temperature, level, pump speed).
    """
    # Define baselines and standard deviations for 5 sensors
    baselines = np.array([50.0, 120.0, 22.5, 8.0, 1500.0])
    noise_std = np.array([2.0, 5.0, 0.5, 0.2, 10.0])
    
    for _ in range(num_steps):
        # Generate normal reading with Gaussian noise
        reading = baselines + np.random.normal(0, noise_std)
        # Yield as dictionary for easy indexing or readability
        yield {
            "flow_rate": reading[0],
            "pressure": reading[1],
            "temperature": reading[2],
            "tank_level": reading[3],
            "pump_speed": reading[4]
        }