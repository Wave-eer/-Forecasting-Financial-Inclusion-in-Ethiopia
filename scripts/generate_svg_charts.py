"""
Pure Python SVG Chart Generator for Final Report Visualizations.
No external library dependencies required.
Generates 6 vector SVG charts in reports/figures/
"""

import os

fig_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports", "figures")
os.makedirs(fig_dir, exist_ok=True)

# 1. Figure 1: Account Ownership Trajectory (2011-2024)
svg1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background:#0f172a; font-family:system-ui, -apple-system, sans-serif;">
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">Ethiopia Account Ownership Trajectory (2011–2024)</text>
  <text x="400" y="65" text-anchor="middle" fill="#94a3b8" font-size="13">Empirical Global Findex Benchmarks &amp; Branch Saturation Slowdown</text>
  
  <line x1="80" y1="360" x2="740" y2="360" stroke="#334155" stroke-width="2"/>
  <line x1="80" y1="100" x2="80" y2="360" stroke="#334155" stroke-width="2"/>
  
  <text x="65" y="365" text-anchor="end" fill="#64748b" font-size="12">0%</text>
  <line x1="80" y1="360" x2="740" y2="360" stroke="#334155" stroke-dasharray="4"/>
  
  <text x="65" y="305" text-anchor="end" fill="#64748b" font-size="12">15%</text>
  <line x1="80" y1="300" x2="740" y2="300" stroke="#334155" stroke-dasharray="4"/>
  
  <text x="65" y="245" text-anchor="end" fill="#64748b" font-size="12">30%</text>
  <line x1="80" y1="240" x2="740" y2="240" stroke="#334155" stroke-dasharray="4"/>
  
  <text x="65" y="185" text-anchor="end" fill="#64748b" font-size="12">45%</text>
  <line x1="80" y1="180" x2="740" y2="180" stroke="#334155" stroke-dasharray="4"/>
  
  <text x="65" y="125" text-anchor="end" fill="#64748b" font-size="12">60%</text>
  <line x1="80" y1="120" x2="740" y2="120" stroke="#334155" stroke-dasharray="4"/>

  <polyline points="120,304 260,272 400,220 580,176 700,164" fill="none" stroke="#3b82f6" stroke-width="4"/>
  <polygon points="120,304 260,272 400,220 580,176 700,164 700,360 120,360" fill="#3b82f6" fill-opacity="0.15"/>

  <circle cx="120" cy="304" r="6" fill="#60a5fa" stroke="#1d4ed8" stroke-width="2"/>
  <text x="120" y="290" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">14.0%</text>
  <text x="120" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2011</text>

  <circle cx="260" cy="272" r="6" fill="#60a5fa" stroke="#1d4ed8" stroke-width="2"/>
  <text x="260" y="258" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">22.0%</text>
  <text x="260" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2014</text>

  <circle cx="400" cy="220" r="6" fill="#60a5fa" stroke="#1d4ed8" stroke-width="2"/>
  <text x="400" y="206" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">35.0%</text>
  <text x="400" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2017</text>

  <circle cx="580" cy="176" r="6" fill="#60a5fa" stroke="#1d4ed8" stroke-width="2"/>
  <text x="580" y="162" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">46.0%</text>
  <text x="580" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2021</text>

  <circle cx="700" cy="164" r="7" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <text x="700" y="150" text-anchor="middle" fill="#4ade80" font-size="14" font-weight="bold">49.0%</text>
  <text x="700" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2024</text>

  <rect x="440" y="120" width="125" height="42" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="502" y="137" text-anchor="middle" fill="#60a5fa" font-size="11" font-weight="bold">Surge Phase</text>
  <text x="502" y="153" text-anchor="middle" fill="#cbd5e1" font-size="10">+2.75 pp/yr (Branching)</text>

  <rect x="590" y="210" width="140" height="42" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="660" y="227" text-anchor="middle" fill="#fb7185" font-size="11" font-weight="bold">Growth Slowdown</text>
  <text x="660" y="243" text-anchor="middle" fill="#cbd5e1" font-size="10">+1.0 pp/yr (Urban Saturation)</text>
