import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()
tinder_url = os.getenv("TINDER_URL", "https://tinder.com/")
facebook_email = os.getenv("FACEBOOK_EMAIL", "")
facebook_password = os.getenv("FACEBOOK_PASSWORD", "")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(tinder_url)

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
login_facebook_button = driver.find_element(
    By.XPATH, value='//*[text()="Log in with Facebook"]'
)
login_facebook_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
)
email_input.send_keys(facebook_email)
sleep(2)

password_input = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password_input.send_keys(facebook_password)
password_input.send_keys(Keys.RETURN)
# wait long time since facebook asked for a manual validation
# you should do this manually
sleep(80)
print("Facebook login done")

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

# Allow button
allow_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]")
    )
)
allow_button.click()
sleep(5)

# Accept button
accept_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/button")
    )
)
accept_button.click()
sleep(5)

# I'll miss out button
ill_miss_out_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[2]")
    )
)
ill_miss_out_button.click()
sleep(5)

# SVG
# First time a pop up appears, to sell you a plan. This is a click in the X button
try:
    close_svg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div/div/div[4]/button/svg")
        )
    )
    close_svg.click()
    sleep(5)
except TimeoutException as e:
    print(e.__class__)
    print("No SVG found")

i = 0
while i < 100:
    try:
        # like button
        if i == 0:
            path = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button"
        else:
            path = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[5]/div/div[4]/button"

        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        like_button.click()
        i += 1
        print(f"Clicked {i} times")
        sleep(2)
    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)
