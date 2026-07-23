import os
import csv
from typing import Dict, List, Tuple, Any

class DataRepository:
    """
    Data loader and manager for Ethiopia Financial Inclusion Unified Dataset.
    Handles observations, events, impact_links, and target records.
    """
    
    def __init__(self, data_path: str = None):
        if data_path is None:
            # Default path relative to repository root
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_path = os.path.join(base_dir, "data", "ethiopia_fi_unified_data.csv")
        self.data_path = data_path
        self.records = []
        self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """Load unified CSV file into memory."""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Dataset not found at {self.data_path}")
        
        with open(self.data_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.records = list(reader)
        return self.records

    def get_observations(self) -> List[Dict[str, Any]]:
        """Filter records of type 'observation'."""
        return [r for r in self.records if r.get('record_type') == 'observation']

    def get_events(self) -> List[Dict[str, Any]]:
        """Filter records of type 'event'."""
        return [r for r in self.records if r.get('record_type') == 'event']

    def get_impact_links(self) -> List[Dict[str, Any]]:
        """Filter records of type 'impact_link'."""
        return [r for r in self.records if r.get('record_type') == 'impact_link']

    def get_targets(self) -> List[Dict[str, Any]]:
        """Filter records of type 'target'."""
        return [r for r in self.records if r.get('record_type') == 'target']

    def get_indicator_series(self, indicator_code: str) -> List[Dict[str, Any]]:
        """Get time series observations for a specific indicator code."""
        obs = self.get_observations()
        matching = [r for r in obs if r.get('indicator_code') == indicator_code or r.get('related_indicator') == indicator_code]
        # Sort by year/date
        def extract_year(r):
            fy = r.get('fiscal_year', '')
            ob_date = r.get('observation_date', '')
            if fy and fy.replace('.', '', 1).isdigit():
                return float(fy)
            if ob_date and ob_date.replace('.', '', 1).isdigit():
                val = float(ob_date)
                if val > 30000: # Excel date serial
                    return 1900 + (val / 365.25)
                return val
            return 2020.0
        return sorted(matching, key=extract_year)

    def to_pandas_dataframes(self):
        """Convert repository into pandas DataFrames for advanced EDA/Modeling."""
        try:
            import pandas as pd
            df = pd.read_csv(self.data_path)
            
            # Clean numeric values
            df['value_numeric'] = pd.to_numeric(df['value_numeric'], errors='coerce')
            df['fiscal_year_clean'] = pd.to_numeric(df['fiscal_year'], errors='coerce')
            df['impact_estimate'] = pd.to_numeric(df['impact_estimate'], errors='coerce')
            df['lag_months'] = pd.to_numeric(df['lag_months'], errors='coerce')
            
            obs_df = df[df['record_type'] == 'observation'].copy()
            evt_df = df[df['record_type'] == 'event'].copy()
            imp_df = df[df['record_type'] == 'impact_link'].copy()
            tgt_df = df[df['record_type'] == 'target'].copy()
            
            return {
                'full': df,
                'observations': obs_df,
                'events': evt_df,
                'impact_links': imp_df,
                'targets': tgt_df
            }
        except ImportError:
            raise ImportError("pandas library is required for to_pandas_dataframes()")

def load_unified_data(data_path: str = None) -> DataRepository:
    """Factory helper to load DataRepository."""
    return DataRepository(data_path)
