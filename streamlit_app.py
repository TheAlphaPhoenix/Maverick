import streamlit as st
import numpy as np
import pandas as pd

# -------------------------------------------
# Set up Streamlit page configuration
# -------------------------------------------
st.set_page_config(page_title="Crib Coaster", layout="wide")

# -------------------------------------------
# Project Overview Header
# -------------------------------------------
st.title("Crib Coaster")
st.markdown("""
### Project Overview
**Crib Coaster** is a smart infant sleep monitoring app and connected device system that helps parents optimize their baby’s sleep by:
- Automatically adjusting crib rocking intensity based on real-time baby feedback.
- Tracking sleep stages and vital signs.
- Providing environmental alerts.
- Integrating data with healthcare providers and pediatric consultations.

**Paired Device:** A smart crib riser and orbital shaker mechanism (modeled after a 3D-printed bed riser and orbital shaker) that fits under each leg of the crib to provide gentle, controlled motion based on real-time baby feedback.
""")
st.markdown("---")

# -------------------------------------------
# Sidebar: User Role Selection (No login required for demo)
# -------------------------------------------
user_role = st.sidebar.selectbox("Select User Role", ["Parent", "Healthcare Provider", "Administrator"])
st.sidebar.markdown("This demo currently does not require login. Authentication can be added later.")

# ============================================
# Parent Dashboard
# ============================================
if user_role == "Parent":
    st.header("Parent Dashboard")
    
    # Create tabs for Parent functionalities
    parent_tabs = st.tabs([
        "Motion & Crib Adjustment", 
        "Sleep Tracking & Analytics", 
        "AI Sleep Coaching", 
        "Rocking Profile Customization",
        "Environmental Monitoring"
    ])
    
    # ----- Tab 1: Motion Detection & Crib Adjustment -----
    with parent_tabs[0]:
        st.subheader("Motion Detection & Crib Adjustment")
        st.markdown("The app connects to the smart riser device to detect baby movements and adjust the rocking speed, intensity, and duration based on real-time data.\n\n*Uses AI-based motion tracking to identify early waking signs and adjust rocking patterns to soothe your baby.*")
        if st.button("Simulate Crib Motion Adjustment"):
            st.success("Crib rocking adjusted: Gentle rocking initiated based on detected baby movement.")
    
    # ----- Tab 2: Sleep Tracking & Data Analytics -----
    with parent_tabs[1]:
        st.subheader("Sleep Tracking & Data Analytics")
        st.markdown("Recording sleep duration and sleep stages (Light, Deep, REM) using motion and sound analysis.")
        # Simulated 24-hour sleep stage data
        times = pd.date_range("2023-01-01", periods=24, freq="H")
        sleep_stages = np.random.choice(["Light", "Deep", "REM"], size=24)
        sleep_df = pd.DataFrame({"Time": times, "Sleep Stage": sleep_stages})
        st.dataframe(sleep_df)
        st.markdown("**Sleep Stage Frequency:**")
        st.bar_chart(sleep_df["Sleep Stage"].value_counts())
    
    # ----- Tab 3: AI-Powered Sleep Coaching -----
    with parent_tabs[2]:
        st.subheader("AI-Powered Sleep Coaching")
        if st.button("Get Sleep Coaching Advice"):
            st.info("Advice: Establish a consistent bedtime routine, lower the rocking intensity as the baby enters deep sleep, and create a quiet, dim environment.")
    
    # ----- Tab 4: Rocking Profile Customization -----
    with parent_tabs[3]:
        st.subheader("Rocking Profile Customization")
        speed = st.slider("Set Rocking Speed", min_value=1, max_value=10, value=5)
        intensity = st.slider("Set Rocking Intensity", min_value=1, max_value=10, value=5)
        if st.button("Update Rocking Profile"):
            st.success(f"Profile updated: Speed = {speed}, Intensity = {intensity}.")
    
    # ----- Tab 5: Sleep Optimization & Environmental Monitoring -----
    with parent_tabs[4]:
        st.subheader("Environmental Monitoring")
        st.markdown("Monitors room temperature and humidity to ensure optimal sleep conditions.\n\nOptimal range: **65–72°F** and **40–60% humidity**.")
        temp = st.slider("Room Temperature (°F)", 60, 80, 70)
        humidity = st.slider("Room Humidity (%)", 20, 80, 50)
        if st.button("Check Environment"):
            if 65 <= temp <= 72 and 40 <= humidity <= 60:
                st.success("Optimal sleeping conditions detected.")
            else:
                st.warning("Conditions are not optimal. Consider adjusting the thermostat or humidifier.")

