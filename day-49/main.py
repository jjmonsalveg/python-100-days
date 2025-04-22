from math import e
import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

_SECONDS_TO_WAIT_FOR_ELEMENT = 80


def _do_jobs_scroll(driver):
    scaffold_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".scaffold-layout__list"))
    )
    child_elements = scaffold_list.find_elements(By.XPATH, "./*")

    if len(child_elements) < 2:
        print("Scroll element not found.")
        driver.quit()

    scroll_container = child_elements[1]
    _scroll_function(driver, scroll_container)


def _scroll_function(driver, scroll_container):
    previous_height = driver.execute_script(
        "return arguments[0].scrollHeight", scroll_container
    )
    while True:
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container
        )
        sleep(2)
        current_height = driver.execute_script(
            "return arguments[0].scrollHeight", scroll_container
        )
        if current_height == previous_height:
            print("Scroll completed")
            break
        previous_height = current_height


def _do_job_scroll(driver):
    scaffold_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".jobs-search__job-details--wrapper")
        )
    )
    _scroll_function(driver, scaffold_list)


load_dotenv()
linkedin_jobs_url = os.getenv("LINKEDIN_JOBS_URL", "https://www.linkedin.com/jobs/")
linkedin_url = os.getenv("LINKEDIN_URL", "https://www.linkedin.com/")
linkedin_email = os.getenv("LINKEDIN_EMAIL", "")
linkedin_password = os.getenv("LINKEDIN_PASSWORD", "")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(linkedin_url)

username_input = driver.find_element(By.ID, value="username")
username_input.send_keys(linkedin_email)

password_input = driver.find_element(By.ID, value="password")
password_input.send_keys(linkedin_password)

button = driver.find_element(
    By.CSS_SELECTOR, value=".btn__primary--large.from__button--floating"
)
button.click()
try:
    search_job_input = WebDriverWait(driver, _SECONDS_TO_WAIT_FOR_ELEMENT).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                ".basic-input.jobs-search-box__text-input.jobs-search-box__keyboard-text-input.jobs-search-global-typeahead__input",
            )
        )
    )
    search_job_input.send_keys("Python Developer")
    search_job_input.send_keys(Keys.RETURN)

    easy_apply_button = WebDriverWait(driver, _SECONDS_TO_WAIT_FOR_ELEMENT).until(
        EC.presence_of_element_located((By.ID, "searchFilter_applyWithLinkedin"))
    )

    easy_apply_button.click()
    sleep(2)

    _do_jobs_scroll(driver)
    sleep(2)

    jobs = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

    for job in jobs:
        job.click()
        sleep(2)
        job_title = driver.find_element(
            By.CSS_SELECTOR,
            value=".job-details-jobs-unified-top-card__job-title > h1 > a",
        )
        job_company = driver.find_element(
            By.CSS_SELECTOR,
            value=".job-details-jobs-unified-top-card__company-name > a",
        )
        print(job_title.text)
        print(job_company.text)

        _do_job_scroll(driver)
        sleep(2)

        follow_button = driver.find_element(
            By.CSS_SELECTOR,
            value=".follow",
        )
        follow_button.click()
        sleep(2)
        print("=====================================")

except TimeoutException:
    driver.quit()

driver.quit()