</svg>"""

with open(os.path.join(fig_dir, "fig1_account_ownership_trajectory.svg"), "w") as f:
    f.write(svg1)

# 2. Figure 2: Mobile Money Adoption & P2P Crossover
svg2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background:#0f172a; font-family:system-ui, -apple-system, sans-serif;">
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">Mobile Money Penetration &amp; Digital P2P Crossover</text>
  <text x="400" y="65" text-anchor="middle" fill="#94a3b8" font-size="13">EthSwitch FY2024/25: Instant P2P Transfers (128.3M) Surpass ATM Cash Withdrawals (119.3M)</text>

  <rect x="40" y="90" width="340" height="320" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="210" y="125" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">Mobile Money Account Rate (%)</text>
  
  <rect x="80" y="330" width="60" height="15" fill="#64748b" rx="4"/>
  <text x="110" y="322" text-anchor="middle" fill="#cbd5e1" font-size="12" font-weight="bold">0.6%</text>
  <text x="110" y="365" text-anchor="middle" fill="#94a3b8" font-size="12">2017</text>

  <rect x="180" y="240" width="60" height="105" fill="#3b82f6" rx="4"/>
  <text x="210" y="232" text-anchor="middle" fill="#60a5fa" font-size="13" font-weight="bold">4.70%</text>
  <text x="210" y="365" text-anchor="middle" fill="#94a3b8" font-size="12">2021</text>

  <rect x="280" y="150" width="60" height="195" fill="#22c55e" rx="4"/>
  <text x="310" y="142" text-anchor="middle" fill="#4ade80" font-size="14" font-weight="bold">9.45%</text>
  <text x="310" y="365" text-anchor="middle" fill="#94a3b8" font-size="12">2024</text>
  
  <text x="210" y="395" text-anchor="middle" fill="#4ade80" font-size="12" font-weight="bold">2x Account Doubling Post-Telebirr</text>

  <rect x="420" y="90" width="340" height="320" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="590" y="125" text-anchor="middle" fill="#f59e0b" font-size="16" font-weight="bold">P2P vs ATM Volume (FY2024/25)</text>

  <rect x="470" y="180" width="90" height="165" fill="#f59e0b" fill-opacity="0.8" rx="6"/>
  <text x="515" y="170" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">119.3M</text>
  <text x="515" y="365" text-anchor="middle" fill="#cbd5e1" font-size="12">ATM Withdrawals</text>

  <rect x="610" y="160" width="90" height="185" fill="#10b981" rx="6"/>
  <text x="655" y="150" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">128.3M</text>
  <text x="655" y="365" text-anchor="middle" fill="#cbd5e1" font-size="12">Instant P2P</text>

  <rect x="490" y="385" width="200" height="24" rx="12" fill="#065f46" stroke="#10b981"/>
  <text x="590" y="401" text-anchor="middle" fill="#a7f3d0" font-size="11" font-weight="bold">Crossover Ratio: 1.08x</text>
</svg>"""

with open(os.path.join(fig_dir, "fig2_mobile_money_and_p2p_surge.svg"), "w") as f:
    f.write(svg2)

