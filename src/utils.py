"""
Utility Module for Financial Inclusion Visualizations, Formatting, and Helper Functions.
"""

from typing import Dict, List, Any

def format_number(val: float, unit: str = "") -> str:
    """Format numbers into human readable string representations (K, M, B, %)."""
    if val is None:
        return "N/A"
    
    try:
        val = float(val)
    except (ValueError, TypeError):
        return str(val)

    if unit == "%" or "rate" in unit.lower() or "percent" in unit.lower():
        return f"{val:.1f}%"
    elif val >= 1e9:
        return f"{val / 1e9:.2f}B {unit}".strip()
    elif val >= 1e6:
        return f"{val / 1e6:.2f}M {unit}".strip()
    elif val >= 1e3:
        return f"{val / 1e3:.1f}K {unit}".strip()
    else:
        return f"{val:.2f} {unit}".strip()

def get_pillar_color(pillar: str) -> str:
    """Return color palette code for specific financial inclusion pillars."""
    colors = {
        'ACCESS': '#1f77b4',       # Deep Blue
        'USAGE': '#2ca02c',        # Vibrant Green
        'AFFORDABILITY': '#ff7f0e',# Warm Amber
        'GENDER': '#e377c2',       # Pinkish Violet
        'QUALITY': '#9467bd',      # Purple
        'TRUST': '#8c564b',        # Earthy Brown
        'DEPTH': '#17becf'         # Cyan
    }
    return colors.get(str(pillar).upper(), '#7f7f7f')
