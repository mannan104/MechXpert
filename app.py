import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

st.set_page_config(
    page_title="MECHXPERT",
    page_icon="⚙️",
    layout="wide"
)

MENU_SHEETS = {
    "Dashboard": "01",
    "Unit Converter": "02",
    "Material Database": "03",
    "Stress Analysis": "04",
    "Beam Deflection": "05",
    "Power & Torque": "06",
    "Gear Ratio Calculator": "07",
    "Fluid Flow (Reynolds Number)": "08",
    "Thermal Efficiency": "09",
}

# =========================
# CUSTOM CSS — Blueprint / Drafting Sheet identity
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&family=Inter:wght@400;500;700&display=swap');

:root{
  --navy: #0A1930;
  --panel: #12294A;
  --panel-light: #1B3A63;
  --cyan: #00D9FF;
  --orange: #FF6B35;
  --green: #39FF6A;
  --amber: #FFD60A;
  --red: #FF3B30;
  --ink: #F5F7FA;
}

.stApp{
background-color: var(--navy);
background-image:
  linear-gradient(rgba(0,217,255,0.06) 1px, transparent 1px),
  linear-gradient(90deg, rgba(0,217,255,0.06) 1px, transparent 1px);
background-size: 32px 32px;
}

html, body, [class*="css"]{
font-family: 'Inter', sans-serif;
}

/* ---------- Header / Title Block ---------- */

.drafting-header{
border: 2px solid var(--cyan);
border-radius: 4px;
padding: 22px 30px;
margin-bottom: 26px;
background: linear-gradient(135deg, rgba(0,217,255,0.05), rgba(255,107,53,0.05));
position: relative;
}

.drafting-header::before{
content: "";
position: absolute;
top: 6px; left: 6px; right: 6px; bottom: 6px;
border: 1px dashed rgba(0,217,255,0.35);
border-radius: 2px;
pointer-events: none;
}

.eyebrow{
font-family: 'JetBrains Mono', monospace;
letter-spacing: 4px;
font-size: 12px;
color: var(--orange) !important;
font-weight: 600;
margin-bottom: 6px;
}

.main-title{
font-family: 'JetBrains Mono', monospace;
font-size: 46px;
font-weight: 800;
color: var(--ink) !important;
margin: 0;
letter-spacing: 2px;
}

.main-title .accent{ color: var(--cyan) !important; }

.sub-title{
color: rgba(245,247,250,0.75) !important;
font-size: 15px;
margin-top: 6px;
font-family: 'Inter', sans-serif;
}

/* ---------- Sheet label per module ---------- */

.sheet-label{
font-family: 'JetBrains Mono', monospace;
color: var(--cyan) !important;
font-size: 13px;
letter-spacing: 3px;
border-bottom: 1px solid rgba(0,217,255,0.3);
padding-bottom: 10px;
margin-bottom: 20px;
}

/* ---------- Cards ---------- */

.card{
background: var(--panel);
padding: 22px 16px;
border-radius: 6px;
text-align: center;
color: var(--ink);
border: 1px solid rgba(0,217,255,0.35);
border-top: 4px solid var(--orange);
position: relative;
}

.card::after{
content: "";
position: absolute;
top: 8px; right: 8px;
width: 10px; height: 10px;
border-top: 2px solid var(--cyan);
border-right: 2px solid var(--cyan);
}

.card h2{
font-family: 'JetBrains Mono', monospace;
font-size: 34px;
margin-bottom: 4px;
color: var(--cyan) !important;
}

.card p{
color: rgba(245,247,250,0.7) !important;
font-size: 12px;
letter-spacing: 1px;
text-transform: uppercase;
margin: 0;
}

/* ---------- Result / formula boxes ---------- */

.result-box{
background: var(--panel);
padding: 16px 20px;
border-radius: 6px;
border-left: 5px solid var(--orange);
color: var(--ink);
margin-top: 10px;
margin-bottom: 10px;
font-family: 'Inter', sans-serif;
}

.result-box b{
font-family: 'JetBrains Mono', monospace;
color: var(--cyan) !important;
font-size: 18px;
}

.formula-box{
background: rgba(0,0,0,0.35);
padding: 14px 18px;
border-radius: 6px;
color: var(--amber) !important;
font-family: 'JetBrains Mono', monospace;
font-size: 15px;
margin-top: 8px;
border: 1px dashed rgba(255,214,10,0.4);
}

/* ---------- Gauges ---------- */

.gauge-wrap{
background: var(--panel);
border: 1px solid rgba(0,217,255,0.3);
border-radius: 6px;
padding: 16px 20px;
margin-top: 10px;
margin-bottom: 10px;
}

.gauge-wrap b{
font-family: 'JetBrains Mono', monospace;
color: var(--ink) !important;
font-size: 14px;
}