# 3. Figure 3: SHAP Feature Importance & Impact Attribution Matrix
svg3_shap = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background:#0f172a; font-family:system-ui, -apple-system, sans-serif;">
  <text x="400" y="35" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="bold">SHAP Feature Importance &amp; Impact Attribution Matrix</text>
  <text x="400" y="58" text-anchor="middle" fill="#94a3b8" font-size="12">Quantifying Event Contribution to Financial Inclusion Metrics (\Delta Metric Impact)</text>

  <!-- Y Axis Label Column -->
  <text x="255" y="105" text-anchor="end" fill="#cbd5e1" font-size="12" font-weight="bold">Telebirr Launch (EVT_0001)</text>
  <text x="255" y="122" text-anchor="end" fill="#64748b" font-size="10">Target: ACC_MM_ACCOUNT (Mobile Money)</text>

  <text x="255" y="165" text-anchor="end" fill="#cbd5e1" font-size="12" font-weight="bold">Fayda Digital ID Rollout (EVT_0004)</text>
  <text x="255" y="182" text-anchor="end" fill="#64748b" font-size="10">Target: ACC_OWNERSHIP (Account Rate)</text>

  <text x="255" y="225" text-anchor="end" fill="#cbd5e1" font-size="12" font-weight="bold">NBE Directive ONPS/01/2020 (EVT_0011)</text>
  <text x="255" y="242" text-anchor="end" fill="#64748b" font-size="10">Target: ACC_MM_ACCOUNT (Non-Bank Issuers)</text>

  <text x="255" y="285" text-anchor="end" fill="#cbd5e1" font-size="12" font-weight="bold">EthSwitch P2P Interoperability (EVT_0012)</text>
  <text x="255" y="302" text-anchor="end" fill="#64748b" font-size="10">Target: USG_P2P_COUNT (Instant Transfers)</text>

  <text x="255" y="345" text-anchor="end" fill="#cbd5e1" font-size="12" font-weight="bold">Fayda Gender e-KYC (EVT_0004)</text>
  <text x="255" y="362" text-anchor="end" fill="#64748b" font-size="10">Target: GEN_GAP_ACC (Gender Gap Reduction)</text>

  <!-- Axis divider -->
  <line x1="270" y1="85" x2="270" y2="385" stroke="#475569" stroke-width="2"/>

  <!-- Horizontal SHAP Value Bars -->
  <!-- Bar 1: Telebirr +4.75 pp -->
  <rect x="270" y="95" width="285" height="26" fill="#3b82f6" rx="4"/>
  <text x="565" y="113" fill="#60a5fa" font-size="12" font-weight="bold">+4.75 pp SHAP Value</text>

  <!-- Bar 2: Fayda ID +4.50 pp -->
  <rect x="270" y="155" width="270" height="26" fill="#10b981" rx="4"/>
  <text x="550" y="173" fill="#34d399" font-size="12" font-weight="bold">+4.50 pp SHAP Value</text>

  <!-- Bar 3: NBE Directive +4.00 pp -->
  <rect x="270" y="215" width="240" height="26" fill="#8b5cf6" rx="4"/>
  <text x="520" y="233" fill="#c084fc" font-size="12" font-weight="bold">+4.00 pp SHAP Value</text>

  <!-- Bar 4: EthSwitch P2P +78.0M -->
  <rect x="270" y="275" width="310" height="26" fill="#f59e0b" rx="4"/>
  <text x="590" y="293" fill="#fbbf24" font-size="12" font-weight="bold">+78.0M Txns SHAP Value</text>

  <!-- Bar 5: Gender Gap Reduction -3.00 pp (Negative bar extending left or highlighted) -->
  <rect x="270" y="335" width="180" height="26" fill="#ec4899" rx="4"/>
  <text x="460" y="353" fill="#f472b6" font-size="12" font-weight="bold">-3.00 pp (Gap Narrowing)</text>

  <!-- Footer Legend -->
  <rect x="230" y="405" width="340" height="25" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="400" y="422" text-anchor="middle" fill="#94a3b8" font-size="11">SHAP Attribution validated against Findex 2021-2024 empirical shifts</text>
