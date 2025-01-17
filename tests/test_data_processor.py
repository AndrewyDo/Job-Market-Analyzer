import unittest
import os
import pandas as pd
from src.data_processor import analyze_skills

class TestDataProcessor(unittest.TestCase):

    def test_analyze_skills(self):
        # Ensure the data file exists before running the test
        test_file_path = "../data/linkedin_jobs.csv"
        if not os.path.exists(test_file_path):
            self.skipTest("Test file does not exist: linkedin_jobs.csv")

        # Create a dummy CSV file for testing
        test_data = pd.DataFrame({
            "Title": ["Python Developer", "SQL Analyst", "Machine Learning Engineer"]
        })
        test_data.to_csv(test_file_path, index=False)

        # Run the skill analysis
        skill_counts = analyze_skills(test_file_path)
        self.assertGreater(len(skill_counts), 0, "No skills were analyzed.")
        self.assertIn("Python", skill_counts, "Skill 'Python' not found in analysis.")

        # Clean up
        os.remove(test_file_path)

if __name__ == "__main__":
    unittest.main()
