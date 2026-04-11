<div align="center">

<br>

### Zero Trust-Enabled Digital Twins for Real-Time Anomaly Detection<br>in Industrial Cyber-Physical Systems

<br>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16+-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

[![IEEE Published](https://img.shields.io/badge/📄%20Published-IEEE%20NMITCON%202025-8B5CF6?style=for-the-badge)](https://doi.org/10.1109/NMITCON65824.2025.11188236)
[![Zero Trust](https://img.shields.io/badge/🔒%20Security-Zero%20Trust-0EA5E9?style=for-the-badge)]()
[![F1 Score](https://img.shields.io/badge/🎯%20F1--Score-≥94.5%25-EF4444?style=for-the-badge)]()
[![Response Time](https://img.shields.io/badge/⚡%20Response-<2%20seconds-F59E0B?style=for-the-badge)]()

<br>

> *Prototype implementation of the IEEE-published paper:*
>
> **"Zero Trust-Enabled Digital Twins for Real-Time Anomaly Detection in Industrial Cyber-Physical Systems"**
>
> *ICICI-2025 · IEEE Xplore · DOI: [10.1109/NMITCON65824.2025.11188236](https://doi.org/10.1109/NMITCON65824.2025.11188236)*

<br>

**TTEH LAB · School of Engineering, Dayananda Sagar University**
*Bangalore – 562112, Karnataka, India*

<br>

</div>

---

## 📌 At a Glance

```
┌─────────────────────────────────────────────────────────────────────┐
│  🏭 Problem   Industrial CPS face cyberattacks that bypass          │
│               traditional perimeter security                        │
│                                                                     │
│  💡 Solution  Digital Twin + Dual ML Models + Zero Trust Engine     │
│               for continuous, real-time threat detection            │
│                                                                     │
│  📊 Results   94.5% F1-Score · 2.8% FPR · <2s Response Time        │
│               Tested on BATADAL & SWaT industrial datasets          │
└─────────────────────────────────────────────────────────────────────┘
```

`Zero Trust Security` &nbsp;·&nbsp; `Digital Twins` &nbsp;·&nbsp; `Anomaly Detection` &nbsp;·&nbsp; `Industrial CPS` &nbsp;·&nbsp; `Real-Time ML`

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 1 | [🔍 Problem Statement](#1--problem-statement) |
| 2 | [🏗️ Proposed Architecture](#2--proposed-architecture) |
| 3 | [⚙️ How It Works](#3--how-it-works) |
| 4 | [📐 Mathematical Model](#4--mathematical-model) |
| 5 | [🔄 Core Algorithm](#5--core-algorithm) |
| 6 | [📊 Implementation Results](#6--implementation-results) |
| 7 | [🏛️ Code Architecture](#7--code-architecture) |
| 8 | [🔧 Core Modules — Deep Dive](#8--core-modules--deep-dive) |
| 9 | [🚀 Setup & Usage](#9--setup--usage) |
| 10 | [⚠️ Implementation Limitations](#10--implementation-limitations) |

---

## 1. 🔍 Problem Statement

> *"How can we secure industrial systems against attacks that traditional security cannot detect?"*

Industrial Cyber-Physical Systems control **critical infrastructure** — water treatment plants, power grids, and manufacturing facilities. These systems are increasingly targeted by attacks that bypass traditional perimeter defenses:

<table>
<tr>
<td width="50%">

**🚨 Threat Vectors**

- 🔓 **Insider Threats** — Authorized users with malicious intent
- 📦 **Supply Chain Attacks** — Compromised third-party components
- 🕵️ **Advanced Persistent Threats** — Long-term stealthy intrusions
- 💣 **Zero-Day Exploits** — Unknown vulnerabilities

</td>
<td width="50%">

**⚡ Resulting Risks**

- 🏭 **Operational Disruption** — Physical damage or service outages
- ☠️ **Safety Hazards** — Systems endangering human life
- 💰 **Economic Impact** — Millions in lost productivity
- 🕐 **Detection Delays** — Threats detected hours or days too late

</td>
</tr>
</table>

**The core problem:** Standard security assumes trust within the perimeter. Once inside, attackers have unrestricted access to manipulate sensors, actuators, and control systems.

**What's needed →** A framework providing **continuous verification**, **real-time anomaly detection**, and **adaptive access control** based on behavioral trust assessment.

---

## 2. 🏗️ Proposed Architecture

ZT-DT Industrial CPS implements Zero Trust security through **three integrated components**:

| # | Component | Role | Key Output |
|---|-----------|------|------------|
| 1️⃣ | **Digital Twin Core** | Virtual representation & anomaly detection | Real-time anomaly scores |
| 2️⃣ | **Zero Trust Engine** | Continuous trust assessment & policy enforcement | Dynamic access decisions |
| 3️⃣ | **Attack Injector** | Simulated attack scenarios for testing | Realistic threat simulation |

### 🖥️ System Dashboard

![First Dashboard](images/First_Dashboard.png)
*Initial system dashboard showing framework initialization and component status*

![Live Graph](images/Live_Graph.png)
*Live terminal dashboard for real-time monitoring*

---

## 3. ⚙️ How It Works

The framework operates through three integrated phases:

```
┌──────────────────────────────────────────────────────────────────────┐
│  PHASE 1 · Training & Baseline Establishment                         │
│                                                                      │
│  1. Collect normal operational data from industrial sensors          │
│  2. Train AutoEncoder + Isolation Forest on baseline data            │
│  3. Calibrate anomaly thresholds via grid search optimization        │
└──────────────────────────────────────────────────────────────────────┘
                               ↓
┌──────────────────────────────────────────────────────────────────────┐
│  PHASE 2 · Real-Time Monitoring & Trust Evaluation                   │
│                                                                      │
│  1. Ingest continuous sensor data from CPS components               │
│  2. Evaluate via dual-model (AE reconstruction + IF outlier score)   │
│  3. Calculate trust score via exponential moving average             │
│  4. Enforce access policy: ALLOW / RESTRICT / ISOLATE                │
└──────────────────────────────────────────────────────────────────────┘
                               ↓
┌──────────────────────────────────────────────────────────────────────┐
│  PHASE 3 · Attack Simulation & Validation                            │
│                                                                      │
│  1. Inject simulated attacks (spoofing, data injection, manipulation)│
│  2. Measure true positive/negative rates and FPR                     │
│  3. Evaluate response time and detection accuracy                    │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 4. 📐 Mathematical Model

The ZT-DT framework uses five core equations to model dynamic behavior, assess risk, and enforce adaptive access control.

### Eq. 1 · Digital Twin Prediction

Each CPS component $C_i$ is represented by a Digital Twin $DT_i$ predicting expected behavior:

$$\hat{d}_{i,t} = f_{DT}(d_{i,t-1}, d_{i,t-2}, \ldots, d_{i,t-k}; \theta_{DT})$$

| Symbol | Meaning |
|--------|---------|
| $\hat{d}_{i,t}$ | Predicted normal behavior |
| $d_{i,t-k}$ | Past observations (k timesteps) |
| $\theta_{DT}$ | AutoEncoder model weights |

### Eq. 2 · Anomaly Score Calculation

Anomalies are identified by comparing observed vs. predicted behavior:

$$A_i = \|d_{i,t} - \hat{d}_{i,t}\| + \lambda \cdot KL(p_{current} \| p_{historical})$$

- **First term** — Captures immediate behavioral deviations (L2 distance)
- **Second term** — Accounts for distributional shifts (KL divergence)
- **$\lambda$** — Adjusts sensitivity to contextual changes

### Eq. 3 · Dynamic Trust Score Update

Trust scores integrate recent anomalies with historical context via exponential moving average:

$$T_i(t) = \alpha \cdot T_i(t-1) + (1-\alpha) \cdot \left(1 - \frac{A_i}{A_{max}}\right)$$

- **$\alpha \in [0,1]$** — Weight of historical trust
- **$A_{max}$** — Normalizes anomaly scores to [0,1]

### Eq. 4 · Zero Trust Policy Decision

$$\text{Decision}(T_i) = \begin{cases}
\text{Allow} & \text{if } T_i \geq \tau_{high} \\
\text{Restrict} & \text{if } \tau_{low} \leq T_i < \tau_{high} \\
\text{Isolate} & \text{if } T_i < \tau_{low}
\end{cases}$$

> Default thresholds: $\tau_{high} = 0.80$, $\tau_{low} = 0.50$

### Eq. 5 · Model Parameter Update

Closed-loop feedback refines the Digital Twin through gradient descent:

$$\theta_{DT}(t+1) = \theta_{DT}(t) - \eta \nabla L(d_{i,t}, \hat{d}_{i,t})$$

- **$\eta$** — Learning rate
- **$L$** — Mean Squared Error reconstruction loss

---

## 5. 🔄 Core Algorithm

### Algorithm 1: ZT-DT Anomaly Detection and Access Control

```
Input:  Real-time CPS data stream D = {d₁, d₂, ..., dₙ}
Output: Access control decision (Allow, Restrict, Isolate)

 1:  Initialize Digital Twin models for all CPS components
 2:  Initialize Zero Trust Policy Engine (ZTP)
 3:  for each time interval t do
 4:    for each CPS component Cᵢ do
 5:      Receive real-time data dᵢ,ₜ from Cᵢ
 6:      Feed dᵢ,ₜ into Digital Twin model DTᵢ
 7:      Predict expected behavior d̂ᵢ,ₜ using DTᵢ
 8:      Compute anomaly score Aᵢ using Eq. 2
 9:      Update trust score Tᵢ = update_trust(Tᵢᵖʳᵉᵛ, Aᵢ)
10:     if Aᵢ > Anomaly_Threshold then
11:       Flag Cᵢ as anomalous
12:     end if
13:     Access_Decision ← ZTP.evaluate_policy(Tᵢ)
14:     if Access_Decision == "Isolate" then
15:       Block all communication Cᵢ
16:     else if Access_Decision == "Restrict" then
17:       Limit Cᵢ's functionality
18:     else
19:       Allow normal operation
20:     end if
21:   end for
22:   Log all trust scores, anomalies, and decisions
23: end for
```

---

## 6. 📊 Implementation Results

### 🧪 Experimental Setup

| Parameter | Details |
|-----------|---------|
| **Environment** | Python-based simulation with socket communication |
| **Components** | Virtual sensors, actuators, and PLC |
| **AE Optimization** | Grid search on latent dims (8–32), dropout (0.1–0.3), 5-fold CV |
| **IF Optimization** | Contamination rate tuning, 100 estimators |
| **Data Split** | 70% training / 30% testing — 60-timestep sliding window |
| **Hardware** | Intel i7, 16GB RAM |
| **Datasets** | SWaT (Secure Water Treatment) · BATADAL |

---

### 📈 Performance Results

**TABLE I: Accuracy & Detection Metrics**

| Method | Precision (%) | Recall (%) | F1-Score (%) |
|--------|:---:|:---:|:---:|
| 🥇 **ZT-DT (Proposed)** | **95.2** | **93.8** | **94.5** |
| AutoEncoder Only | 89.6 | 86.1 | 87.8 |
| Isolation Forest Only | 91.0 | 88.7 | 89.8 |
| Rule-Based IDS | 84.2 | 82.5 | 83.3 |

> ✅ **Key Finding:** ZT-DT achieves **9–12% improvement** in F1-Score over all baseline methods.

<br>

**TABLE II: Efficiency & Resource Metrics**

| Method | FPR (%) ↓ | Latency (s) ↓ | CPU Usage (%) ↓ |
|--------|:---:|:---:|:---:|
| 🥇 **ZT-DT (Proposed)** | **2.8** | **1.7** | **24.7** |
| AutoEncoder Only | 6.3 | 1.4 | 28.5 |
| Isolation Forest Only | 5.5 | 1.6 | 32.2 |
| Rule-Based IDS | 8.1 | 2.1 | 36.8 |

> ✅ **Key Finding:** ZT-DT reduces False Positive Rate to **2.8%** (vs 5.5–8.1%) while maintaining sub-2-second response time at lower CPU cost than all baselines.

---

### 🗺️ System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│        Physical CPS Components (Sensors / Actuators)         │
└────────────────────────┬─────────────────────────────────────┘
                         │ Real-time Data
                         ▼
         ┌───────────────────────────┐
         │    Digital Twin Module    │
         │   (Behavior Prediction)   │
         └────────────┬──────────────┘
                      │ Predicted Behavior d̂
                      ▼
         ┌───────────────────────────┐
         │  Anomaly Detection Engine │
         │   (AutoEncoder + IF)      │
         └────────────┬──────────────┘
                      │ Anomaly Score Aᵢ
                      ▼
         ┌───────────────────────────┐
         │  Zero Trust Policy Engine │
         │   (Trust Scoring + EMA)   │
         └────────────┬──────────────┘
                      │ Trust Score Tᵢ(t)
                      ▼
         ┌───────────────────────────┐
         │   Access Decision Module  │
         │  ALLOW · RESTRICT · ISOLATE│
         └────────────┬──────────────┘
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
   MONITOR       LOG & UPDATE      ENFORCE
```

### 📉 Latency vs. CPU Efficiency Trade-off

```
CPU Usage (%)
    36.8  │                                  ● Rule-Based IDS
    32.2  │                         ● Isolation Forest
    28.5  │                   ● AutoEncoder
    24.7  │          ★ ZT-DT (Proposed)        ← Best balance
           └──────────────────────────────────────
           1.4      1.6      1.7      2.1     Latency (s)
```

![Performance Graph](images/Graph.png)
*F1-Score, Precision, Recall, and FPR comparison across detection methods*

---

### 💬 Result Analysis

<table>
<tr>
<td width="50%">

**🎯 Detection Accuracy**

ZT-DT reached **95.2% precision** and **93.8% recall**, beating all baselines by 4–11 percentage points through its integrated dual-model approach.

**⚡ Response Time**

Median response of **1.7 seconds** (max <2s) makes this suitable for real-time industrial deployments where delayed action risks system-wide disruption.

</td>
<td width="50%">

**✅ False Positive Rate**

FPR reduced to just **2.8%** by combining behavioral baselines with trust history — distinguishing benign deviations from actual threats.

**💻 Resource Efficiency**

Averaging **24.7% CPU** during peak load, the framework runs on standard desktop hardware without specialized infrastructure.

</td>
</tr>
</table>

**Why the improvement?** The 9–12% F1 gain over baselines comes from the synergy of four integrated subsystems: Digital Twin behavioral prediction → Dual anomaly scoring (AE + IF) → Contextual EMA trust scoring → Trust-based dynamic policy enforcement.

---

## 7. 🏛️ Code Architecture

```
zt-dt-industrial-cps/
│
├── 📄 main.py                      # Main execution with live dashboard
├── 📄 dashboard.py                 # Additional dashboard functionality
├── 📄 requirements.txt             # Python dependencies
│
├── 📁 framework/
│   ├── 📁 digital_twin/
│   │   ├── dt_core.py              # Digital Twin anomaly detection core
│   │   └── __init__.py
│   └── 📁 zero_trust_engine/
│       ├── zt_policy.py            # Zero Trust policy engine
│       └── __init__.py
│
├── 📁 models/
│   ├── 📁 autoencoder/
│   │   ├── ae_model.py             # AutoEncoder model definition
│   │   ├── train_ae.py             # Training script
│   │   └── checkpoints/            # Pre-trained weights
│   └── 📁 isolation_forest/
│       ├── if_model.py             # Isolation Forest model
│       ├── train_if.py             # Training script
│       └── checkpoints/            # Pre-trained models
│
└── 📁 utils/
    ├── preprocess.py               # Data preprocessing utilities
    ├── attack_injector.py          # Attack simulation tools
    └── __init__.py
```

---

## 8. 🔧 Core Modules — Deep Dive

### `framework/digital_twin/dt_core.py` — Digital Twin Core

| Feature | Description |
|---------|-------------|
| **AutoEncoder Model** | Neural network for unsupervised anomaly detection |
| **Isolation Forest** | Tree-based outlier detection algorithm |
| **Ensemble Scoring** | Combined anomaly scores from both models |
| **Real-Time Evaluation** | Streaming data processing with minimal latency |

### `framework/zero_trust_engine/zt_policy.py` — Zero Trust Engine

| Feature | Description |
|---------|-------------|
| **Trust Scoring** | Exponential moving average for continuous assessment |
| **Policy Actions** | ALLOW · RESTRICT · ISOLATE based on trust thresholds |
| **Adaptive Thresholds** | Dynamic adjustment based on operational context |

![Node Trust Level](images/Node_Trust_Level.png)
*Trust scoring across CPS nodes with dynamic policy decisions*

### `utils/attack_injector.py` — Attack Injector

| Feature | Description |
|---------|-------------|
| **Attack Types** | DoS, integrity attacks, sensor manipulation |
| **Realistic Simulation** | Based on known industrial attack patterns |
| **Validation Framework** | Ground truth for detection accuracy testing |

#### 🟢 Normal Operation

![No Breach Detected](images/No_Breach_Detected.png)
*All nodes operating normally — high trust scores, no anomalies detected*

#### 🔴 Attack Detected

![Breach Detected](images/Breach_Detected.png)
*Breach flagged — automatic anomaly detection and access isolation triggered*

---

## 9. 🚀 Setup & Usage

### Prerequisites

- Python **3.8+**
- TensorFlow **2.16+**
- scikit-learn **1.3.2**

### Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/zt-dt-industrial-cps.git
cd zt-dt-industrial-cps

# Install dependencies
pip install -r requirements.txt
```

### Training Models

```bash
# Train AutoEncoder
python models/autoencoder/train_ae.py

# Train Isolation Forest
python models/isolation_forest/train_if.py
```

### Running the System

```bash
# Start real-time monitoring
python main.py
```

### Expected Output

```
Initializing components...
Initialization complete. Starting live stream...

Timestamp               | Status  | Anomaly | Trust Score | ZTP Action
-----------------------------------------------------------------------
2024-01-15 10:30:15.123 | Normal  |    0.12 |        0.95 | ✅ ALLOW
2024-01-15 10:30:16.456 | Normal  |    0.08 |        0.96 | ✅ ALLOW
2024-01-15 10:30:17.789 | Attack  |    0.87 |        0.34 | ⛔ RESTRICT
```

![Live Dashboard](images/Live_Graph.png)
*Real-time monitoring dashboard with anomaly detection and trust scoring*

![Logs](images/Logs.png)
*System logs showing detailed event tracking and decision history*

---

## 10. ⚠️ Implementation Limitations

| Limitation | Details |
|------------|---------|
| **Dataset Dependency** | Performance validated only on BATADAL and SWaT datasets |
| **Computational Requirements** | TensorFlow models benefit from GPU for optimal performance |
| **Real-World Deployment** | Requires integration with actual SCADA systems |
| **Attack Diversity** | Limited to simulated attack types, not all real-world scenarios |
| **Scalability** | Current implementation designed for single-system monitoring |

---

## 📦 Datasets

This project uses publicly available ICS datasets from **iTrust, Centre for Research in Cyber Security, Singapore University of Technology and Design**.

<table>
<tr>
<td width="50%">

### BATADAL
*Battle of the Attack Detection Algorithms*

- **Source**: Water Distribution System benchmark
- **Size**: ~500K records
- **Features**: 43 sensor measurements
- **Attacks**: 34 labeled attack scenarios (17 types)
- 🔗 [Request Dataset](https://itrust.sutd.edu.sg/itrust-labs_datasets/dataset_info/)

</td>
<td width="50%">

### SWaT
*Secure Water Treatment*

- **Source**: Physical water treatment testbed
- **Size**: ~900K records (11 days)
- **Features**: 51 sensors (continuous + discrete)
- **Attacks**: 6 real-world attack scenarios
- 🔗 [Request Dataset](https://itrust.sutd.edu.sg/itrust-labs_datasets/dataset_info/)

</td>
</tr>
</table>

### Dataset Access

Researchers can request datasets via [iTrust SUTD](https://itrust.sutd.edu.sg). Requirements:
- Institutional email and affiliation
- Agreement to usage terms

### Attribution

When using these datasets you must:
- ✅ Credit **"iTrust, Centre for Research in Cyber Security, Singapore University of Technology and Design"**
- ✅ Cite properly in all publications
- ⚠️ Keep datasets confidential
- 📧 Notify iTrust upon publication

> *"We acknowledge iTrust, Centre for Research in Cyber Security, Singapore University of Technology and Design, for providing the BATADAL and SWaT datasets used in this research."*

---

## 🛠️ Development

```bash
# Install dev dependencies
pip install pytest-cov black flake8

# Run tests
pytest tests/ -v --cov=framework --cov=models

# Code quality
black . --line-length=100
flake8 . --max-line-length=100
```

---

## 📈 Future Enhancements

- [ ] Real-time model retraining and adaptation
- [ ] Multi-system federation support
- [ ] Distributed inference across edge devices
- [ ] Advanced visualization dashboards
- [ ] Integration with SCADA/ICS platforms
- [ ] Explainability module (SHAP/LIME)
- [ ] Performance optimization for embedded systems
- [ ] Additional industrial datasets (gas, power, manufacturing)

---

## 🤝 Contributing

Contributions are welcome!

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/AmazingFeature`
3. **Commit** your changes: `git commit -m 'Add AmazingFeature'`
4. **Push** to the branch: `git push origin feature/AmazingFeature`
5. **Open** a Pull Request

---

## ⚖️ Disclaimer

This implementation is for **research and educational purposes only**. Production deployments must comply with:

- **IEC 62443** — Industrial Automation and Control Systems security standards
- **NIST Cybersecurity Framework** — Framework for managing cybersecurity risk
- **Industry-Specific Regulations** — Water, power, and manufacturing guidelines
- **Safety-Critical Requirements** — Formal verification for systems affecting human safety

---

## 👥 Contributors

| Name | USN | Email |
|------|-----|-------|
| Prajwal R P | ENG23CY0032 | eng23cy0032@dsu.edu.in |
| Sudeep Gowda | ENG24CY1005 | eng24cy1005@dsu.edu.in |
| Darshan H | ENG23CY0011 | eng23cy0011@dsu.edu.in |
| Shashanka N | ENG23CY0036 | eng23cy0036@dsu.edu.in |
| Shivalingayya S Yadrami | ENG23CY0037 | eng23cy0037@dsu.edu.in |

**Department of Computer Science and Engineering (Cyber Security)**
School of Engineering, Dayananda Sagar University

---

## 🧑‍🏫 Mentor

**Dr. Prajwalasimha S N**, Ph.D., Postdoc. (NewRIIS)
Associate Professor — Department of CSE (Cyber Security)
School of Engineering, Dayananda Sagar University

---

<div align="center">

**TTEH LAB · School of Engineering · Dayananda Sagar University**

*Bangalore – 562112, Karnataka, India*

<br>

*If you find this work useful, please consider giving it a ⭐*

</div>
