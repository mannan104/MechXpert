import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Mechanical Engineering Suite",
    page_icon="⚙️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#00c6ff,#0072ff,#7b2ff7);
}

.main-title{
    font-size:50px;
    font-weight:bold;
    text-align:center;
    color:white;
}

.card{
    background:rgba(255,255,255,0.15);
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
}

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#ff512f,#dd2476);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>⚙️ Abdul Mannan Mechanical Engineering Suite</div>", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Dashboard",
        "Unit Converter",
        "Material Database",
        "Stress Calculator",
        "Beam Deflection",
        "Power & Torque"
    ]
)

# Dashboard
if menu == "Dashboard":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h2>6</h2><p>Modules</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h2>5</h2><p>Materials</p></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h2>PRO</h2><p>Status</p></div>", unsafe_allow_html=True)

    st.markdown("### Engineering Analytics")

    df = pd.DataFrame({
        "Week":[1,2,3,4,5],
        "Performance":[60,70,82,88,95]
    })

    fig = px.line(
        df,
        x="Week",
        y="Performance",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

# Unit Converter
elif menu == "Unit Converter":

    st.header("📏 Unit Converter")

    mm = st.number_input("Length (mm)", value=1000.0)

    meters = mm / 1000
    inches = mm / 25.4

    st.success(f"Meters: {meters:.4f}")
    st.info(f"Inches: {inches:.4f}")

# Material Database
elif menu == "Material Database":

    st.header("🔩 Material Database")

    materials = pd.DataFrame({
        "Material":["Steel","Aluminum","Copper","Titanium","Cast Iron"],
        "Density (kg/m³)":[7850,2700,8960,4500,7200],
        "Young Modulus (GPa)":[210,69,110,116,170]
    })

    st.dataframe(materials, use_container_width=True)

# Stress Calculator
elif menu == "Stress Calculator":

    st.header("📊 Stress Calculator")

    force = st.number_input("Force (N)", value=1000.0)
    area = st.number_input("Area (mm²)", value=100.0)

    stress = force / area

    st.success(f"Stress = {stress:.2f} MPa")

# Beam Deflection
elif menu == "Beam Deflection":

    st.header("🏗 Beam Deflection")

    P = st.number_input("Load P (N)", value=1000.0)
    L = st.number_input("Length L (m)", value=1.0)
    E = st.number_input("Young's Modulus E (Pa)", value=210e9)
    I = st.number_input("Moment of Inertia I (m⁴)", value=1e-6)

    delta = (P * L**3)/(48 * E * I)

    st.success(f"Deflection = {delta:.8f} m")

# Power & Torque
elif menu == "Power & Torque":

    st.header("⚡ Power & Torque")

    torque = st.number_input("Torque (Nm)", value=100.0)
    rpm = st.number_input("Speed (RPM)", value=1500.0)

    power = (2*np.pi*rpm*torque)/60

    st.success(f"Power = {power/1000:.2f} kW")
