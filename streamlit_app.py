import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Crib Coaster", layout="wide")

# App Title and Overview
st.title("Crib Coaster")
st.markdown("""
**Crib Coaster** is a smart infant sleep monitoring app and connected device system that helps parents optimize their baby’s sleep by:
- Automatically adjusting crib rocking intensity based on real-time baby feedback.
- Tracking sleep stages and vital signs.
- Providing environmental alerts.
- Integrating data with healthcare providers and pediatric consultations.

The paired device consists of a smart crib riser and orbital shaker mechanism (modeled after a 3D-printed bed riser and orbital shaker) that fits under each leg of the crib.
""")
st.markdown("---")

# Sidebar: User Role Selection
user_role = st.sidebar.selectbox(
    "Select User Type",
    ["Parent", "Healthcare Provider", "Administrator"]
)

st.sidebar.markdown("This demo does not require login. Future updates will integrate authentication.")

# =======================================
# Parent Dashboard
# =======================================
if user_role == "Parent":
    st.header("Parent Dashboard")
    
    tabs = st.tabs(["Motion & Crib Adjustment", "Sleep Tracking", "AI Sleep Coaching", "Rocking Profile Customization"])
    
    # Tab 1: Motion Detection & Crib Adjustment
    with tabs[0]:
        st.subheader("Motion Detection & Crib Adjustment")
        if st.button("Simulate Crib Motion Adjustment"):
            st.success("Crib rocking adjusted: Gentle rocking initiated based on detected baby movement.")
        st.info("This feature uses AI-based motion tracking to detect early waking signs and adjust rocking patterns accordingly.")
    
    # Tab 2: Sleep Tracking & Data Analytics
    with tabs[1]:
        st.subheader("Sleep Tracking & Data Analytics")
        st.write("Simulated sleep data for the past 24 hours:")
        # Simulate sleep stages data
        times = pd.date_range("2023-01-01", periods=24, freq="H")
        sleep_stages = np.random.choice(["Light", "Deep", "REM"], size=24)
        sleep_data = pd.DataFrame({"Time": times, "Sleep Stage": sleep_stages})
        st.dataframe(sleep_data)
        
        # Plot sleep stage frequency
        stage_counts = sleep_data["Sleep Stage"].value_counts()
        st.bar_chart(stage_counts)
    
    # Tab 3: AI-Powered Sleep Coaching
    with tabs[2]:
        st.subheader("AI-Powered Sleep Coaching")
        if st.button("Generate Sleep Coaching Advice"):
            st.write("Based on your baby's recent sleep patterns, we recommend a quiet, dim environment and a consistent bedtime routine. Consider lowering the rocking intensity gradually as your baby transitions into deep sleep.")
    
    # Tab 4: Customize Rocking Profile
    with tabs[3]:
        st.subheader("Customize Rocking Profile")
        rocking_speed = st.slider("Set Rocking Speed", min_value=1, max_value=10, value=5)
        rocking_intensity = st.slider("Set Rocking Intensity", min_value=1, max_value=10, value=5)
        if st.button("Update Rocking Profile"):
            st.success(f"Profile updated: Speed = {rocking_speed} and Intensity = {rocking_intensity}.")

# =======================================
# Healthcare Provider Dashboard
# =======================================
elif user_role == "Healthcare Provider":
    st.header("Healthcare Provider Dashboard")
    
    tabs = st.tabs(["Sleep Data Analytics", "Vital Signs Monitoring", "Export Reports"])
    
    # Tab 1: Sleep Data Analytics
    with tabs[0]:
        st.subheader("Sleep Data Analytics")
        # Simulate sleep duration data for a week
        days = pd.date_range(end=pd.Timestamp.today(), periods=7)
        sleep_duration = np.random.randint(5, 12, size=7)
        sleep_df = pd.DataFrame({"Day": days, "Sleep Duration (hrs)": sleep_duration})
        st.line_chart(sleep_df.set_index("Day"))
        st.write("Simulated sleep duration over the past week.")
    
    # Tab 2: Vital Signs Monitoring
    with tabs[1]:
        st.subheader("Vital Signs Monitoring")
        if st.button("Simulate Vital Signs Check"):
            heart_rate = np.random.randint(100, 140)
            breathing_rate = np.random.randint(30, 40)
            st.write(f"Current Heart Rate: **{heart_rate} BPM**")
            st.write(f"Current Breathing Rate: **{breathing_rate} breaths per minute**")
    
    # Tab 3: Export Reports
    with tabs[2]:
        st.subheader("Export Sleep Report")
        if st.button("Generate Sleep Report"):
            st.write("Sleep report generated. [Download Report](#)")
            st.info("This report includes data on sleep duration, sleep stage distribution, and environmental conditions.")

# =======================================
# Administrator Dashboard
# =======================================
elif user_role == "Administrator":
    st.header("Administrator Dashboard")
    
    tabs = st.tabs(["System Configuration", "User Management", "Data Security", "Reporting & Analytics"])
    
    # Tab 1: System Configuration
    with tabs[0]:
        st.subheader("System Configuration")
        alert_threshold = st.slider("Alert Threshold (Heart Rate BPM)", min_value=80, max_value=150, value=120)
        motion_sensitivity = st.slider("Motion Sensitivity", min_value=1, max_value=10, value=5)
        if st.button("Update System Settings"):
            st.success(f"Settings updated: Alert Threshold = {alert_threshold} BPM, Motion Sensitivity = {motion_sensitivity}.")
    
    # Tab 2: User Management
    with tabs[1]:
        st.subheader("User Management")
        st.write("User management functionalities will be integrated with login features in the future.")
        if st.button("Simulate Adding a New User"):
            st.success("New user added (simulation).")
    
    # Tab 3: Data Security & Compliance
    with tabs[2]:
        st.subheader("Data Security & Compliance")
        if st.button("View Data Security Logs"):
            st.write("Data Security Logs: All systems operational. No breaches detected.")
    
    # Tab 4: Reporting & Analytics
    with tabs[3]:
        st.subheader("Reporting & Analytics")
        if st.button("Generate System Performance Report"):
            st.write("System performance report generated (simulation).")

st.markdown("---")
st.markdown("### Technical Specifications Overview")
st.markdown("""
- **Device Integration:** 3D-printed with high-strength materials (polycarbonate, carbon fiber PETG) with a low-noise orbital shaker mechanism.
- **Connectivity:** Utilizes Wi-Fi/Bluetooth with an Arduino/Raspberry Pi Pico for sensor and motion control.
- **Backend & Frontend:** Secure backend (AWS/Firebase/Google Cloud) paired with a React Native mobile app.
- **AI/ML:** Powered by TensorFlow/OpenCV for motion and sleep tracking analysis.
- **Data Security:** End-to-end encryption and multi-factor authentication.
""")
st.markdown("### Next Steps")
st.markdown("""
1. **Prototype Development:** 3D-print the initial smart crib riser with integrated motion mechanisms.
2. **Mobile App MVP:** Develop the initial version with motion control, sleep tracking, and environmental monitoring.
3. **Beta Testing:** Gather real-world feedback from parents, healthcare providers, and administrators.
4. **Iteration & Scaling:** Refine algorithms and UI based on user feedback; prepare for scalable production.
""")

