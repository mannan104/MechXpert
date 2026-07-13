import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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
margin-bottom:0px;
text-shadow: 2px 2px 8px rgba(0,0,0,0.35);
}

.sub-title{
text-align:center;
color:#e8e8ff;
font-size:16px;
margin-bottom:25px;
}

.card{
background:rgba(255,255,255,0.15);
padding:20px;
border-radius:20px;
text-align:center;
color:white;
box-shadow:0px 5px 20px rgba(0,0,0,0.3);
border:1px solid rgba(255,255,255,0.25);
}

.card h2{
font-size:38px;
margin-bottom:5px;
}

.result-box{
background:rgba(255,255,255,0.12);
padding:18px 22px;
border-radius:16px;
border-left:6px solid #00e5ff;
color:white;
margin-top:10px;
margin-bottom:10px;
}

.formula-box{
background:rgba(0,0,0,0.25);
padding:14px 18px;
border-radius:12px;
color:#dff6ff;
font-family:monospace;
font-size:16px;
margin-top:8px;
}

.footer{
text-align:center;
color:rgba(255,255,255,0.7);
font-size:13px;
margin-top:40px;
padding-top:15px;
border-top:1px solid rgba(255,255,255,0.2);
}

[data-testid="stSidebar"]{
background:linear-gradient(180deg,#ff512f,#dd2476);
}

h1,h2,h3,h4,p,label,span{
color:white !important;
}

div[data-testid="stMetricValue"]{
color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("<div class='main-title'>⚙️ MECHXPERT</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>A Mechanical Engineering Toolkit — Developed by Abdul Mannan</div>", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.markdown("### 🧭 Navigation")

menu = st.sidebar.selectbox(
    "Choose Module",
    [
        "Dashboard",
        "Unit Converter",
        "Material Database",
        "Stress Analysis",
        "Beam Deflection",
        "Power & Torque",
        "Gear Ratio Calculator",
        "Fluid Flow (Reynolds Number)",
        "Thermal Efficiency"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **About MECHXPERT**

    A quick-reference calculator suite for
    core mechanical engineering concepts —
    statics, strength of materials, thermo,
    and fluid mechanics.
    """
)

MATERIALS = pd.DataFrame({
    "Material": ["Steel (Mild)", "Aluminum 6061", "Copper", "Titanium Ti-6Al-4V", "Cast Iron (Grey)"],
    "Density (kg/m³)": [7850, 2700, 8960, 4430, 7200],
    "Young Modulus (GPa)": [210, 69, 110, 114, 170],
    "Yield Strength (MPa)": [250, 276, 70, 880, 130],
    "Ultimate Strength (MPa)": [400, 310, 220, 950, 200]
})

# =========================
# DASHBOARD
# =========================

if menu == "Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='card'><h2>9</h2><p>Engineering Modules</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'><h2>{len(MATERIALS)}</h2><p>Materials in DB</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'><h2>PRO</h2><p>Status</p></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='card'><h2>2026</h2><p>Build Year</p></div>", unsafe_allow_html=True)

    st.markdown("## 📈 Performance Analytics")

    df = pd.DataFrame({
        "Semester": [1, 2, 3, 4, 5, 6],
        "Performance": [60, 68, 75, 83, 90, 96]
    })

    c1, c2 = st.columns([2, 1])

    with c1:
        fig = px.line(
            df, x="Semester", y="Performance",
            markers=True, title="Engineering Growth"
        )
        fig.update_traces(line_color="#00e5ff", line_width=3, marker=dict(size=10, color="white"))
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig2 = px.bar(
            MATERIALS, x="Material", y="Yield Strength (MPa)",
            title="Material Yield Strength", color="Yield Strength (MPa)",
            color_continuous_scale="Blues"
        )
        fig2.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            font_color="white", showlegend=False
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("## 🕸 Material Comparison Radar")
    categories = ["Density (kg/m³)", "Young Modulus (GPa)", "Yield Strength (MPa)", "Ultimate Strength (MPa)"]
    fig3 = go.Figure()
    for _, row in MATERIALS.iterrows():
        norm_vals = [row[c] / MATERIALS[c].max() * 100 for c in categories]
        fig3.add_trace(go.Scatterpolar(
            r=norm_vals + [norm_vals[0]],
            theta=categories + [categories[0]],
            fill='toself',
            name=row["Material"]
        ))
    fig3.update_layout(
        polar=dict(bgcolor="rgba(255,255,255,0.05)", radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True, paper_bgcolor="rgba(0,0,0,0)", font_color="white"
    )
    st.plotly_chart(fig3, use_container_width=True)

# =========================
# UNIT CONVERTER
# =========================

elif menu == "Unit Converter":

    st.header("📏 Unit Converter")

    conv_type = st.radio("Conversion Type", ["Length", "Force", "Pressure", "Torque"], horizontal=True)

    if conv_type == "Length":
        mm = st.number_input("Length (mm)", value=1000.0)
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"<div class='result-box'>Meters<br><b>{mm/1000:.4f} m</b></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='result-box'>Inches<br><b>{mm/25.4:.4f} in</b></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='result-box'>Feet<br><b>{mm/304.8:.4f} ft</b></div>", unsafe_allow_html=True)

    elif conv_type == "Force":
        n = st.number_input("Force (N)", value=1000.0)
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"<div class='result-box'>Kilonewtons<br><b>{n/1000:.4f} kN</b></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='result-box'>Pounds-force<br><b>{n/4.44822:.4f} lbf</b></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='result-box'>Kilogram-force<br><b>{n/9.80665:.4f} kgf</b></div>", unsafe_allow_html=True)

    elif conv_type == "Pressure":
        pa = st.number_input("Pressure (Pa)", value=1_000_000.0)
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"<div class='result-box'>MPa<br><b>{pa/1e6:.4f} MPa</b></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='result-box'>psi<br><b>{pa/6894.76:.4f} psi</b></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='result-box'>bar<br><b>{pa/1e5:.4f} bar</b></div>", unsafe_allow_html=True)

    elif conv_type == "Torque":
        nm = st.number_input("Torque (Nm)", value=100.0)
        c1, c2 = st.columns(2)
        c1.markdown(f"<div class='result-box'>lb-ft<br><b>{nm*0.737562:.4f} lb·ft</b></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='result-box'>lb-in<br><b>{nm*8.85075:.4f} lb·in</b></div>", unsafe_allow_html=True)

# =========================
# MATERIAL DATABASE
# =========================

elif menu == "Material Database":

    st.header("🔩 Material Database")
    st.dataframe(MATERIALS, use_container_width=True)

    fig = px.bar(
        MATERIALS, x="Material", y=["Yield Strength (MPa)", "Ultimate Strength (MPa)"],
        barmode="group", title="Yield vs Ultimate Strength"
    )
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# =========================
# STRESS ANALYSIS
# =========================

elif menu == "Stress Analysis":

    st.header("📊 Stress Analysis")

    col1, col2 = st.columns(2)
    with col1:
        force = st.number_input("Force (N)", value=1000.0)
        area = st.number_input("Area (mm²)", value=100.0)
        material_choice = st.selectbox("Compare against material", MATERIALS["Material"])

    stress = force / area
    yield_strength = MATERIALS.loc[MATERIALS["Material"] == material_choice, "Yield Strength (MPa)"].values[0]
    safety_factor = yield_strength / stress if stress > 0 else float("inf")

    with col2:
        st.markdown(f"<div class='result-box'>Applied Stress<br><b>{stress:.2f} MPa</b></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-box'>Yield Strength ({material_choice})<br><b>{yield_strength:.1f} MPa</b></div>", unsafe_allow_html=True)
        verdict = "✅ Safe" if safety_factor >= 1.5 else ("⚠️ Marginal" if safety_factor >= 1 else "❌ Unsafe")
        st.markdown(f"<div class='result-box'>Safety Factor<br><b>{safety_factor:.2f} — {verdict}</b></div>", unsafe_allow_html=True)

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=stress,
        title={'text': "Stress vs Yield Strength (MPa)"},
        gauge={
            'axis': {'range': [0, yield_strength * 1.5]},
            'bar': {'color': "#00e5ff"},
            'steps': [
                {'range': [0, yield_strength / 1.5], 'color': "rgba(0,255,150,0.3)"},
                {'range': [yield_strength / 1.5, yield_strength], 'color': "rgba(255,200,0,0.3)"},
                {'range': [yield_strength, yield_strength * 1.5], 'color': "rgba(255,0,0,0.3)"}
            ],
            'threshold': {'line': {'color': "red", 'width': 4}, 'value': yield_strength}
        }
    ))
    gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    st.plotly_chart(gauge, use_container_width=True)

    st.markdown("<div class='formula-box'>σ = F / A</div>", unsafe_allow_html=True)

# =========================
# BEAM DEFLECTION
# =========================

elif menu == "Beam Deflection":

    st.header("🏗 Beam Deflection")
    st.caption("Simply supported beam, central point load")

    col1, col2 = st.columns(2)
    with col1:
        P = st.number_input("Load (N)", value=1000.0)
        L = st.number_input("Length (m)", value=1.0)
        E = st.number_input("Young Modulus E (Pa)", value=210e9, format="%e")
        I = st.number_input("Moment of Inertia I (m⁴)", value=1e-6, format="%e")

    delta = (P * (L ** 3)) / (48 * E * I)

    with col2:
        st.markdown(f"<div class='result-box'>Max Deflection<br><b>{delta:.8f} m</b></div>", unsafe_allow_html=True)
        st.markdown("<div class='formula-box'>δ = P·L³ / (48·E·I)</div>", unsafe_allow_html=True)

    x = np.linspace(0, L, 100)
    y = (P * x * (3 * L**2 - 4 * x**2)) / (48 * E * I)
    y[x > L/2] = ((P * (L - x[x > L/2]) * (3 * L**2 - 4 * (L - x[x > L/2])**2)) / (48 * E * I))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=-y, mode="lines", line=dict(color="#00e5ff", width=3), name="Deflection shape"))
    fig.add_hline(y=0, line_dash="dash", line_color="white")
    fig.update_layout(
        title="Beam Deflection Shape", xaxis_title="Position along beam (m)", yaxis_title="Deflection (m)",
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white"
    )
    st.plotly_chart(fig, use_container_width=True)

# =========================
# POWER & TORQUE
# =========================

elif menu == "Power & Torque":

    st.header("⚡ Power & Torque")

    col1, col2 = st.columns(2)
    with col1:
        torque = st.number_input("Torque (Nm)", value=100.0)
        rpm = st.number_input("RPM", value=1500.0)

    power = (2 * np.pi * rpm * torque) / 60

    with col2:
        st.markdown(f"<div class='result-box'>Power<br><b>{power/1000:.2f} kW</b></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-box'>Power<br><b>{power/745.7:.2f} hp</b></div>", unsafe_allow_html=True)
        st.markdown("<div class='formula-box'>P = 2π·N·T / 60</div>", unsafe_allow_html=True)

    rpm_range = np.linspace(100, 5000, 50)
    power_range = (2 * np.pi * rpm_range * torque) / 60 / 1000

    fig = px.line(x=rpm_range, y=power_range, labels={"x": "RPM", "y": "Power (kW)"}, title="Power vs RPM at Fixed Torque")
    fig.update_traces(line_color="#00e5ff", line_width=3)
    fig.add_vline(x=rpm, line_dash="dash", line_color="yellow")
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# =========================
# GEAR RATIO CALCULATOR
# =========================

elif menu == "Gear Ratio Calculator":

    st.header("⚙️ Gear Ratio Calculator")

    col1, col2 = st.columns(2)
    with col1:
        t_driver = st.number_input("Driver Gear Teeth", value=20, step=1)
        t_driven = st.number_input("Driven Gear Teeth", value=60, step=1)
        input_rpm = st.number_input("Input Speed (RPM)", value=1000.0)

    ratio = t_driven / t_driver
    output_rpm = input_rpm / ratio

    with col2:
        st.markdown(f"<div class='result-box'>Gear Ratio<br><b>{ratio:.2f} : 1</b></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-box'>Output Speed<br><b>{output_rpm:.2f} RPM</b></div>", unsafe_allow_html=True)
        mode = "Speed Reduction / Torque Increase" if ratio > 1 else "Speed Increase / Torque Reduction"
        st.markdown(f"<div class='result-box'>Mode<br><b>{mode}</b></div>", unsafe_allow_html=True)

    st.markdown("<div class='formula-box'>Ratio = T_driven / T_driver &nbsp;&nbsp;|&nbsp;&nbsp; N_out = N_in / Ratio</div>", unsafe_allow_html=True)

# =========================
# FLUID FLOW - REYNOLDS NUMBER
# =========================

elif menu == "Fluid Flow (Reynolds Number)":

    st.header("🌊 Reynolds Number Calculator")

    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Fluid Density ρ (kg/m³)", value=1000.0)
        velocity = st.number_input("Velocity V (m/s)", value=2.0)
        diameter = st.number_input("Pipe Diameter D (m)", value=0.05)
        mu = st.number_input("Dynamic Viscosity μ (Pa·s)", value=0.001, format="%e")

    Re = (rho * velocity * diameter) / mu

    with col2:
        st.markdown(f"<div class='result-box'>Reynolds Number<br><b>{Re:,.1f}</b></div>", unsafe_allow_html=True)
        flow_regime = "Laminar" if Re < 2300 else ("Transitional" if Re < 4000 else "Turbulent")
        st.markdown(f"<div class='result-box'>Flow Regime<br><b>{flow_regime}</b></div>", unsafe_allow_html=True)
        st.markdown("<div class='formula-box'>Re = ρ·V·D / μ</div>", unsafe_allow_html=True)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=Re,
        title={'text': "Reynolds Number"},
        gauge={
            'axis': {'range': [0, max(6000, Re * 1.2)]},
            'bar': {'color': "#00e5ff"},
            'steps': [
                {'range': [0, 2300], 'color': "rgba(0,255,150,0.3)"},
                {'range': [2300, 4000], 'color': "rgba(255,200,0,0.3)"},
                {'range': [4000, max(6000, Re * 1.2)], 'color': "rgba(255,0,0,0.3)"}
            ]
        }
    ))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# =========================
# THERMAL EFFICIENCY
# =========================

elif menu == "Thermal Efficiency":

    st.header("🔥 Thermal Cycle Efficiency")

    cycle = st.selectbox("Select Cycle", ["Carnot", "Otto", "Diesel"])

    if cycle == "Carnot":
        Th = st.number_input("Hot Reservoir Temp Th (K)", value=800.0)
        Tc = st.number_input("Cold Reservoir Temp Tc (K)", value=300.0)
        eff = 1 - (Tc / Th)
        formula = "η = 1 − Tc/Th"

    elif cycle == "Otto":
        r = st.number_input("Compression Ratio r", value=8.0)
        gamma = st.number_input("Specific Heat Ratio γ", value=1.4)
        eff = 1 - (1 / (r ** (gamma - 1)))
        formula = "η = 1 − 1/r^(γ−1)"

    else:
        r = st.number_input("Compression Ratio r", value=18.0)
        rc = st.number_input("Cutoff Ratio rc", value=2.0)
        gamma = st.number_input("Specific Heat Ratio γ", value=1.4)
        eff = 1 - (1 / (gamma * (r ** (gamma - 1)))) * ((rc ** gamma - 1) / (rc - 1))
        formula = "η = 1 − [1/(γ·r^(γ−1))]·[(rc^γ−1)/(rc−1)]"

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='result-box'>Thermal Efficiency<br><b>{eff*100:.2f}%</b></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='formula-box'>{formula}</div>", unsafe_allow_html=True)

    with col2:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=eff * 100,
            title={'text': f"{cycle} Cycle Efficiency (%)"},
            gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#00e5ff"}}
        ))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")
        st.plotly_chart(fig, use_container_width=True)

# =========================
# FOOTER
# =========================

st.markdown(
    "<div class='footer'>MECHXPERT © 2026 — Developed by Abdul Mannan | Mechanical Engineering, UET Taxila</div>",
    unsafe_allow_html=True
)
