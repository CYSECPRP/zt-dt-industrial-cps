def inject_anomaly(sensor_data):
    """
    Takes normal sensor data and drastically multiplies the values 
    to simulate a severe data manipulation attack on the CPS.
    """
    anomalous_data = {}
    multiplier = 7.5 # Multiply by 7.5 to simulate extreme manipulation
    for key, value in sensor_data.items():
        anomalous_data[key] = value * multiplier
    return anomalous_data