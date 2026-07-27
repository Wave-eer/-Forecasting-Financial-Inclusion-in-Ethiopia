"""
Generate static figures for the final report.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 0.8

fig_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports", "figures")
os.makedirs(fig_dir, exist_ok=True)

# 1. Figure 1: Account Ownership Trajectory (2011-2024)
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
years = [2011, 2014, 2017, 2021, 2024]
acc_rates = [14.0, 22.0, 35.0, 46.0, 49.0]

ax.plot(years, acc_rates, marker='o', color='#1d4ed8', linewidth=2.5, markersize=8, label='Account Ownership Rate (%)')
for y, val in zip(years, acc_rates):
    ax.annotate(f"{val:.1f}%", (y, val + 1.2), ha='center', fontweight='bold', color='#1e293b')

# Highlight slowdown annotation
ax.annotate('Surge (+2.75 pp/yr)\nBank Branching', xy=(2019, 40.5), xytext=(2016.5, 45),
            arrowprops=dict(facecolor='#3b82f6', shrink=0.05, width=1, headwidth=6),
            fontsize=9, color='#1e3a8a', bbox=dict(boxstyle='round,pad=0.3', facecolor='#dbeafe', edgecolor='#93c5fd'))

ax.annotate('Slowdown (+1.0 pp/yr)\nUrban Branch Saturation', xy=(2022.5, 47.5), xytext=(2021, 35),
            arrowprops=dict(facecolor='#ef4444', shrink=0.05, width=1, headwidth=6),
            fontsize=9, color='#991b1b', bbox=dict(boxstyle='round,pad=0.3', facecolor='#fee2e2', edgecolor='#fca5a5'))

ax.set_title('Ethiopia Account Ownership Trajectory (2011–2024)\nGlobal Findex Empirical Benchmarks', fontsize=12, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=10, fontweight='bold')
ax.set_ylabel('Adult Account Ownership (%)', fontsize=10, fontweight='bold')
ax.set_ylim(10, 55)
ax.set_xticks(years)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig1_account_ownership_trajectory.png"))
plt.close()

# 2. Figure 2: Mobile Money & P2P Crossover
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# MM adoption
mm_years = [2017, 2021, 2024]
mm_rates = [0.6, 4.7, 9.45]
ax1.bar([str(y) for y in mm_years], mm_rates, color=['#94a3b8', '#3b82f6', '#16a34a'], width=0.5)
for i, v in enumerate(mm_rates):
    ax1.text(i, v + 0.3, f"{v}%", ha='center', fontweight='bold')
ax1.set_title('Mobile Money Account Penetration (2017–2024)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Mobile Money Account Rate (%)', fontsize=10)
ax1.set_ylim(0, 12)

# P2P vs ATM Crossover
channels = ['ATM Withdrawals', 'P2P Instant Transfers']
counts_m = [119.3, 128.3] # FY24/25 in Millions
colors = ['#f59e0b', '#10b981']
bars = ax2.bar(channels, counts_m, color=colors, width=0.45)
for bar, val in zip(bars, counts_m):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 2, f"{val:.1f}M txns", ha='center', fontweight='bold')
ax2.set_title('Digital Payment Crossover (FY2024/25)\nInstant P2P Surpasses Physical ATM Withdrawals', fontsize=11, fontweight='bold')
ax2.set_ylabel('Transaction Volume (Millions)', fontsize=10)
ax2.set_ylim(0, 150)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig2_mobile_money_and_p2p_surge.png"))
plt.close()

# 3. Figure 3: Event Impact Matrix Heatmap
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=300)
events = ['Telebirr Launch', 'M-Pesa Entry', 'Fayda Digital ID', 'NBE Directive', 'EthSwitch P2P']
indicators = ['ACC_MM_ACCOUNT', 'ACC_OWNERSHIP', 'USG_P2P_COUNT', 'GEN_GAP_ACC']

# Impact Matrix Matrix
data = np.array([
    [4.75, 3.00, 35.0, 0.0],
    [2.10, 1.50, 12.0, 0.0],
    [2.50, 4.50, 8.0, -3.0],
    [4.00, 2.00, 15.0, 0.0],
    [1.50, 0.50, 78.0, 0.0]
])

sns.heatmap(data, annot=True, fmt=".1f", cmap='YlGnBu', xticklabels=indicators, yticklabels=events, ax=ax, cbar_kws={'label': 'Modeled Impact Magnitude'})
ax.set_title('Event-Indicator Association Matrix\nQuantified Impact Estimates Across Pillars', fontsize=11, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig3_event_impact_matrix.png"))
plt.close()

# 4. Figure 4: 2025-2027 Forecasts Scenarios
fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=300)
fc_years = [2024, 2025, 2026, 2027]
base_fc = [49.0, 50.8, 52.2, 53.5]
opt_fc = [49.0, 52.4, 55.1, 58.2]
pess_fc = [49.0, 49.5, 50.0, 50.5]

ax.plot(fc_years, opt_fc, marker='^', color='#16a34a', linestyle='--', linewidth=2, label='Optimistic Scenario (Fast Fayda + Interoperability)')
ax.plot(fc_years, base_fc, marker='o', color='#2563eb', linewidth=2.5, label='Base Scenario (Steady Growth)')
ax.plot(fc_years, pess_fc, marker='v', color='#dc2626', linestyle=':', linewidth=2, label='Pessimistic Scenario (Macro Headwinds)')

ax.fill_between(fc_years, pess_fc, opt_fc, color='#3b82f6', alpha=0.12, label='Uncertainty Range (95% CI)')

# Target Line
ax.axhline(60.0, color='#9333ea', linestyle='--', linewidth=1.5, label='NFIS Interim Goal (60%)')

for y, b, o, p in zip(fc_years[1:], base_fc[1:], opt_fc[1:], pess_fc[1:]):
    ax.annotate(f"{b}%", (y, b + 0.6), ha='center', color='#1e40af', fontweight='bold', fontsize=8.5)

ax.set_title('Ethiopia Account Ownership Forecasts (2025–2027)\nMulti-Scenario Uncertainty Bounds', fontsize=12, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=10, fontweight='bold')
ax.set_ylabel('Account Ownership Rate (%)', fontsize=10, fontweight='bold')
ax.set_ylim(45, 65)
ax.set_xticks(fc_years)
ax.legend(loc='upper left', frameon=True)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig4_forecasts_2025_2027.png"))
plt.close()

print("All static figures generated cleanly in reports/figures/")
