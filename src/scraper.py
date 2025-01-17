from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from config.settings import (
    LINKEDIN_LOGIN_URL,
    LINKEDIN_JOBS_URL,
    USERNAME,
    PASSWORD,
    SCROLL_PAUSE_TIME,
)

def login_to_linkedin(driver):
    """
    Logs into LinkedIn using provided credentials.
    """
    print("Navigating to LinkedIn login page...")
    driver.get(LINKEDIN_LOGIN_URL)
    time.sleep(2)

    # Enter username and password
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)

    # Click the login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    print("Successfully logged into LinkedIn.")

def scrape_jobs(driver):
    """
    Scrapes job postings from LinkedIn and returns them as a list of dictionaries.
    """
    print("Navigating to LinkedIn jobs page...")
    driver.get(LINKEDIN_JOBS_URL)
    time.sleep(3)

    # Scroll to load more jobs
    print("Scrolling through job listings...")
    for _ in range(5):  # Adjust range for more scrolling
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

    print("Extracting job data...")
    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")
    job_data = []
    for job in jobs:
        try:
            title = job.find_element(By.CLASS_NAME, "job-card-list__title").text
            company = job.find_element(By.CLASS_NAME, "job-card-container__company-name").text
            location = job.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
            job_data.append({"Title": title, "Company": company, "Location": location})
        except Exception as e:
            print(f"Error extracting job data: {e}")

    print(f"Extracted {len(job_data)} job postings.")
    return job_data

if __name__ == "__main__":
    # Initialize WebDriver
    print("Initializing WebDriver...")
    driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
    try:
        # Log in to LinkedIn
        login_to_linkedin(driver)

        # Scrape job postings
        job_listings = scrape_jobs(driver)

        # Quit the driver
        driver.quit()

        # Save job data to CSV
        print("Saving job data to 'linkedin_jobs.csv'...")
        df = pd.DataFrame(job_listings)
        df.to_csv("../data/linkedin_jobs.csv", index=False)
        print("Job data saved successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