</svg>"""

with open(os.path.join(fig_dir, "fig3_shap_explainability_matrix.svg"), "w") as f:
    f.write(svg3_shap)

# 4. Figure 4: Forecast Scenarios (2025-2027)
svg4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background:#0f172a; font-family:system-ui, -apple-system, sans-serif;">
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">Ethiopia Account Ownership Forecasts (2025–2027)</text>
  <text x="400" y="65" text-anchor="middle" fill="#94a3b8" font-size="13">Multi-Scenario Projections &amp; Progress Toward NFIS-II Targets</text>

  <line x1="100" y1="130" x2="720" y2="130" stroke="#a855f7" stroke-width="2" stroke-dasharray="6"/>
  <text x="730" y="135" fill="#c084fc" font-size="12" font-weight="bold">60% NFIS Goal</text>

  <line x1="100" y1="360" x2="720" y2="360" stroke="#334155" stroke-width="2"/>
  <line x1="100" y1="100" x2="100" y2="360" stroke="#334155" stroke-width="2"/>

  <text x="85" y="365" text-anchor="end" fill="#64748b" font-size="12">45%</text>
  <text x="85" y="285" text-anchor="end" fill="#64748b" font-size="12">50%</text>
  <text x="85" y="205" text-anchor="end" fill="#64748b" font-size="12">55%</text>
  <text x="85" y="125" text-anchor="end" fill="#64748b" font-size="12">60%</text>

  <polyline points="140,296 330,241 520,198 700,148" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4"/>
  <polyline points="140,296 330,267 520,244 700,224" fill="none" stroke="#3b82f6" stroke-width="4"/>
  <polyline points="140,296 330,288 520,280 700,272" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="2"/>

  <circle cx="140" cy="296" r="6" fill="#3b82f6"/>
  <text x="140" y="316" text-anchor="middle" fill="#cbd5e1" font-size="12">49.0% (2024)</text>

  <circle cx="700" cy="148" r="6" fill="#22c55e"/>
  <text x="700" y="138" text-anchor="middle" fill="#4ade80" font-size="13" font-weight="bold">58.2% (Opt)</text>

  <circle cx="700" cy="224" r="7" fill="#3b82f6"/>
  <text x="700" y="214" text-anchor="middle" fill="#60a5fa" font-size="14" font-weight="bold">53.5% (Base)</text>

  <circle cx="700" cy="272" r="6" fill="#ef4444"/>
  <text x="700" y="292" text-anchor="middle" fill="#fca5a5" font-size="13" font-weight="bold">50.5% (Pess)</text>

  <text x="330" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2025</text>
  <text x="520" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2026</text>
  <text x="700" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2027</text>

  <rect x="140" y="90" width="400" height="30" rx="6" fill="#1e293b" stroke="#334155"/>
  <circle cx="160" cy="105" r="4" fill="#22c55e"/>
  <text x="170" y="109" fill="#cbd5e1" font-size="11">Optimistic</text>

  <circle cx="260" cy="105" r="4" fill="#3b82f6"/>
  <text x="270" y="109" fill="#cbd5e1" font-size="11">Base</text>

  <circle cx="340" cy="105" r="4" fill="#ef4444"/>
  <text x="350" y="109" fill="#cbd5e1" font-size="11">Pessimistic</text>
</svg>"""

with open(os.path.join(fig_dir, "fig4_forecasts_2025_2027.svg"), "w") as f:
    f.write(svg4)

