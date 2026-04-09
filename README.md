# Zero Trust-Enabled Digital Twins for Real-Time Anomaly Detection in Industrial Cyber-Physical Systems

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active_Development-f59e0b?style=for-the-badge)]()
[![IEEE](https://img.shields.io/badge/Published-IEEE_NMITCON_2025-00629B?style=for-the-badge&logo=ieee&logoColor=white)]()

**A novel security framework integrating Zero Trust Architecture with Digital Twin technology for real-time anomaly detection and adaptive access control in Industrial Cyber-Physical Systems.**

[Overview](#overview) • [Architecture](#architecture) • [Installation](#installation) • [Usage](#usage) • [Results](#results) • [Dataset](#dataset) • [Authors](#authors) • [Collaborators](#collaborators)

</div>

---

## Overview

Industrial Cyber-Physical Systems (CPS) are increasingly targeted by sophisticated cyberattacks that exploit tightly integrated computational and physical components. Traditional perimeter-based security models and static access controls are inadequate against dynamic threats such as insider attacks, lateral movement, and real-time data manipulation.

This project presents the **Zero Trust-enabled Digital Twin (ZT-DT) framework** — a fully implemented and validated Python-based simulation environment that:

- Creates **virtual Digital Twin representations** of CPS components to model real-time operational behavior
- Employs a **machine learning-driven anomaly detection engine** combining AutoEncoders and Isolation Forests
- Integrates **Zero Trust principles** — continuous authentication, micro-segmentation, and behavior-based trust scoring — to dynamically isolate or mitigate suspicious entities
- Delivers **≥ 94.5% F1-Score** with a median response latency of **1.7 seconds**, enabling rapid detection and enforcement without physical hardware deployment

This work was published at the **2025 Third International Conference on Networks, Multimedia and Information Technology (NMITCON)**, IEEE.

---

## Features

- **Real-Time Anomaly Detection**
  - Dual-model approach: AutoEncoder (reconstruction error) combined with Isolation Forest (outlier partitioning)
  - Sub-2-second inference pipeline for critical infrastructure response
  - Adaptive anomaly thresholding using exponential moving averages

- **Zero Trust Policy Engine**
  - Continuous trust scoring via Exponential Moving Average (EMA)
  - Dynamic access control with three tiers: `ALLOW` / `RESTRICT` / `ISOLATE`
  - Behavior-based trust assessment decoupled from network location or static role

- **Digital Twin Framework**
  - Virtual representation of physical CPS components (sensors, actuators, PLCs)
  - Baseline training on labeled normal operational data
  - Real-time synchronization with simulated sensor streams via socket communication

- **Industrial Dataset Support**
  - BATADAL (Battle of the Attack Detection Algorithms — Water Distribution System)
  - SWaT (Secure Water Treatment testbed)
  - Extensible architecture for custom industrial datasets

- **Production-Ready Features**
  - Pre-trained model checkpoints for both datasets
  - Comprehensive logging, dashboarding, and live stream processing
  - Reproducible experiments with fixed random seeds and chronological data splits

---

## Architecture

The ZT-DT framework operates as a **closed feedback loop** tightly integrating data collection, behavioral analysis, and access control enforcement.

```
┌──────────────────────────────────────────────────────────┐
│             Industrial CPS  (Sensors / SCADA)            │
└───────────────────────┬──────────────────────────────────┘
                        │  Real-Time Data Stream
                        ▼
            ┌───────────────────────────┐
            │     Data Preprocessing    │
            │   (Normalization, Scaling)│
            └───────────┬───────────────┘
                        │
           ┌────────────┴────────────┐
           ▼                         ▼
       ┌─────────────┐        ┌──────────────┐
       │ AutoEncoder │        │  Isolation   │
       │   Anomaly   │        │   Forest     │
       │  Detector   │        │  Detector    │
       └──────┬──────┘        └──────┬───────┘
              │                      │
              └──────────┬───────────┘
                         ▼
            ┌──────────────────────────┐
            │      Anomaly Score       │
            │  (0 = Normal, 1 = Attack)│
            └──────────────┬───────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │    Zero Trust Policy Engine  │
            │  - Trust Scoring (EMA)       │
            │  - Access Control Decision   │
            └──────────────┬───────────────┘
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
           ALLOW / RESTRICT / ISOLATE
```

### Framework Components

| Component | Role |
|---|---|
| **Digital Twin (DT)** | Maintains real-time virtual models of CPS components; establishes behavioral baselines |
| **Anomaly Detection Engine** | AutoEncoder + Isolation Forest ensemble to detect known and zero-day threats |
| **Zero Trust Policy Engine** | Evaluates dynamic trust scores; enforces fine-grained access decisions |
| **Feedback Loop** | Continuously refines DT model parameters via gradient descent on reconstruction loss |

---

## Mathematical Model

### Digital Twin Behavioral Prediction

Each CPS component $C_i$ is represented by Digital Twin $DT_i$. The expected state is predicted from historical observations:

$$\hat{d}_{i,t} = f_{DT}(d_{i,t-1},\ d_{i,t-2},\ \ldots,\ d_{i,t-k};\ \theta_{DT})$$

### Anomaly Score Computation

Anomalies are quantified by combining immediate behavioral deviation with distributional divergence:

$$A_i = \|d_{i,t} - \hat{d}_{i,t}\| + \lambda \cdot KL(p_{\text{current}} \| p_{\text{historical}})$$

### Trust Score Update (Exponential Moving Average)

$$T_i(t) = \alpha \cdot T_i(t-1) + (1 - \alpha) \cdot \left(1 - \frac{A_i}{A_{\max}}\right)$$

where $\alpha \in [0, 1]$ controls the influence of historical trust.

### Zero Trust Access Control Decision

$$\text{Decision}(T_i) = \begin{cases} \text{Allow} & \text{if } T_i \geq \tau_{\text{high}} \\ \text{Restrict} & \text{if } \tau_{\text{low}} \leq T_i < \tau_{\text{high}} \\ \text{Isolate} & \text{if } T_i < \tau_{\text{low}} \end{cases}$$

---

## Project Structure

```
zt-dt-industrial-cps/
│
├── framework/                           # Core framework modules
│   ├── digital_twin/
│   │   ├── dt_core.py                   # Digital Twin implementation
│   │   └── __init__.py
│   └── zero_trust_engine/
│       ├── zt_policy.py                 # Zero Trust Policy Engine
│       └── __init__.py
│
├── models/                              # Machine Learning Models
│   ├── autoencoder/
│   │   ├── ae_model.py                  # AutoEncoder architecture
│   │   ├── train_ae.py                  # AutoEncoder training script
│   │   ├── checkpoints/                 # Pre-trained model weights
│   │   │   ├── batadal/ae_model.h5
│   │   │   └── swat/ae_model.h5
│   │   └── __init__.py
│   ├── isolation_forest/
│   │   ├── if_model.py                  # Isolation Forest implementation
│   │   ├── train_if.py                  # Isolation Forest training script
│   │   ├── checkpoints/                 # Saved model checkpoints
│   │   │   ├── batadal/
│   │   │   └── swat/
│   │   └── __init__.py
│   └── __init__.py
│
├── utils/                               # Utility Functions
│   ├── preprocess.py                    # Data preprocessing and simulation
│   ├── attack_injector.py               # Synthetic attack injection
│   └── __init__.py
│
├── images/                              # Documentation figures
├── main.py                              # Main pipeline entry point
├── dashboard.py                         # Interactive web dashboard
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- Minimum 4 GB RAM (8 GB recommended)
- Compatible with Windows, macOS, and Linux

### Step 1 — Clone the Repository

```bash
git clone https://github.com/CYSECPRP/zt-dt-industrial-cps.git
cd zt-dt-industrial-cps
```

### Step 2 — Create a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv zt_dt_env
.\zt_dt_env\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv zt_dt_env
source zt_dt_env/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Running the Real-Time Anomaly Detection Pipeline

```bash
python main.py
```

The pipeline will display a live console output showing:

| Column | Description |
|---|---|
| `Timestamp` | Precise timestamp of each data point |
| `Status` | Ground truth operational state (Normal / Attack) |
| `Anomaly` | Anomaly flag output from the Digital Twin (0 or 1) |
| `Trust Score` | Computed EMA-based trust score (0.0 – 1.0) |
| `ZTP Action` | Zero Trust Policy Engine decision (ALLOW / RESTRICT / ISOLATE) |

**Example Console Output:**

```
Timestamp                | Status          | Anomaly | Trust Score | ZTP Action
2026-04-01 10:30:45.123  | Normal          |    0    |   0.9800    | ALLOW
2026-04-01 10:30:46.124  | Normal          |    0    |   0.9840    | ALLOW
2026-04-01 10:30:47.125  | Attack          |    1    |   0.7970    | RESTRICT
2026-04-01 10:30:48.126  | Attack          |    1    |   0.6576    | RESTRICT
2026-04-01 10:30:49.127  | Normal          |    0    |   0.7261    | RESTRICT
```

### Launching the Interactive Dashboard

```bash
python dashboard.py
```

---

## Configuration

### Key Hyperparameters

**Digital Twin / Isolation Forest:**

| Parameter | Value | Description |
|---|---|---|
| `contamination` | 0.05 | Expected anomaly rate in training data (5%) |
| `n_estimators` | 100 | Number of trees in Isolation Forest |
| `random_state` | 42 | Fixed seed for reproducibility |

**AutoEncoder:**

| Parameter | Search Range | Method |
|---|---|---|
| `latent_dimensions` | 8 – 32 | Grid search with 5-fold cross-validation |
| `dropout_rate` | 0.1 – 0.3 | Grid search with 5-fold cross-validation |

**Zero Trust Policy Engine:**

| Parameter | Value | Description |
|---|---|---|
| `alpha` | 0.8 | EMA weight for historical trust influence |
| `tau_high` | 0.80 | Trust threshold for ALLOW decision |
| `tau_low` | 0.50 | Trust threshold for ISOLATE decision |

**Data Splitting:**

| Split | Proportion | Notes |
|---|---|---|
| Training | 70% | Chronological order maintained |
| Testing | 30% | Sliding window of 60 timesteps |

---

## Results

### Accuracy and Detection Metrics

| Method | Precision (%) | Recall (%) | F1-Score (%) |
|---|---|---|---|
| **ZT-DT (Proposed)** | **95.2** | **93.8** | **94.5** |
| AutoEncoder | 89.6 | 86.1 | 87.8 |
| Isolation Forest | 91.0 | 88.7 | 89.8 |
| Rule-Based IDS | 84.2 | 82.5 | 83.3 |

### Efficiency and Resource Metrics

| Method | False Positive Rate (%) | Latency (s) | CPU Usage (%) |
|---|---|---|---|
| **ZT-DT (Proposed)** | **2.8** | **1.7** | **24.7** |
| AutoEncoder | 6.3 | 1.4 | 28.5 |
| Isolation Forest | 5.5 | 1.6 | 32.2 |
| Rule-Based IDS | 8.1 | 2.1 | 36.8 |

The ZT-DT framework achieves a **9% to 12% improvement** in F1-Score over standalone baselines, with a **false positive rate of just 2.8%** — the lowest among all evaluated methods. The median response latency of **1.7 seconds** from anomaly detection to policy enforcement makes the framework suitable for real-time industrial deployments.

Experiments were conducted on standardized hardware (Intel Core i7, 16 GB RAM) with fixed random seeds to ensure full reproducibility.

### Console Output — Pipeline Execution

The real-time anomaly detection pipeline produces the following structured console output during execution:

```
Timestamp                | Status          | Anomaly | Trust Score | ZTP Action
-------------------------|-----------------|---------|-------------|------------
2026-04-01 10:30:45.123  | Normal          |    0    |   0.9800    | ALLOW
2026-04-01 10:30:46.124  | Normal          |    0    |   0.9840    | ALLOW
2026-04-01 10:30:47.125  | Attack          |    1    |   0.7970    | RESTRICT
2026-04-01 10:30:48.126  | Attack          |    1    |   0.6576    | RESTRICT
2026-04-01 10:30:49.127  | Normal          |    0    |   0.7261    | RESTRICT
```

Each row represents a single evaluation tick. During an attack event, the trust score degrades via the EMA update and the Zero Trust Policy Engine escalates the enforcement action from `ALLOW` to `RESTRICT`. Trust recovery occurs gradually as normal behavior resumes, demonstrating the hysteresis effect built into the EMA-based trust model.

### Dashboard Output

The interactive dashboard (`dashboard.py`) provides live visualization of the ZT-DT framework across three tabs: **Live Monitoring**, **CPS Topology**, and **Audit Logs**.

**Secure State — No Breach Detected**

System status shows `SECURE` with ZTP Enforcement set to `ALLOW`. Active Node Trust is high (0.8349) and Anomaly Probability reads 0%. The Trust Score line (cyan) remains elevated while the Anomaly Score (red dashed) stays near zero.

![No Breach Detected](images/No_Breach_Detected.png)

**Attack State — Breach Detected**

Upon injecting a targeted attack, the system immediately transitions to `BREACH DETECTED`. Anomaly Probability spikes to 100%, the Active Node Trust drops (0.7982, delta −0.1995), and ZTP Enforcement escalates to `RESTRICT`. The red dashed Anomaly Score line spikes sharply while the Trust Score line begins to degrade.

![Breach Detected](images/Breach_Detected.png)

**Zero Trust Evaluation Engine — Live Graph**

The live monitoring chart plots three overlaid signals in real time: Trust Score (cyan, filled area), Anomaly Score (red dashed), and Sensor Flow Rate (green). Attack events are clearly visible as sharp upward spikes in the Anomaly Score accompanied by corresponding trust degradation.

![Zero Trust Evaluation Engine Graph](images/Graph.png)

**Audit Logs — Zero Trust Policy Logs**

The Audit Logs tab displays a timestamped record of every evaluation cycle for each CPS node, including the raw Anomaly Score, computed Trust Score, enforced Action, sensor Flow rate, and Pressure readings. Highlighted rows (amber) indicate `RESTRICT` decisions immediately following an attack event, with subsequent rows transitioning back to `ALLOW` as the trust score recovers.

![Zero Trust Policy Logs](images/Logs.png)

---

## Dataset

This project uses publicly available Industrial Control System datasets provided through academic collaboration with **iTrust, Centre for Research in Cyber Security, Singapore University of Technology and Design**.

### BATADAL — Battle of the Attack Detection Algorithms

- **Domain:** Water Distribution System benchmark
- **Size:** Approximately 500,000 records
- **Features:** 43 sensor measurements (pressures, flow rates, pump states)
- **Attack Scenarios:** 34 labeled attack scenarios covering 17 distinct attack types
- **Reference:** [BATADAL Dataset — iTrust SUTD](https://itrust.sutd.edu.sg/itrust-labs_datasets/dataset_info/)

### SWaT — Secure Water Treatment

- **Domain:** Physical testbed for multi-stage water treatment processes
- **Size:** Approximately 900,000 records (11 days of continuous operation)
- **Features:** 51 sensors (continuous and discrete measurements)
- **Attack Scenarios:** 6 real-world attack scenarios targeting critical process stages
- **Reference:** [SWaT Dataset — iTrust SUTD](https://itrust.sutd.edu.sg/itrust-labs_datasets/dataset_info/)

### Dataset Access and Attribution

Researchers may request these datasets through the [iTrust SUTD website](https://itrust.sutd.edu.sg). Requests require institutional affiliation and agreement to usage terms.

When using these datasets, the following attribution is required in all publications:

> *"We acknowledge iTrust, Centre for Research in Cyber Security, Singapore University of Technology and Design, for providing the BATADAL and SWaT datasets used in this research."*

---

## Future Work

- [ ] Hardware-in-the-Loop (HIL) testing for real-world validation
- [ ] Privacy-preserving federated learning for distributed anomaly detection
- [ ] Explainable Artificial Intelligence integration (SHAP / LIME) for trust transparency
- [ ] Replacing rule-based policies with adaptive, learning-based policy mechanisms
- [ ] Distributed inference deployment across edge devices
- [ ] Extension to additional critical domains: smart grids, healthcare, manufacturing
- [ ] Advanced real-time visualization dashboards
- [ ] Integration with SCADA / ICS platforms

---

## Authors

This research was published at the **2025 Third International Conference on Networks, Multimedia and Information Technology (NMITCON)**, IEEE.

| Author | Affiliation |
|---|---|
| **G. Hemanth Kumar** | Department of CSE (Cyber Security), School of Engineering, Dayananda Sagar University, Bangalore, India |
| **Nilesh Shelke** | Department of CSE, Symbiosis Institute of Technology, Nagpur, India |
| **Amit Pimpalkar** | School of Computer Science and Engineering, Ramdeobaba University, Nagpur, India |
| **Dilip Kumar Jang Bahadur Saini** | Department of CSE (Cyber Security), School of Engineering, Dayananda Sagar University, Bangalore, India |
| **Prajwalasimha S N** | School of Computing Science, Newcastle University (NUiS), Singapore |
| **Y. Dileep Kumar** | Department of ECE, School of Engineering, Mohan Babu University, Tirupati, India |

---

## Collaborators

The following individuals contributed to the implementation, experimentation, and development of this project:

| Name | Role |
|---|---|
| **Prajwal R P** | Zero Trust Policy Engine — Project Lead |
| **Shivalingayya Yadrami** | Data Engineering |
| **Shashanka N** | Machine Learning — AutoEncoder and Isolation Forest |
| **Darshan H** | Integration Engineering — Digital Twin and System Testing |

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

---

## Disclaimer

This implementation is intended for research and educational purposes. When deployed in production environments, ensure compliance with:

- Industrial control system security standards (IEC 62443)
- NIST Cybersecurity Framework
- Industry-specific regulations applicable to your sector (for example, water sector guidelines)
- Safety-critical system requirements

---

<div align="center">

**Institution:** Dayananda Sagar University, Bangalore, India

**[Back to Top](#zero-trust-enabled-digital-twins-for-real-time-anomaly-detection-in-industrial-cyber-physical-systems)**

</div>
