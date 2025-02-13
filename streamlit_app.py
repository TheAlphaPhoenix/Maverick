import streamlit as st

# App Title and Overview
st.title("Crib Coaster")
st.markdown("""
**Project Overview:**  
Crib Coaster is a smart infant sleep monitoring app and connected device system that helps parents optimize their baby’s sleep by automatically adjusting crib rocking intensity, tracking sleep stages, monitoring vital signs, and providing environmental alerts. The paired device consists of a smart crib riser and orbital shaker mechanism (modeled after a 3D-printed bed riser and an orbital shaker) that fits under each leg of the crib to provide gentle, controlled motion based on real-time baby feedback.
""")

st.markdown("---")
st.markdown("### Core Features and Functionalities")
st.markdown("""
1. **Motion Detection & Crib Adjustment**  
   - Connects to the smart riser device to detect baby movements and adjust rocking speed, intensity, and duration.
   - Uses AI-based motion tracking to identify early waking signs and adjust rocking patterns to soothe the baby.
   - Allows parents to set customized rocking profiles.

2. **Parent Alert System (Vital Signs & Movement Monitoring)**  
   - Integrates non-contact vital signs monitoring (breathing rate, movement tracking).
   - Sends immediate alerts if the baby wakes unexpectedly, experiences irregular breathing, or shows sudden movements.
   - Allows manual or AI-driven adjustments to crib motion.

3. **Sleep Optimization & Environmental Monitoring**  
   - Monitors room temperature and humidity to ensure optimal sleep conditions.
   - Provides automated recommendations if conditions are outside the optimal range (65–72°F, 40–60% humidity).
   - Integrates with smart home devices (thermostats, humidifiers, fans).

4. **Sleep Tracking & Data Analytics**  
   - Records sleep duration and stages (light, deep, REM) using motion and sound analysis.
   - Generates daily/weekly sleep reports, including a sleep efficiency score.
   - Provides longitudinal data for developmental tracking and exportable reports for pediatrician visits.

5. **AI-Powered Sleep Coaching & Custom Recommendations**  
   - Offers tailored sleep coaching insights based on tracked data and infant age.
   - Helps establish healthy bedtime routines with suggestions for soothing techniques and nap schedules.

6. **Customizable Sleep Profiles & Parental Controls**  
   - Enables personalized sleep and motion preferences.
   - Supports manual overrides and preset soothing cycles.
   - Features a "Do Not Disturb" mode for uninterrupted monitoring.

7. **Healthcare & Research Integration**  
   - Allows data sharing with pediatricians for review of sleep and vital sign history.
   - Provides API integration for healthcare providers and researchers.
   - Meets HIPAA compliance for secure health data.
""")

st.markdown("---")

# Sidebar for User Role Selection
user_role = st.sidebar.selectbox(
    "Select User Type",
    ["Parent", "Healthcare Provider", "Administrator"]
)

st.sidebar.markdown("### Demo Navigation")
st.sidebar.markdown("This demo currently does not require a login but the functionality can be easily integrated later.")

# Display different dashboards based on user role selection
if user_role == "Parent":
    st.header("Parent User Dashboard")
    st.markdown("#### Motion Detection & Crib Adjustment")
    st.write("Automatically adjusts crib rocking based on baby movements. Customize your rocking profile to suit your baby's sleep patterns.")
    
    st.markdown("#### Parent Alert System")
    st.write("Receive real-time notifications for baby movements and vital signs such as breathing rate. Stay informed without constantly checking on your baby.")
    
    st.markdown("#### Sleep Tracking & Data Analytics")
    st.write("View detailed sleep reports that include sleep duration, sleep stages (light, deep, REM), and overall sleep efficiency. Use these reports during pediatrician visits.")
    
    st.markdown("#### AI-Powered Sleep Coaching")
    st.write("Get tailored sleep coaching insights and recommendations to establish healthy bedtime routines.")
    
elif user_role == "Healthcare Provider":
    st.header("Healthcare Provider Dashboard")
    st.markdown("#### Sleep Data Analytics")
    st.write("Access exportable reports on infant sleep duration, disruptions, and environmental conditions to support health assessments.")
    
    st.markdown("#### Vital Signs Monitoring")
    st.write("Review real-time data on infant breathing patterns and movements, helping identify any irregularities quickly.")
    
    st.markdown("#### Research & Data Integration")
    st.write("Utilize API integration to access aggregated, anonymized sleep data for research and clinical studies.")
    
elif user_role == "Administrator":
    st.header("Administrator Dashboard")
    st.markdown("#### System Configuration")
    st.write("Configure alert thresholds, adjust motion sensitivity, and manage integrations with smart home and healthcare systems.")
    
    st.markdown("#### User Management")
    st.write("Manage user roles and permissions. (Login functionality to be integrated in the future.)")
    
    st.markdown("#### Data Security & Compliance")
    st.write("Monitor data encryption, system backups, and ensure compliance with HIPAA and other regulatory requirements.")
    
    st.markdown("#### Reporting & Analytics")
    st.write("Generate and review system-wide performance reports to optimize system functionality.")

st.markdown("---")
st.markdown("### Technical Specifications Overview")
st.markdown("""
- **Device Integration:** 3D-printed with high-strength materials (e.g., polycarbonate, carbon fiber PETG) and a low-noise orbital shaker mechanism.
- **Connectivity:** Uses Wi-Fi/Bluetooth with an Arduino/Raspberry Pi Pico for sensor and motion control.
- **Backend & Frontend:** Secure backend (AWS/Firebase/Google Cloud) with a React Native mobile app.
- **AI/ML:** Powered by TensorFlow or OpenCV for motion and sleep tracking analysis.
- **Data Security:** End-to-end encryption and multi-factor authentication.
""")

st.markdown("### Next Steps")
st.markdown("""
1. **Prototype Development:** 3D-print the initial smart crib riser with integrated motion mechanisms.  
2. **Mobile App MVP:** Develop the initial version with motion control, sleep tracking, and environmental monitoring.  
3. **Beta Testing:** Gather real-world feedback from parents, healthcare providers, and administrators.  
4. **Iterate & Scale:** Refine algorithms and UI based on user feedback; prepare for scalable manufacturing.
""")
