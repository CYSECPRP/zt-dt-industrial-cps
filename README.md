# 🏭 ZT-DT
## Zero Trust-Enabled Digital Twins for Real-Time Anomaly Detection in Industrial Cyber-Physical Systems

*School of Engineering, Dayananda Sagar University · Bangalore, India*
*Symbiosis Institute of Technology · Ramdeobaba University · Newcastle University (NUiS) · Mohan Babu University*

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-AE%20%7C%20IF-orange) ![Zero Trust](https://img.shields.io/badge/Security-Zero%20Trust-success) ![IEEE](https://img.shields.io/badge/Published-IEEE%20NMITCON%202025-blueviolet) ![License](https://img.shields.io/badge/License-MIT-green.svg)

*Prototype implementation of:*
**"Zero Trust-Enabled Digital Twins for Real-Time Anomaly Detection in Industrial Cyber Physical Systems"**
*2025 Third International Conference on Networks, Multimedia and Information Technology (NMITCON), IEEE Xplore · DOI: 10.1109/NMITCON65824.2025.11188236*

---

## 🔭 Overview

Industrial Cyber-Physical Systems (CPS) are increasingly vulnerable to sophisticated cyberattacks that exploit their tightly integrated computational and physical components. Traditional security models, relying on fixed perimeters and static access controls, inadequately address dynamic threats such as insider attacks and real-time data manipulation.

This project presents the **Zero Trust-enabled Digital Twin (ZT-DT) framework**—a novel security framework integrating Zero Trust Architecture (ZTA) with Digital Twin (DT) technology. It enforces continuous authentication through virtual twins of CPS components and a machine learning-driven anomaly detection engine. Validated within a Python-based simulation environment, the framework dynamically isolates or mitigates suspicious entities, achieving a **94.5% F1-Score** and a **1.7-second median response latency** without requiring physical hardware deployment.

Digital Twins · AutoEncoders · Isolation Forests · Zero Trust Architecture · SWaT · BATADAL · Real-Time Detection

---

## 📋 Table of Contents
1. [🔍 Problem Statement](#1--problem-statement)
2. [🏗️ Proposed Architecture](#2-️-proposed-architecture)
3. [⚡ How It Works (Mathematical Model)](#3--how-it-works-mathematical-model)
4. [📊 Paper Results & Metrics](#4--paper-results--metrics)
5. [🗂️ Code Architecture](#5-️-code-architecture)
6. [🚀 Setup & Usage](#6--setup--usage)
7. [📂 Datasets](#7--datasets)
8. [👥 Authors & Contributors](#8--authors--contributors)

---

## 1. 🔍 Problem Statement

Conventional CPS security models primarily rely on perimeter defenses, role-based access control (RBAC), and intrusion detection systems (IDS). These rule-based and signature-based mechanisms struggle to detect zero-day or adaptive attacks. Furthermore, once an attacker breaches the perimeter, they often gain unfettered access to sensors, actuators, and PLCs.

*What's needed →* A framework that combines physical process modeling (**Digital Twins**) with continuous, behavior-based security enforcement (**Zero Trust Architecture**) to provide active defense, proactive anomaly detection, and granular access control in real-time.

---

## 2. 🏗️ Proposed Architecture

The ZT-DT framework operates as a closed-loop feedback mechanism where data collection, behavior analysis, and access control enforcement are tightly integrated.

| *#* | *Module* | *Role* | *Key Output* |
| :--- | :--- | :--- | :--- |
| 1️⃣ | **Digital Twin (DT)** | Predicts expected operational state of CPS | Expected behavior $\hat{d}_{i,t}$ |
| 2️⃣ | **Anomaly Engine** | AE + Isolation Forest ensemble for threat detection | Anomaly Score $A_i$ |
| 3️⃣ | **ZT Policy Engine** | Evaluates trust scores via moving averages | Continuous Trust Score $T_i$ |
| 4️⃣ | **Access Control** | Enforces adaptive security policies | `Allow` / `Restrict` / `Isolate` |

```text
┌──────────────────────────────────────────────────────────┐
│             Industrial CPS  (Sensors / SCADA)            │
└───────────────────────┬──────────────────────────────────┘
                        │  Real-Time Data Stream
                        ▼
            ┌───────────────────────────┐
            │   Digital Twin Model (DT) │
            └───────────┬───────────────┘
                        │ Predicts Expected Behavior
           ┌────────────┴────────────┐
           ▼                         ▼
       ┌─────────────┐        ┌──────────────┐
       │ AutoEncoder │        │  Isolation   │
       └──────┬──────┘        └──────┬───────┘
              │                      │
              └──────────┬───────────┘
                         ▼
            ┌──────────────────────────┐
            │      Anomaly Score       │
            └──────────────┬───────────┘
                           │ Update Trust
                           ▼
            ┌──────────────────────────────┐
            │    Zero Trust Policy Engine  │
            └──────────────┬───────────────┘
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
           Allow / Restrict / Isolate
