"""
Pure Python SVG Chart Generator for Final Report Visualizations.
No external library dependencies required.
"""

import os

fig_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports", "figures")
os.makedirs(fig_dir, exist_ok=True)

# 1. Figure 1: Account Ownership Trajectory (2011-2024)
svg1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background:#0f172a; font-family:system-ui, -apple-system, sans-serif;">
  <!-- Title -->
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">Ethiopia Account Ownership Trajectory (2011–2024)</text>
  <text x="400" y="65" text-anchor="middle" fill="#94a3b8" font-size="13">Empirical Global Findex Benchmarks &amp; Branch Saturation Slowdown</text>
  
  <!-- Axes -->
  <line x1="80" y1="360" x2="740" y2="360" stroke="#334155" stroke-width="2"/>
  <line x1="80" y1="100" x2="80" y2="360" stroke="#334155" stroke-width="2"/>
  
  <!-- Grid & Y-Labels -->
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

  <!-- Plot Line & Points -->
  <!-- 2011: (120, 304) = 14% | 2014: (260, 272) = 22% | 2017: (400, 220) = 35% | 2021: (580, 176) = 46% | 2024: (700, 164) = 49% -->
  <polyline points="120,304 260,272 400,220 580,176 700,164" fill="none" stroke="#3b82f6" stroke-width="4"/>
  
  <!-- Fill Area -->
  <polygon points="120,304 260,272 400,220 580,176 700,164 700,360 120,360" fill="#3b82f6" fill-opacity="0.15"/>

  <!-- Data Circles & Labels -->
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

  <!-- Annotations -->
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

  <!-- Left Card: Mobile Money Growth -->
  <rect x="40" y="90" width="340" height="320" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="210" y="125" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">Mobile Money Account Rate (%)</text>
  
  <!-- Bars -->
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

  <!-- Right Card: P2P vs ATM Crossover -->
  <rect x="420" y="90" width="340" height="320" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="590" y="125" text-anchor="middle" fill="#f59e0b" font-size="16" font-weight="bold">P2P vs ATM Volume (FY2024/25)</text>

  <!-- ATM Bar -->
  <rect x="470" y="180" width="90" height="165" fill="#f59e0b" fill-opacity="0.8" rx="6"/>
  <text x="515" y="170" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">119.3M</text>
  <text x="515" y="365" text-anchor="middle" fill="#cbd5e1" font-size="12">ATM Withdrawals</text>

  <!-- P2P Bar -->
  <rect x="610" y="160" width="90" height="185" fill="#10b981" rx="6"/>
  <text x="655" y="150" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">128.3M</text>
  <text x="655" y="365" text-anchor="middle" fill="#cbd5e1" font-size="12">Instant P2P</text>

  <!-- Badge -->
  <rect x="490" y="385" width="200" height="24" rx="12" fill="#065f46" stroke="#10b981"/>
  <text x="590" y="401" text-anchor="middle" fill="#a7f3d0" font-size="11" font-weight="bold">Crossover Ratio: 1.08x</text>
</svg>"""

with open(os.path.join(fig_dir, "fig2_mobile_money_and_p2p_surge.svg"), "w") as f:
    f.write(svg2)

# 3. Figure 3: Forecast Scenarios (2025-2027)
svg3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background:#0f172a; font-family:system-ui, -apple-system, sans-serif;">
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">Ethiopia Account Ownership Forecasts (2025–2027)</text>
  <text x="400" y="65" text-anchor="middle" fill="#94a3b8" font-size="13">Multi-Scenario Projections &amp; Progress Toward NFIS-II Targets</text>

  <!-- Target Line (60% / 70%) -->
  <line x1="100" y1="130" x2="720" y2="130" stroke="#a855f7" stroke-width="2" stroke-dasharray="6"/>
  <text x="730" y="135" fill="#c084fc" font-size="12" font-weight="bold">60% NFIS Goal</text>

  <!-- Axes -->
  <line x1="100" y1="360" x2="720" y2="360" stroke="#334155" stroke-width="2"/>
  <line x1="100" y1="100" x2="100" y2="360" stroke="#334155" stroke-width="2"/>

  <!-- Y Labels -->
  <text x="85" y="365" text-anchor="end" fill="#64748b" font-size="12">45%</text>
  <text x="85" y="285" text-anchor="end" fill="#64748b" font-size="12">50%</text>
  <text x="85" y="205" text-anchor="end" fill="#64748b" font-size="12">55%</text>
  <text x="85" y="125" text-anchor="end" fill="#64748b" font-size="12">60%</text>

  <!-- Plot Points -->
  <!-- 2024: (140, 296) = 49% -->
  <!-- 2025: Opt (330, 241) = 52.4%, Base (330, 267) = 50.8%, Pess (330, 288) = 49.5% -->
  <!-- 2026: Opt (520, 198) = 55.1%, Base (520, 244) = 52.2%, Pess (520, 280) = 50.0% -->
  <!-- 2027: Opt (700, 148) = 58.2%, Base (700, 224) = 53.5%, Pess (700, 272) = 50.5% -->

  <!-- Optimistic -->
  <polyline points="140,296 330,241 520,198 700,148" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4"/>
  <!-- Base -->
  <polyline points="140,296 330,267 520,244 700,224" fill="none" stroke="#3b82f6" stroke-width="4"/>
  <!-- Pessimistic -->
  <polyline points="140,296 330,288 520,280 700,272" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="2"/>

  <!-- Points & Values -->
  <!-- 2024 -->
  <circle cx="140" cy="296" r="6" fill="#3b82f6"/>
  <text x="140" y="316" text-anchor="middle" fill="#cbd5e1" font-size="12">49.0% (2024)</text>

  <!-- 2027 Points -->
  <circle cx="700" cy="148" r="6" fill="#22c55e"/>
  <text x="700" y="138" text-anchor="middle" fill="#4ade80" font-size="13" font-weight="bold">58.2% (Opt)</text>

  <circle cx="700" cy="224" r="7" fill="#3b82f6"/>
  <text x="700" y="214" text-anchor="middle" fill="#60a5fa" font-size="14" font-weight="bold">53.5% (Base)</text>

  <circle cx="700" cy="272" r="6" fill="#ef4444"/>
  <text x="700" y="292" text-anchor="middle" fill="#fca5a5" font-size="13" font-weight="bold">50.5% (Pess)</text>

  <!-- X Labels -->
  <text x="330" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2025</text>
  <text x="520" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2026</text>
  <text x="700" y="385" text-anchor="middle" fill="#94a3b8" font-size="12">2027</text>

  <!-- Legend -->
  <rect x="140" y="90" width="400" height="30" rx="6" fill="#1e293b" stroke="#334155"/>
  <circle cx="160" cy="105" r="4" fill="#22c55e"/>
  <text x="170" y="109" fill="#cbd5e1" font-size="11">Optimistic</text>

  <circle cx="260" cy="105" r="4" fill="#3b82f6"/>
  <text x="270" y="109" fill="#cbd5e1" font-size="11">Base</text>

  <circle cx="340" cy="105" r="4" fill="#ef4444"/>
  <text x="350" y="109" fill="#cbd5e1" font-size="11">Pessimistic</text>
</svg>"""

with open(os.path.join(fig_dir, "fig4_forecasts_2025_2027.svg"), "w") as f:
    f.write(svg3)

print("Pure Python SVG vector charts generated successfully in reports/figures/")
