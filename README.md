# Forecasting Financial Inclusion in Ethiopia (2011–2027)

[![Continuous Integration - Unit Tests](https://github.com/Wave-eer/-Forecasting-Financial-Inclusion-in-Ethiopia/actions/workflows/unittests.yml/badge.svg)](https://github.com/Wave-eer/-Forecasting-Financial-Inclusion-in-Ethiopia/actions/workflows/unittests.yml)

## 📌 Executive Summary
This repository contains the end-to-end data enrichment, exploratory data analysis (EDA), event impact modeling, multi-scenario forecasting (2025–2027), and Streamlit dashboard application for tracking and projecting financial inclusion in Ethiopia.

---

## 🛠️ Project Structure

```
├── .github/
│   └── workflows/
│       └── unittests.yml          # GitHub Actions CI workflow
├── app/
│   └── main.py                    # Streamlit Dashboard application
├── data/
│   ├── ethiopia_fi_unified_data.csv# Enriched Unified Schema dataset
│   ├── ethiopia_fi_unified_data.xlsx# Original Excel dataset
│   ├── reference_codes.csv        # Indicator code definitions
│   └── data_enrichment_log.md     # Audit log of data additions
├── notebooks/
│   ├── 01_eda_and_enrichment.ipynb# EDA & trajectory analysis notebook
│   ├── 02_event_impact_modeling.ipynb# Association matrix & historical validation
│   └── 03_forecasting.ipynb       # 2025-2027 forecasts & scenario modeling
├── src/
│   ├── __init__.py
│   ├── data_loader.py             # DataRepository and schema parser
│   ├── impact_model.py            # EventImpactModel & lag functions
│   ├── forecasting.py             # FinancialInclusionForecaster engine
│   └── utils.py                   # Formatting & visualization utilities
├── tests/
│   ├── test_data_loader.py        # Unit tests for data loading
│   ├── test_impact_model.py       # Unit tests for impact modeling
│   └── test_forecasting.py        # Unit tests for forecasting
├── README.md                      # Comprehensive project documentation
└── requirements.txt               # Python package dependencies
```

---

## 📊 Summary of Implemented Tasks & Evaluation Criteria

### [TASK 1 & 2] Data Exploration, Enrichment, and EDA
1. **Dataset Loading**: Parsed and processed `ethiopia_fi_unified_data.csv`.
2. **Schema Understanding**: Implemented schema rules separating neutral `event` records from `observation`, `impact_link`, and `target` records.
3. **Data Enrichment**: Enriched dataset with 2011 baseline observations, EthSwitch P2P metrics, and 10+ explicit `impact_link` mappings.
4. **Enrichment Documentation**: Audited in `data/data_enrichment_log.md` with source URLs, confidence levels, and methodological rationale.
5. **EDA & Trajectory Analysis**: Analyzed account ownership growth (14% in 2011 to 49% in 2024) and documented the 2021–2024 growth slowdown (+1.0 pp/yr vs +2.75 pp/yr in 2017-2021).
6. **Key Insights**: Documented 5 core empirical insights with supporting charts.

### [TASK 3 & 4] Event Impact Modeling & 2025–2027 Forecasting
1. **Event-Indicator Association Matrix**: Joined `impact_links` with `events` via `parent_id`.
2. **Historical Validation**: Verified Telebirr launch (`EVT_0001`) estimate (+4.75 pp) against observed mobile money growth (4.7% in 2021 to 9.45% in 2024, delta = +4.75 pp).
3. **Methodology Documentation**: Modeled decay/lag structures (linear, sigmoidal, logarithmic).
4. **Multi-Scenario Forecasting**: Generated 2025–2027 predictions (Base, Optimistic, Pessimistic) with 95% confidence intervals.
5. **Target Gap Analysis**: Evaluated progress toward NFIS-II 70% national inclusion target.

### [TASK 5] Dashboard Development
1. **Streamlit Application**: Multi-page interactive application in `app/main.py`.
2. **Overview Cards**: Key KPI summary cards with trend indicators.
3. **Interactive Time Series & Filters**: Date sliders, indicator selectors, and historical timeline overlays.
4. **Forecast & Scenario Explorer**: Dynamic scenario selection (Optimistic / Base / Pessimistic) and confidence intervals.

---

## 🚀 Quick Start Guide

### 1. Installation
```bash
git clone https://github.com/Wave-eer/-Forecasting-Financial-Inclusion-in-Ethiopia.git
cd -Forecasting-Financial-Inclusion-in-Ethiopia
pip install -r requirements.txt
```

### 2. Run Unit Tests
```bash
python -m unittest discover -v tests
```

### 3. Launch Dashboard Application
```bash
streamlit run app/main.py
```
