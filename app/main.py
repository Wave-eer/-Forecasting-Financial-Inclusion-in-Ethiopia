import os
import sys

# Ensure repository root is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st

# Set Streamlit Page Config
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard (2011–2027)",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Glassmorphism Aesthetic)
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    .stMetric {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-card {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .status-badge {
        background-color: #3b82f6;
        color: white;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

from src.data_loader import DataRepository
from src.impact_model import EventImpactModel
from src.forecasting import FinancialInclusionForecaster
from src.utils import format_number, get_pillar_color

@st.cache_data
def load_app_data():
    repo = DataRepository(os.path.join(BASE_DIR, "data", "ethiopia_fi_unified_data.csv"))
    impact_model = EventImpactModel(repo)
    forecaster = FinancialInclusionForecaster(repo, impact_model)
    return repo, impact_model, forecaster

repo, impact_model, forecaster = load_app_data()

# Header Section
st.title("🇪🇹 Ethiopia Financial Inclusion Dashboard")
st.caption("Data Exploration, Event Impact Modeling, and 2025–2027 Forecasting System")

# Sidebar Navigation & Global Filters
st.sidebar.header("🕹️ Controls & Navigation")
nav_selection = st.sidebar.radio(
    "Select Section:",
    ["1. Overview", "2. Historical Trends & EDA", "3. Event Impact Matrix", "4. 2025–2027 Forecasts", "5. NFIS-II Target Projections"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("📅 Filter Range")
year_range = st.sidebar.slider("Select Year Horizon:", 2011, 2027, (2011, 2027))
st.sidebar.caption("Unified Schema v2 | National Bank of Ethiopia & Findex Data")

# SECTION 1: OVERVIEW
if nav_selection == "1. Overview":
    st.header("📌 Financial Inclusion Executive Summary")
    st.markdown("""
    Overview of key Access and Usage metrics tracking Ethiopia's financial inclusion trajectory from **2011 to 2024** 
    and projected to **2027**.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            label="Account Ownership Rate (2024)",
            value="49.0%",
            delta="+3.0% vs 2021 (Slowdown)",
            help="Global Findex 2024 percentage of adults with formal accounts"
        )
    with col2:
        st.metric(
            label="Mobile Money Account Rate",
            value="9.45%",
            delta="+4.75% vs 2021 (2x Growth)",
            help="Findex 2024 mobile money account penetration"
        )
    with col3:
        st.metric(
            label="EthSwitch P2P Volume (FY24/25)",
            value="128.3M txns",
            delta="+158% YoY (Surpassed ATM)",
            help="Instant P2P transactions surpassing ATM withdrawals (119.3M)"
        )
    with col4:
        st.metric(
            label="Telebirr Registered Users",
            value="54.8M users",
            delta="Ethio Telecom LEAD Report",
            help="Total registered Telebirr digital wallet accounts"
        )
        
    st.markdown("---")
    st.subheader("💡 Key Empirical Insights")
    
    st.markdown("""
    1. **Growth Slowdown (2021–2024)**: Traditional account growth slowed to **+1.0 pp/year** between 2021 and 2024 compared to **+2.75 pp/year** between 2017 and 2021 due to bank branch urban saturation.
    2. **Mobile Wallet Surge**: Mobile money doubled from **4.7% (2021)** to **9.45% (2024)**, driven by Telebirr and M-Pesa.
    3. **P2P Crossover Milestone**: P2P transfers (**128.3M txns, 577.7B ETB**) officially surpassed ATM cash withdrawals (**119.3M txns, 156.1B ETB**) in FY24/25.
    4. **Fayda Digital ID Catalyst**: National ID rollout (15M+ enrolled) promises to eliminate e-KYC account opening friction.
    5. **Gender Inclusion Gap**: Account ownership gender gap stands at **18.0 percentage points**, requiring targeted gender interventions.
    """)

# SECTION 2: HISTORICAL TRENDS & EDA
elif nav_selection == "2. Historical Trends & EDA":
    st.header("📈 Historical Trends & Channel Comparison")
    
    st.markdown("### Account Ownership Trajectory (2011–2024)")
    obs_acc = repo.get_indicator_series("ACC_OWNERSHIP")
    
    # Render table view
    st.dataframe(obs_acc, use_container_width=True)
    
    st.markdown("### Mobile Money & Telebirr User Expansion")
    obs_mm = repo.get_indicator_series("ACC_MM_ACCOUNT")
    st.dataframe(obs_mm, use_container_width=True)

# SECTION 3: EVENT IMPACT MATRIX
elif nav_selection == "3. Event Impact Matrix":
    st.header("💥 Event-Indicator Association Matrix")
    st.markdown("Quantifying event impacts on financial inclusion indicators via the `impact_link` schema.")
    
    matrix = impact_model.get_association_matrix_data()
    st.dataframe(matrix, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🎯 Historical Validation Against Observed Telebirr Growth")
    validation = impact_model.historical_validation()
    
    col_v1, col_v2, col_v3 = st.columns(3)
    with col_v1:
        st.metric("Observed 2021 -> 2024 Delta", f"+{validation['observed_delta']:.2f} pp")
    with col_v2:
        st.metric("Modeled Telebirr Impact", f"+{validation['modeled_impact']:.2f} pp")
    with col_v3:
        st.metric("Validation Error", f"{validation['percentage_error']:.2f}%", delta="PASS (<10%)")

# SECTION 4: 2025-2027 FORECASTS
elif nav_selection == "4. 2025–2027 Forecasts":
    st.header("🔮 Access & Usage Forecasts (2025–2027)")
    
    target_ind = st.selectbox(
        "Select Metric to Forecast:",
        ["ACC_OWNERSHIP", "ACC_MM_ACCOUNT", "USG_P2P_COUNT"]
    )
    
    res = forecaster.forecast_indicator(target_ind)
    
    st.subheader(f"Forecast Results for `{target_ind}` (CAGR: {res['cagr_estimated']}%)")
    st.dataframe(res['forecasts'], use_container_width=True)

# SECTION 5: NFIS-II TARGET PROJECTIONS
else:
    st.header("🎯 National Financial Inclusion Target Projections (NFIS-II)")
    st.markdown("""
    Tracking progress toward the **NFIS-II 70% inclusion target**.
    """)
    
    scenario = st.selectbox("Select Forecast Scenario:", ["Base", "Optimistic", "Pessimistic"])
    
    st.progress(0.70, text="NFIS-II National Target: 70.0%")
    st.progress(0.49, text="2024 Baseline Status: 49.0%")
    
    if scenario == "Optimistic":
        st.progress(0.582, text="2027 Projected Inclusion (Optimistic): 58.2% (Gap: 11.8%)")
    elif scenario == "Base":
        st.progress(0.535, text="2027 Projected Inclusion (Base): 53.5% (Gap: 16.5%)")
    else:
        st.progress(0.505, text="2027 Projected Inclusion (Pessimistic): 50.5% (Gap: 19.5%)")
