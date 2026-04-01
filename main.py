import time
from datetime import datetime
from utils.preprocess import get_simulated_stream
from utils.attack_injector import inject_anomaly
from framework.digital_twin.dt_core import DigitalTwin
from framework.zero_trust_engine.zt_policy import ZeroTrustPolicyEngine

# ANSI terminal colors
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"

def main():
    print("Initializing components...")
    dt = DigitalTwin()
    ztp_engine = ZeroTrustPolicyEngine()
    print("Initialization complete. Starting live stream...\n")
    
    # Print Dashboard Header
    print(f"{'Timestamp':<25} | {'Status':<15} | {'Anomaly':<7} | {'Trust Score':<12} | {'ZTP Action'}")
    print("-" * 85)
    
    # Get the synthetic data stream
    stream = get_simulated_stream(num_steps=100)
    
    for i, data in enumerate(stream):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        status = "Normal"
        
        # Trigger Attacks every 10th tick
        if (i + 1) % 10 == 0:
            data = inject_anomaly(data)
            status = "Attack"
            
        # Digital Twin Evaluation
        anomaly_score = dt.evaluate(data)
        
        # ZT Engine Evaluation
        trust_score, action = ztp_engine.calculate_trust(anomaly_score)
        
        # Format the output with colors
        if action == "ALLOW":
            action_color = GREEN
        elif action == "RESTRICT":
            action_color = YELLOW
        else:
            action_color = RED
            
        status_color = RED if status == "Attack" else GREEN
            
        print(f"{CYAN}{timestamp}{RESET} | "
              f"{status_color}{status:<15}{RESET} | "
              f"{anomaly_score:<7} | "
              f"{trust_score:<12.4f} | "
              f"{action_color}{action}{RESET}")
              
        # Simulate real-time streaming
        time.sleep(1)

if __name__ == "__main__":
    main()