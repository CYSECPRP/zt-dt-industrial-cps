import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

# Import Custom Modules
from utils.preprocess import get_simulated_stream
from utils.attack_injector import inject_anomaly
from framework.digital_twin.dt_core import DigitalTwin
from framework.zero_trust_engine.zt_policy import ZeroTrustPolicyEngine

# ---------------------------------------------------------
# 1. Page Configuration & Custom CSS
# ---------------------------------------------------------
st.set_page_config(page_title="ZT-DT Enterprise SOC", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for a dark, sleek enterprise look
st.markdown("""
    <style>
    .metric-card {
        background-color: #1E1E1E;
        border-left: 5px solid #00B4D8;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    .metric-card-alert {
        border-left: 5px solid #FF4B4B;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. Session State Initialization
# ---------------------------------------------------------
if 'running' not in st.session_state:
    st.session_state.running = False
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["Timestamp", "Node", "Anomaly_Score", "Trust_Score", "Action", "Flow", "Pressure"])
if 'force_attack' not in st.session_state:
    st.session_state.force_attack = False

# Persistent Models
if "dt_model" not in st.session_state:
    st.session_state.dt_model = DigitalTwin()
if "ztp_engine" not in st.session_state:
    st.session_state.ztp_engine = ZeroTrustPolicyEngine()
if "stream" not in st.session_state:
    st.session_state.stream = get_simulated_stream(num_steps=1000000)

# ---------------------------------------------------------
# 3. Sidebar Command Center
# ---------------------------------------------------------
with st.sidebar:
    st.title("Command Center")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start", type="primary"):
            st.session_state.running = True
    with col2:
        if st.button("Stop"):
            st.session_state.running = False
            
    if st.button("INJECT TARGETED ATTACK", type="primary", use_container_width=True):
        st.session_state.force_attack = True
        
    if st.button("Reset Environment"):
        st.session_state.history = pd.DataFrame(columns=["Timestamp", "Node", "Anomaly_Score", "Trust_Score", "Action", "Flow", "Pressure"])
        st.session_state.dt_model = DigitalTwin()
        st.session_state.ztp_engine = ZeroTrustPolicyEngine()
        st.session_state.stream = get_simulated_stream(num_steps=1000000)
        st.session_state.running = False
        st.rerun()

    st.markdown("---")
    st.caption("Simulation Settings")
    sim_speed = st.slider("Tick Rate (Seconds)", 0.1, 2.0, 1.0)

# ---------------------------------------------------------
# 4. Main Dashboard Header
# ---------------------------------------------------------
st.title("Zero Trust-Enabled Digital Twin (ZT-DT)")
st.markdown("Real-Time Anomaly Detection for Industrial Cyber-Physical Systems")

# ---------------------------------------------------------
# 5. Data Generation Logic (Integrated with Core Pipeline)
# ---------------------------------------------------------
if st.session_state.running:
    try:
        data = next(st.session_state.stream)
    except StopIteration:
        st.session_state.stream = get_simulated_stream(num_steps=1000000)
        data = next(st.session_state.stream)
        
    current_time = datetime.now().strftime("%H:%M:%S")
    is_attack = st.session_state.force_attack
    
    if is_attack:
        data = inject_anomaly(data)
        st.session_state.force_attack = False # Reset immediately
        
    # Evaluate Pipeline natively relying on dt_core and zt_policy
    a_score = st.session_state.dt_model.evaluate(data)
    t_score, action = st.session_state.ztp_engine.calculate_trust(a_score)
    
    flow = data.get("flow_rate", 0.0)
    pressure = data.get("pressure", 0.0)
    
    new_row = {"Timestamp": current_time, "Node": "PLC_1", "Anomaly_Score": a_score, 
                "Trust_Score": t_score, "Action": action, "Flow": flow, "Pressure": pressure}
    
    st.session_state.history = pd.concat([st.session_state.history, pd.DataFrame([new_row])], ignore_index=True)
    
    # Keep only last 50 points to prevent memory bloat
    if len(st.session_state.history) > 50:
        st.session_state.history = st.session_state.history.iloc[-50:]

df = st.session_state.history

# ---------------------------------------------------------
# 6. Render UI if History Exists
# ---------------------------------------------------------
if not df.empty:
    last_action = df['Action'].iloc[-1]
    last_t_score = df['Trust_Score'].iloc[-1]
    last_a_score = df['Anomaly_Score'].iloc[-1]
    
    # Calculate Trust Delta
    delta_t = 0.00
    if len(df) > 1:
        delta_t = last_t_score - df['Trust_Score'].iloc[-2]

    # --- Render KPIs ---
    k1, k2, k3, k4 = st.columns(4)
    status_color = "normal" if last_action == "ALLOW" else "off" if last_action == "RESTRICT" else "inverse"
    k1.metric("System Status", "SECURE" if last_action == "ALLOW" else "BREACH DETECTED", delta="Normal" if last_action == "ALLOW" else "-Critical", delta_color=status_color)
    k2.metric("Active Node Trust", f"{last_t_score:.4f}", delta=f"{delta_t:.4f}")
    k3.metric("Anomaly Probability", f"{float(last_a_score):.0%}")
    k4.metric("ZTP Enforcement", last_action)

    st.markdown("---")

    # --- Render Tabs & Charts ---
    tab1, tab2, tab3 = st.tabs(["Live Monitoring", "CPS Topology", "Audit Logs"])
    
    with tab1:
        # Advanced Plotly Subplot
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # Trust Line
        fig.add_trace(go.Scatter(x=df["Timestamp"], y=df["Trust_Score"], name="Trust Score",
                                    line=dict(color="#00B4D8", width=3), fill='tozeroy', fillcolor='rgba(0, 180, 216, 0.1)'),
                        secondary_y=False)
        
        # Anomaly Line
        fig.add_trace(go.Scatter(x=df["Timestamp"], y=df["Anomaly_Score"], name="Anomaly Score",
                                    line=dict(color="#FF4B4B", width=2, dash='dot')),
                        secondary_y=False)
        
        # Sensor Data (Flow) on secondary Y axis
        fig.add_trace(go.Scatter(x=df["Timestamp"], y=df["Flow"], name="Sensor Flow Rate",
                                    line=dict(color="#38B000", width=1)),
                        secondary_y=True)

        fig.update_layout(title="Zero Trust Evaluation Engine", height=450, 
                            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=40, b=0),
                            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        fig.update_yaxes(title_text="Score (0.0 - 1.0)", range=[0, 1.05], secondary_y=False)
        fig.update_yaxes(title_text="Flow Rate", secondary_y=True)
        
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("### Industrial Network Status")
        st.info(f"**PLC_1 Status:** Currently operating under **{last_action}** protocol.")
        st.progress(last_t_score, text=f"Node Trust Level: {last_t_score:.2f}")

    with tab3:
        st.markdown("### Zero Trust Policy Logs")
        
        # Style Pandas dataframe map logic
        def highlight_action(action_val):
            if action_val == 'ISOLATE':
                return 'background-color: rgba(255, 75, 75, 0.3)'
            elif action_val == 'RESTRICT':
                return 'background-color: rgba(255, 204, 0, 0.3)'
            return ''
            
        try:
            styled_df = df.tail(10).style.map(highlight_action, subset=['Action'])
        except AttributeError:
            # Fallback for older pandas versions
            styled_df = df.tail(10).style.applymap(highlight_action, subset=['Action'])
            
        st.dataframe(styled_df, use_container_width=True)
        
else:
    st.info("No data simulated yet. Click 'Start' to begin streaming real-time telemetry from the Digital Twin engine.")

# ---------------------------------------------------------
# 7. Render Engine Loop (Uses Streamlit's architecture safely)
# ---------------------------------------------------------
if st.session_state.running:
    time.sleep(sim_speed)
    st.rerun()