from dataclasses import dataclass
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException


@dataclass
class Config:
    instagram_email: str
    instagram_password: str
    similar_account: str


class FollowerInstagramBot:
    def __init__(self, config: Config):
        self._instagram_email = config.instagram_email
        self._instagram_password = config.instagram_password
        self._similar_account = config.similar_account
        self._set_webdriver()

    def _set_webdriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.page_load_strategy = "eager"
        self._driver = webdriver.Chrome(options=chrome_options)

    def login_provider(self):
        self._driver.get("https://www.instagram.com/")
        sleep(2)
        email_input = self._driver.find_element(
            By.XPATH,
            value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input',
        )
        email_input.send_keys(self._instagram_email)
        email_input.send_keys(Keys.RETURN)
        sleep(2)

        password_input = self._driver.find_element(
            By.XPATH,
            value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input',
        )
        password_input.send_keys(self._instagram_password)
        password_input.send_keys(Keys.RETURN)
        sleep(10)

    def find_followers(self):
        self._driver.get("https://www.instagram.com/juezcentral/")

        followers_link = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a",
                )
            )
        )
        followers_link.click()
        sleep(3)

        scroll_container = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]",
                )
            )
        )
        self._scroll_function(scroll_container)

    def _scroll_function(self, scroll_container):
        previous_height = self._driver.execute_script(
            "return arguments[0].scrollHeight", scroll_container
        )
        while True:
            self._driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container
            )
            sleep(2)
            current_height = self._driver.execute_script(
                "return arguments[0].scrollHeight", scroll_container
            )
            if current_height == previous_height:
                print("Scroll completed")
                break
            previous_height = current_height

    def follow(self):
        follower_container = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div",
                )
            )
        )

        follow_buttons = follower_container.find_elements(
            By.XPATH, ".//button[.//div[text()='Follow']]"
        )

        print(f"Found {len(follow_buttons)} follow buttons.")

        for btn in follow_buttons:
            try:
                btn.click()
                time.sleep(1)  # sleep to simulate human interaction
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(
                    by=By.XPATH, value="//button[contains(text(), 'Cancel')]"
                )
                cancel_button.click()
