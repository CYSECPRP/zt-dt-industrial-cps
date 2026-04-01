# Zero Trust-Enabled Digital Twins for Industrial CPS

This project implements a Zero Trust-Enabled Digital Twin for securing Industrial Cyber-Physical Systems. It uses AutoEncoders and Isolation Forests to detect real-time anomalies in water distribution datasets like BATADAL. The goal is a 94.5% F1-Score with a sub-2-second response time to ensure industrial resilience.

## Project Overview
Implementation of real-time anomaly detection for industrial control systems using Digital Twins and Zero Trust Architecture.

## Team Members
- **Member 1** (Team Lead) - Zero Trust Policy Engine
- **Member 2** (Data Engineer) - Data Preprocessing
- **Member 3** (ML Engineer) - AutoEncoder Model
- **Member 4** (ML Engineer) - Isolation Forest & Anomaly Scoring
- **Member 5** (Integration Engineer) - Digital Twin & Testing

## Datasets
- **BATADAL** - Water Distribution System
- **SWaT** - Secure Water Treatment (optional)

## Setup Instructions

### Windows Setup
```powershell
# Clone repository
git clone https://github.com/CYSECPRP/zt-dt-industrial-cps.git
cd zt-dt-industrial-cps

# Create virtual environment
python -m venv zt_dt_env

# Activate virtual environment
.\zt_dt_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Project Structure
```
├── data/              # Datasets
├── models/            # ML models
├── framework/         # Digital Twin + Zero Trust
├── utils/             # Helper functions
├── evaluation/        # Testing & metrics
└── main.py           # Main entry point
```

## Progress Tracker

- [x] Week 1: Project Setup
- [ ] Week 2: Data Preprocessing
- [ ] Week 3-4: ML Model Development
- [ ] Week 5-6: Integration
- [ ] Week 7: Testing & Evaluation
- [ ] Week 8: Documentation

## Target Metrics
- Precision: 95.2%
- Recall: 93.8%
- F1-Score: 94.5%
- False Positive Rate: <3%
- Response Time: <2 seconds