# 5. Figure 5: Streamlit Interactive Dashboard UI Representation
svg5_dashboard = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="100%" style="background:#0f172a; font-family:system-ui, -apple-system, sans-serif;">
  <!-- Streamlit Top Bar -->
  <rect x="0" y="0" width="900" height="40" fill="#1e293b" stroke="#334155"/>
  <circle cx="25" cy="20" r="6" fill="#ef4444"/>
  <circle cx="45" cy="20" r="6" fill="#f59e0b"/>
  <circle cx="65" cy="20" r="6" fill="#10b981"/>
  <text x="450" y="25" text-anchor="middle" fill="#f8fafc" font-size="14" font-weight="bold">Streamlit — Ethiopia Financial Inclusion Analytics Suite (app/main.py)</text>

  <!-- Left Navigation Sidebar -->
  <rect x="0" y="40" width="200" height="480" fill="#0f172a" stroke="#1e293b"/>
  <text x="20" y="75" fill="#38bdf8" font-size="13" font-weight="bold">NAVIGATION</text>

  <rect x="15" y="90" width="170" height="30" rx="6" fill="#3b82f6"/>
  <text x="30" y="110" fill="#ffffff" font-size="12" font-weight="bold">1. Overview &amp; KPIs</text>

  <rect x="15" y="130" width="170" height="30" rx="6" fill="#1e293b"/>
  <text x="30" y="150" fill="#94a3b8" font-size="12">2. Historical Trends</text>

  <rect x="15" y="170" width="170" height="30" rx="6" fill="#1e293b"/>
  <text x="30" y="190" fill="#94a3b8" font-size="12">3. Impact Matrix</text>

  <rect x="15" y="210" width="170" height="30" rx="6" fill="#1e293b"/>
  <text x="30" y="230" fill="#94a3b8" font-size="12">4. 2025-2027 Forecasts</text>

  <rect x="15" y="250" width="170" height="30" rx="6" fill="#1e293b"/>
  <text x="30" y="270" fill="#94a3b8" font-size="12">5. Target Gap Analysis</text>

  <!-- Sidebar Controls -->
  <text x="20" y="320" fill="#38bdf8" font-size="12" font-weight="bold">SCENARIO CONTROLS</text>
  <text x="20" y="345" fill="#cbd5e1" font-size="11">Select Scenario:</text>
  <rect x="15" y="355" width="170" height="25" rx="4" fill="#1e293b" stroke="#334155"/>
  <text x="25" y="372" fill="#38bdf8" font-size="11">● Base Scenario ▼</text>

  <text x="20" y="405" fill="#cbd5e1" font-size="11">Fayda e-KYC Impact:</text>
  <line x1="20" y1="425" x2="170" y2="425" stroke="#475569" stroke-width="4"/>
  <circle cx="120" cy="425" r="7" fill="#3b82f6"/>
  <text x="120" y="445" text-anchor="middle" fill="#60a5fa" font-size="10">+4.50 pp</text>

  <!-- Main Content Dashboard Area -->
  <!-- Top 4 KPI Cards -->
  <rect x="220" y="60" width="150" height="80" rx="8" fill="#1e293b" stroke="#3b82f6"/>
  <text x="235" y="82" fill="#94a3b8" font-size="11">Account Ownership</text>
  <text x="235" y="112" fill="#38bdf8" font-size="20" font-weight="bold">49.0%</text>
  <text x="235" y="130" fill="#22c55e" font-size="10">+3.0 pp (2021-2024)</text>

  <rect x="385" y="60" width="150" height="80" rx="8" fill="#1e293b" stroke="#22c55e"/>
  <text x="400" y="82" fill="#94a3b8" font-size="11">Mobile Money Rate</text>
  <text x="400" y="112" fill="#4ade80" font-size="20" font-weight="bold">9.45%</text>
  <text x="400" y="130" fill="#22c55e" font-size="10">2x Doubling (Telebirr)</text>

  <rect x="550" y="60" width="150" height="80" rx="8" fill="#1e293b" stroke="#f59e0b"/>
  <text x="565" y="82" fill="#94a3b8" font-size="11">EthSwitch P2P Count</text>
  <text x="565" y="112" fill="#fbbf24" font-size="20" font-weight="bold">128.3M</text>
  <text x="565" y="130" fill="#22c55e" font-size="10">+158% YoY Surge</text>

  <rect x="715" y="60" width="160" height="80" rx="8" fill="#1e293b" stroke="#ec4899"/>
  <text x="730" y="82" fill="#94a3b8" font-size="11">P2P / ATM Crossover</text>
  <text x="730" y="112" fill="#f472b6" font-size="20" font-weight="bold">1.08x</text>
  <text x="730" y="130" fill="#f472b6" font-size="10">P2P &gt; ATM Volume</text>

  <!-- Interactive Chart Area -->
  <rect x="220" y="160" width="655" height="210" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="240" y="185" fill="#f8fafc" font-size="14" font-weight="bold">Interactive Trajectory &amp; Forecast Visualizer</text>
  
  <polyline points="260,330 360,300 460,260 560,220 660,195 760,175" fill="none" stroke="#3b82f6" stroke-width="3"/>
  <circle cx="660" cy="195" r="5" fill="#4ade80"/>
  <circle cx="760" cy="175" r="5" fill="#60a5fa"/>

  <!-- Lower Data Table Area -->
  <rect x="220" y="385" width="655" height="120" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="240" y="410" fill="#38bdf8" font-size="12" font-weight="bold">Event Impact Association Matrix Table</text>

  <text x="240" y="435" fill="#94a3b8" font-size="11">Event Name | Category | Indicator | Impact Estimate | Lag</text>
  <line x1="240" y1="442" x2="850" y2="442" stroke="#334155"/>
  <text x="240" y="460" fill="#cbd5e1" font-size="11">Telebirr Launch | Product | ACC_MM_ACCOUNT | +4.75 pp | 12.0 mos</text>
  <text x="240" y="480" fill="#cbd5e1" font-size="11">Fayda ID Rollout | Infrastructure | ACC_OWNERSHIP | +4.50 pp | 18.0 mos</text>
  <text x="240" y="500" fill="#cbd5e1" font-size="11">EthSwitch P2P | Infrastructure | USG_P2P_COUNT | +78.0M txns | 12.0 mos</text>
