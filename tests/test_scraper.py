import unittest
from selenium import webdriver
from src.scraper import login_to_linkedin, scrape_jobs
from config.settings import LINKEDIN_LOGIN_URL

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        try:
            login_to_linkedin(self.driver)
            self.assertIn("LinkedIn", self.driver.title)
        except Exception as e:
            self.fail(f"Login failed: {e}")

    def test_scrape_jobs(self):
        try:
            self.driver.get(LINKEDIN_LOGIN_URL)  # Ensure login is done first
            login_to_linkedin(self.driver)
            jobs = scrape_jobs(self.driver)
            self.assertGreater(len(jobs), 0, "No jobs were scraped.")
        except Exception as e:
            self.fail(f"Job scraping failed: {e}")

if __name__ == "__main__":
    unittest.main()
