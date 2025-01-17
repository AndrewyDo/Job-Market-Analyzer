import unittest
import os
from dash.testing.application_runners import import_app

class TestDashboard(unittest.TestCase):

    def test_dashboard(self):
        # Ensure the skill analysis file exists
        skill_file_path = "../data/skill_analysis.json"
        if not os.path.exists(skill_file_path):
            self.skipTest("Skill analysis file does not exist: skill_analysis.json")

        # Launch the dashboard app
        app = import_app("src.dashboard")
        self.assertIsNotNone(app, "Failed to import the dashboard app.")

if __name__ == "__main__":
    unittest.main()

