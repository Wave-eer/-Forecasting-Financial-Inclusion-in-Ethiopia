import os
import unittest
from src.data_loader import DataRepository
from src.forecasting import FinancialInclusionForecaster

class TestForecasting(unittest.TestCase):
    
    def setUp(self):
        self.repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(self.repo_root, "data", "ethiopia_fi_unified_data.csv")
        self.repo = DataRepository(self.data_path)
        self.forecaster = FinancialInclusionForecaster(self.repo)

    def test_forecast_generation(self):
        fc = self.forecaster.forecast_indicator('ACC_OWNERSHIP', horizon_years=[2025, 2026, 2027])
        self.assertEqual(len(fc['forecasts']), 3)
        
        for f in fc['forecasts']:
            self.assertGreater(f['optimistic'], f['base_forecast'])
            self.assertGreater(f['base_forecast'], f['pessimistic'])
            self.assertGreater(f['ci_upper_95'], f['ci_lower_95'])

    def test_all_forecasts(self):
        all_fc = self.forecaster.generate_all_forecasts()
        self.assertIn('ACC_OWNERSHIP', all_fc)
        self.assertIn('ACC_MM_ACCOUNT', all_fc)
        self.assertIn('USG_P2P_COUNT', all_fc)

if __name__ == '__main__':
    unittest.main()