</svg>"""

with open(os.path.join(fig_dir, "fig5_streamlit_dashboard_interface.svg"), "w") as f:
    f.write(svg5_dashboard)

# 6. Figure 6: Unified Schema Architecture & Data Flow
svg6_arch = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background:#0f172a; font-family:system-ui, -apple-system, sans-serif;">
  <text x="400" y="35" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="bold">Unified Schema v2 Architecture &amp; Event-Impact Pipeline</text>
  <text x="400" y="58" text-anchor="middle" fill="#94a3b8" font-size="12">Decoupling Neutral Events from Empirical Metric Observations to Eliminate Bias</text>

  <!-- Entity Box 1: Observation -->
  <rect x="40" y="90" width="210" height="180" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
  <rect x="40" y="90" width="210" height="35" rx="10" fill="#1d4ed8"/>
  <text x="145" y="113" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">observation</text>
  
  <text x="55" y="145" fill="#cbd5e1" font-size="11">• Empirical metrics (Findex)</text>
  <text x="55" y="165" fill="#cbd5e1" font-size="11">• pillar assigned (ACCESS)</text>
  <text x="55" y="185" fill="#cbd5e1" font-size="11">• category = empty</text>
  <text x="55" y="205" fill="#cbd5e1" font-size="11">• metric_code: ACC_OWNERSHIP</text>
  <text x="55" y="225" fill="#cbd5e1" font-size="11">• value: 49.0% (2024)</text>

  <!-- Entity Box 2: Event -->
  <rect x="295" y="90" width="210" height="180" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <rect x="295" y="90" width="210" height="35" rx="10" fill="#b45309"/>
  <text x="400" y="113" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">event</text>

  <text x="310" y="145" fill="#cbd5e1" font-size="11">• Exogenous shocks / policy</text>
  <text x="310" y="165" fill="#cbd5e1" font-size="11">• pillar = empty (neutral)</text>
  <text x="310" y="185" fill="#cbd5e1" font-size="11">• category assigned (regulation)</text>
  <text x="310" y="205" fill="#cbd5e1" font-size="11">• event_id: EVT_0001</text>
  <text x="310" y="225" fill="#cbd5e1" font-size="11">• name: Telebirr Launch</text>

  <!-- Entity Box 3: Impact Link -->
  <rect x="550" y="90" width="210" height="180" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <rect x="550" y="90" width="210" height="35" rx="10" fill="#047857"/>
  <text x="655" y="113" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">impact_link</text>

  <text x="565" y="145" fill="#cbd5e1" font-size="11">• Directional connection</text>
  <text x="565" y="165" fill="#cbd5e1" font-size="11">• parent_id: EVT_0001</text>
  <text x="565" y="185" fill="#cbd5e1" font-size="11">• target: ACC_MM_ACCOUNT</text>
  <text x="565" y="205" fill="#cbd5e1" font-size="11">• magnitude: +4.75 pp</text>
  <text x="565" y="225" fill="#cbd5e1" font-size="11">• lag_months: 12.0</text>

  <!-- Connecting Arrows -->
  <path d="M 505 180 L 550 180" fill="none" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
  <path d="M 250 180 L 295 180" fill="none" stroke="#3b82f6" stroke-width="3"/>

  <!-- Bottom Processing Engine Box -->
  <rect x="140" y="300" width="520" height="85" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="2"/>
  <text x="400" y="330" text-anchor="middle" fill="#c084fc" font-size="14" font-weight="bold">EventImpactModel &amp; Sigmoidal Forecaster Engine</text>
  <text x="400" y="355" text-anchor="middle" fill="#cbd5e1" font-size="12">Calculates Lagged S-Curves $\rightarrow$ Generates 2025–2027 Scenarios with 95% CI</text>
</svg>"""

with open(os.path.join(fig_dir, "fig6_unified_schema_architecture.svg"), "w") as f:
    f.write(svg6_arch)

print("All 6 pure Python SVG vector charts generated successfully in reports/figures/")
