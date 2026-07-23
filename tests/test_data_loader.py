import os
import unittest
from src.data_loader import DataRepository

class TestDataLoader(unittest.TestCase):
    
    def setUp(self):
        self.repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(self.repo_root, "data", "ethiopia_fi_unified_data.csv")
        self.repo = DataRepository(self.data_path)

    def test_load_records(self):
        self.assertTrue(len(self.repo.records) > 0, "Records should not be empty")

    def test_schema_record_types(self):
        obs = self.repo.get_observations()
        evts = self.repo.get_events()
        links = self.repo.get_impact_links()
        
        self.assertTrue(len(obs) > 0, "Should contain observation records")
        self.assertTrue(len(evts) > 0, "Should contain event records")
        self.assertTrue(len(links) > 0, "Should contain impact_link records")

    def test_neutral_events_schema(self):
        # Rule: event records should have empty pillar (no pre-assigned interpretation)
        evts = self.repo.get_events()
        for e in evts:
            self.assertEqual(e.get('pillar', '').strip(), '', f"Event {e.get('record_id')} should have empty pillar")

    def test_indicator_series_retrieval(self):
        series = self.repo.get_indicator_series('ACC_OWNERSHIP')
        self.assertTrue(len(series) >= 4, "Should retrieve account ownership series")

if __name__ == '__main__':
    unittest.main()
