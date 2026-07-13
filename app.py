import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="MECHXPERT",
    page_icon="⚙️",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#00c6ff,#0072ff,#7b2ff7);
}

.main-title{
font-size:55px;
font-weight:800;
text-align:center;
color:white;
margin-bottom:20px;
}

.card{
background:rgba(255,255,255,0.15);
padding:20px;
border-radius:20px;
text-align:center;
color:white;
box-shadow:0px 5px 20px rgba(0,0,0,0.3);
}

[data-testid="stSidebar"]{
background:linear-gradient(180deg,#ff512f,#dd2476);
}

h1,h2,h3,h4,p,label{
color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
"""
<div class='main-title'>
⚙️ MECHXPERT
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"<h3 style='text-align:center;color:white;'>Developed by Abdul Mannan</h3>",
unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================

menu = st.sidebar.selectbox(
    "Choose Module",
    [
        "Dashboard",
        "Unit Converter",
        "Material Database",
        "Stress Analysis",
        "Beam Deflection",
        "Power & Torque"
    ]
)

# =========================
# DASHBOARD
# =========================

if menu == "Dashboard":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='card'>
        <h2>6</h2>
        <p>Engineering Modules</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
        <h2>5</h2>
        <p>Materials</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='card'>
        <h2>PRO</h2>
        <p>Status</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Performance Analytics")

    df = pd.DataFrame({
        "Semester":[1,2,3,4,5,6],
        "Performance":[60,68,75,83,90,96]
    })

    fig = px.line(
        df,
        x="Semester",
        y="Performance",
        markers=True,
        title="Engineering Growth"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================
# UNIT CONVERTER
# =========================

elif menu == "Unit Converter":

    st.header("📏 Unit Converter")

    mm = st.number_input(
        "Length (mm)",
        value=1000.0
    )

    meters = mm / 1000
    inches = mm / 25.4

    st.success(f"Meters = {meters:.4f}")
    st.info(f"Inches = {inches:.4f}")

# =========================
# MATERIAL DATABASE
# =========================

elif menu == "Material Database":

    st.header("🔩 Material Database")

    materials = pd.DataFrame({
        "Material":[
            "Steel",
            "Aluminum",
            "Copper",
            "Titanium",
            "Cast Iron"
        ],
        "Density (kg/m³)":[
            7850,
            2700,
            8960,
            4500,
            7200
        ],
        "Young Modulus (GPa)":[
            210,
            69,
            110,
            116,
            170
        ]
    })

    st.dataframe(
        materials,
        use_container_width=True
    )

# =========================
# STRESS ANALYSIS
# =========================

elif menu == "Stress Analysis":

    st.header("📊 Stress Analysis")

    force = st.number_input(
        "Force (N)",
        value=1000.0
    )

    area = st.number_input(
        "Area (mm²)",
        value=100.0
    )

    stress = force / area

    st.success(
        f"Stress = {stress:.2f} MPa"
    )

# =========================
# BEAM DEFLECTION
# =========================

elif menu == "Beam Deflection":

    st.header("🏗 Beam Deflection")

    P = st.number_input(
        "Load (N)",
        value=1000.0
    )

    L = st.number_input(
        "Length (m)",
        value=1.0
    )

    E = st.number_input(
        "Young Modulus E (Pa)",
        value=210e9
    )

    I = st.number_input(
        "Moment of Inertia I (m⁴)",
        value=1e-6,
        format="%e"
    )

    delta = (P * (L**3)) / (48 * E * I)

    st.success(
        f"Deflection = {delta:.8f} m"
    )

# =========================
# POWER & TORQUE
# =========================

elif menu == "Power & Torque":

    st.header("⚡ Power & Torque")

    torque = st.number_input(
        "Torque (Nm)",
        value=100.0
    )

    rpm = st.number_input(
        "RPM",
        value=1500.0
    )

    power = (2 * np.pi * rpm * torque) / 60

    st.success(
        f"Power = {power/1000:.2f} kW"
    )