# ============================================
# Healthcare Provider Dashboard
# ============================================
elif user_role == "Healthcare Provider":
    st.header("Healthcare Provider Dashboard")
    
    # Create tabs for Provider functionalities
    provider_tabs = st.tabs([
        "Sleep Data Analytics", 
        "Vital Signs Monitoring", 
        "Export Reports", 
        "Research Integration"
    ])
    
    # ----- Tab 1: Sleep Data Analytics -----
    with provider_tabs[0]:
        st.subheader("Sleep Data Analytics")
        st.markdown("Review aggregated sleep data for infants. The chart below simulates sleep duration over the past week.")
        days = pd.date_range(end=pd.Timestamp.today(), periods=7)
        sleep_duration = np.random.randint(6, 12, size=7)
        sleep_data = pd.DataFrame({"Day": days, "Sleep Duration (hrs)": sleep_duration})
        st.line_chart(sleep_data.set_index("Day"))
    
    # ----- Tab 2: Vital Signs Monitoring -----
    with provider_tabs[1]:
        st.subheader("Vital Signs Monitoring")
        st.markdown("Monitor vital signs such as heart rate and breathing rate.")
        if st.button("Simulate Vital Signs Check"):
            heart_rate = np.random.randint(100, 140)
            breathing_rate = np.random.randint(30, 40)
            st.write(f"**Current Heart Rate:** {heart_rate} BPM")
            st.write(f"**Current Breathing Rate:** {breathing_rate} breaths per minute")
    
    # ----- Tab 3: Export Reports -----
    with provider_tabs[2]:
        st.subheader("Export Reports")
        if st.button("Generate Sleep Report"):
            st.success("Sleep report generated. [Download Report](#)")
            st.info("This report includes data on sleep duration, sleep stage distribution, and environmental conditions.")
    
    # ----- Tab 4: Research Integration -----
    with provider_tabs[3]:
        st.subheader("Research Integration")
        st.markdown("Provides API integration for healthcare providers and researchers to access aggregated, anonymized infant sleep data.")
        st.write("API details and aggregated data would be displayed here in a real implementation.")

# ============================================
# Administrator Dashboard
# ============================================
elif user_role == "Administrator":
    st.header("Administrator Dashboard")
    
    # Create tabs for Administrator functionalities
    admin_tabs = st.tabs([
        "System Configuration", 
        "User Management", 
        "Data Security & Compliance", 
        "Reporting & Analytics"
    ])
    
    # ----- Tab 1: System Configuration -----
    with admin_tabs[0]:
        st.subheader("System Configuration")
        st.markdown("Configure alert thresholds and motion sensitivity for the system.")
        alert_threshold = st.slider("Alert Threshold (Heart Rate BPM)", 80, 150, 120)
        motion_sensitivity = st.slider("Motion Sensitivity", 1, 10, 5)
        if st.button("Update System Settings"):
            st.success(f"Settings updated: Alert Threshold = {alert_threshold} BPM, Motion Sensitivity = {motion_sensitivity}.")
    
    # ----- Tab 2: User Management -----
    with admin_tabs[1]:
        st.subheader("User Management")
        st.markdown("Manage user roles and permissions. (Login integration will be added in future versions.)")
        if st.button("Simulate Adding a New User"):
            st.success("New user added (simulation).")
    
    # ----- Tab 3: Data Security & Compliance -----
    with admin_tabs[2]:
        st.subheader("Data Security & Compliance")
        if st.button("View Data Security Logs"):
            st.write("Data Security Logs: All systems operational. No breaches detected.")
    
    # ----- Tab 4: Reporting & Analytics -----
    with admin_tabs[3]:
        st.subheader("Reporting & Analytics")
        if st.button("Generate System Performance Report"):
            st.write("System performance report generated (simulation).")

# -------------------------------------------
# Technical Specifications and Next Steps
# -------------------------------------------
st.markdown("---")
st.markdown("### Technical Specifications Overview")
st.markdown("""
- **Device Integration:** 3D-printed with high-strength materials (e.g., polycarbonate, carbon fiber PETG) with a low-noise orbital shaker mechanism.
- **Connectivity:** Utilizes Wi-Fi/Bluetooth with an Arduino/Raspberry Pi Pico for sensor and motion control.
- **Backend & Frontend:** Secure backend (AWS/Firebase/Google Cloud) paired with a React Native mobile app.
- **AI/ML Integration:** Powered by TensorFlow/OpenCV for motion and sleep tracking analysis.
- **Data Security:** End-to-end encryption and multi-factor authentication.
""")
st.markdown("### Next Steps")
st.markdown("""
1. **Prototype Development:** 3D-print the initial smart crib riser with integrated motion mechanisms.
2. **Mobile App MVP:** Develop the initial version with motion control, sleep tracking, and environmental monitoring.
3. **Beta Testing:** Gather real-world feedback from parents, healthcare providers, and administrators.
4. **Iteration & Scaling:** Refine algorithms and UI based on user feedback; prepare for scalable production.
""")



