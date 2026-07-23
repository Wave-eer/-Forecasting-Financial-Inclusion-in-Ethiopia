import os
import unittest
from src.data_loader import DataRepository
from src.impact_model import EventImpactModel

class TestImpactModel(unittest.TestCase):
    
    def setUp(self):
        self.repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(self.repo_root, "data", "ethiopia_fi_unified_data.csv")
        self.repo = DataRepository(self.data_path)
        self.model = EventImpactModel(self.repo)

    def test_association_matrix_building(self):
        matrix = self.model.get_association_matrix_data()
        self.assertTrue(len(matrix) > 0, "Association matrix should contain rows")
        for row in matrix:
            self.assertIn('event_id', row)
            self.assertIn('target_indicator_code', row)
            self.assertIn('impact_estimate', row)

    def test_historical_validation(self):
        res = self.model.historical_validation()
        self.assertEqual(res['validation_status'], 'PASS')
        self.assertLess(res['percentage_error'], 10.0)

    def test_lagged_impact_calculation(self):
        # Linear lag test: half time elapsed = half impact
        linear_val = self.model.compute_lagged_impact(10.0, 6.0, 12.0, functional_form='linear')
        self.assertAlmostEqual(linear_val, 5.0)

if __name__ == '__main__':
    unittest.main()