.gauge-track{
width: 100%;
height: 20px;
background: rgba(0,0,0,0.4);
border-radius: 3px;
overflow: hidden;
margin-top: 10px;
border: 1px solid rgba(0,217,255,0.25);
}

.gauge-fill{
height: 100%;
}

/* ---------- Sidebar ---------- */

[data-testid="stSidebar"]{
background: linear-gradient(180deg, #071527, #0A1930);
border-right: 2px solid var(--orange);
}

[data-testid="stSidebar"] h3{
font-family: 'JetBrains Mono', monospace;
color: var(--orange) !important;
letter-spacing: 2px;
font-size: 15px;
}

/* ---------- General text ---------- */

h1,h2,h3,h4,p,label,span,div{
color: var(--ink);
}

h2, h3{
font-family: 'JetBrains Mono', monospace;
}

div[data-testid="stMetricValue"]{
color: var(--cyan) !important;
font-family: 'JetBrains Mono', monospace;
}

/* ---------- Title block (footer signature) ---------- */

.title-block{
margin-top: 40px;
border: 2px solid var(--cyan);
border-radius: 4px;
overflow: hidden;
font-family: 'JetBrains Mono', monospace;
font-size: 12px;
}

.title-block-row{
display: flex;
border-top: 1px solid rgba(0,217,255,0.3);
}

.title-block-row:first-child{ border-top: none; }

.tb-cell{
flex: 1;
padding: 8px 14px;
border-right: 1px solid rgba(0,217,255,0.3);
}

.tb-cell:last-child{ border-right: none; }

.tb-label{
color: var(--orange) !important;
letter-spacing: 1px;
font-size: 10px;
display: block;
}

.tb-value{
color: var(--ink) !important;
font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


def gauge(label, value, max_value, unit="", zones=None):
    """Render a color-coded HTML/CSS gauge bar (no external plotting library)."""
    pct = max(0.0, min(1.0, value / max_value)) if max_value > 0 else 0.0

    if zones is None:
        color = "var(--cyan)"
    else:
        color = zones[-1][1]
        for upper, zone_color in zones:
            if value <= upper:
                color = zone_color
                break

    st.markdown(f"""
    <div class='gauge-wrap'>
        <b>{label}: {value:,.2f} {unit}</b>
        <div class='gauge-track'>
            <div class='gauge-fill' style='width:{pct*100:.1f}%; background:{color};'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def sheet_label(name):
    st.markdown(
        f"<div class='sheet-label'>SHEET {MENU_SHEETS[name]} / {len(MENU_SHEETS):02d} — {name.upper()}</div>",
        unsafe_allow_html=True
    )


def title_block(module_name):
    today = date.today().strftime("%d %b %Y")
    st.markdown(f"""
    <div class='title-block'>
        <div class='title-block-row'>
            <div class='tb-cell'><span class='tb-label'>DRAWN BY</span><span class='tb-value'>ABDUL MANNAN</span></div>
            <div class='tb-cell'><span class='tb-label'>PROJECT</span><span class='tb-value'>MECHXPERT TOOLKIT</span></div>
            <div class='tb-cell'><span class='tb-label'>SHEET</span><span class='tb-value'>{MENU_SHEETS[module_name]} OF {len(MENU_SHEETS):02d}</span></div>
        </div>
        <div class='title-block-row'>
            <div class='tb-cell'><span class='tb-label'>DATE</span><span class='tb-value'>{today}</span></div>
            <div class='tb-cell'><span class='tb-label'>SCALE</span><span class='tb-value'>NOT TO SCALE</span></div>
            <div class='tb-cell'><span class='tb-label'>REV</span><span class='tb-value'>2026.1</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# HEADER
# =========================

st.markdown("""
<div class='drafting-header'>
    <div class='eyebrow'>MECHANICAL ENGINEERING TOOLKIT · DRAFT SHEET SERIES</div>
    <div class='main-title'>⚙ MECH<span class='accent'>X</span>PERT</div>
    <div class='sub-title'>Calculation suite for statics, strength of materials, thermodynamics &amp; fluid mechanics — Developed by Abdul Mannan</div>
</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.markdown("### ▣ CONTROL PANEL")

menu = st.sidebar.selectbox(
    "SELECT MODULE",
    list(MENU_SHEETS.keys())
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style='font-family:JetBrains Mono, monospace; font-size:12px; color:rgba(245,247,250,0.75); line-height:1.6;'>
    <b style='color:#FF6B35;'>ABOUT</b><br>
    A quick-reference calculator suite<br>
    for core mechanical engineering<br>
    concepts — statics, strength of<br>
    materials, thermo, and fluids.
    </div>
    """,
    unsafe_allow_html=True
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
    sheet_label(menu)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='card'><h2>9</h2><p>Modules</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'><h2>{len(MATERIALS)}</h2><p>Materials in DB</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'><h2>PRO</h2><p>Status</p></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='card'><h2>2026</h2><p>Build Year</p></div>", unsafe_allow_html=True)

    st.markdown("#### ▸ PERFORMANCE ANALYTICS")

    df = pd.DataFrame({
        "Semester": [1, 2, 3, 4, 5, 6],
        "Performance": [60, 68, 75, 83, 90, 96]
    }).set_index("Semester")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("**Engineering Growth by Semester**")
        st.line_chart(df, use_container_width=True, color="#00D9FF")

    with c2:
        st.markdown("**Material Yield Strength (MPa)**")
        bar_df = MATERIALS.set_index("Material")[["Yield Strength (MPa)"]]
        st.bar_chart(bar_df, use_container_width=True, color="#FF6B35")

    st.markdown("#### ▸ MATERIAL COMPARISON")
    compare_df = MATERIALS.set_index("Material")[
        ["Young Modulus (GPa)", "Yield Strength (MPa)", "Ultimate Strength (MPa)"]
    ]
    st.bar_chart(compare_df, use_container_width=True, color=["#00D9FF", "#FF6B35", "#39FF6A"])

    title_block(menu)

# =========================
# UNIT CONVERTER
# =========================

elif menu == "Unit Converter":
    sheet_label(menu)

    conv_type = st.radio("CONVERSION TYPE", ["Length", "Force", "Pressure", "Torque"], horizontal=True)

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

    title_block(menu)

# =========================
# MATERIAL DATABASE
# =========================

elif menu == "Material Database":
    sheet_label(menu)

    st.dataframe(MATERIALS, use_container_width=True)

    st.markdown("**Yield vs Ultimate Strength (MPa)**")
    chart_df = MATERIALS.set_index("Material")[["Yield Strength (MPa)", "Ultimate Strength (MPa)"]]
    st.bar_chart(chart_df, use_container_width=True, color=["#FF6B35", "#00D9FF"])

    title_block(menu)

# =========================
# STRESS ANALYSIS
# =========================

elif menu == "Stress Analysis":
    sheet_label(menu)

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
        verdict = "SAFE" if safety_factor >= 1.5 else ("MARGINAL" if safety_factor >= 1 else "UNSAFE")
        st.markdown(f"<div class='result-box'>Safety Factor<br><b>{safety_factor:.2f} — {verdict}</b></div>", unsafe_allow_html=True)

    gauge(
        "Applied Stress vs Yield Strength", stress, yield_strength * 1.5, unit="MPa",
        zones=[(yield_strength/1.5, "#39FF6A"), (yield_strength, "#FFD60A"), (yield_strength*1.5, "#FF3B30")]
    )

    st.markdown("<div class='formula-box'>σ = F / A</div>", unsafe_allow_html=True)

    title_block(menu)

# =========================
# BEAM DEFLECTION
# =========================

elif menu == "Beam Deflection":
    sheet_label(menu)
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
    half = x <= L / 2
    y = np.zeros_like(x)
    y[half] = (P * x[half] * (3 * L**2 - 4 * x[half]**2)) / (48 * E * I)
    xr = L - x[~half]
    y[~half] = (P * xr * (3 * L**2 - 4 * xr**2)) / (48 * E * I)

    shape_df = pd.DataFrame({"Position (m)": x, "Deflection (m)": -y}).set_index("Position (m)")
    st.markdown("**Deflection Shape Along Beam**")
    st.line_chart(shape_df, use_container_width=True, color="#FF6B35")

    title_block(menu)

# =========================
# POWER & TORQUE
# =========================

elif menu == "Power & Torque":
    sheet_label(menu)

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
    curve_df = pd.DataFrame({"RPM": rpm_range, "Power (kW)": power_range}).set_index("RPM")

    st.markdown("**Power vs RPM at Fixed Torque**")
    st.line_chart(curve_df, use_container_width=True, color="#00D9FF")

    title_block(menu)

# =========================
# GEAR RATIO CALCULATOR
# =========================

elif menu == "Gear Ratio Calculator":
    sheet_label(menu)

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

    title_block(menu)

# =========================
# FLUID FLOW - REYNOLDS NUMBER
# =========================

elif menu == "Fluid Flow (Reynolds Number)":
    sheet_label(menu)

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

    gauge(
        "Reynolds Number", Re, max(6000, Re * 1.2),
        zones=[(2300, "#39FF6A"), (4000, "#FFD60A"), (max(6000, Re*1.2), "#FF3B30")]
    )

    title_block(menu)

# =========================
# THERMAL EFFICIENCY
# =========================

elif menu == "Thermal Efficiency":
    sheet_label(menu)

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
        gauge(f"{cycle} Cycle Efficiency", eff * 100, 100, unit="%",
              zones=[(35, "#FF3B30"), (55, "#FFD60A"), (100, "#39FF6A")])

    title_block(menu)
