class ZeroTrustPolicyEngine:
    def __init__(self):
        self.current_trust = 1.0
        self.alpha = 0.8
        
    def calculate_trust(self, anomaly_score):
        """
        Calculates exponentially moving average trust.
        """
        # If anomaly_score is high (1), Behavior Score is 0. If normal (0), Behavior Score is 1.
        behavior_score = 0.0 if anomaly_score == 1 else 1.0
        
        # New Trust = (alpha * Old Trust) + ((1 - alpha) * Behavior Score)
        self.current_trust = (self.alpha * self.current_trust) + ((1 - self.alpha) * behavior_score)
        
        # Access Decision based on thresholds
        if self.current_trust > 0.80:
            action = "ALLOW"
        elif 0.50 <= self.current_trust <= 0.80:
            action = "RESTRICT"
        else:
            action = "ISOLATE"
            
        return self.current_trust, action