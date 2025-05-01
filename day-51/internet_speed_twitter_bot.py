from dataclasses import dataclass
from time import sleep
from regex import B
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@dataclass
class Config:
    twitter_email: str
    twitter_password: str
    chrome_driver_path: str
    promised_down: int
    primised_up: int


class InternetSpeedTwitterBot:
    def __init__(self, config: Config):
        self._twitter_email = config.twitter_email
        self._twitter_password = config.twitter_password
        self._chrome_driver_path = config.chrome_driver_path
        self._promised_down = config.promised_down
        self._primised_up = config.primised_up
        self._upload_speed = 0
        self._download_speed = 0
        self._set_webdriver()

    def _set_webdriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.page_load_strategy = "eager"
        self._driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        print("Opening the speed test page")
        self._driver.get("https://www.speedtest.net/")
        sleep(2)

        wait = WebDriverWait(self._driver, 20)
        go_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[1]/a',
                )
            )
        )
        go_button.click()

        print("Waiting for the test to finish")
        sleep(60)

        self._download_speed = self._driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text
        self._upload_speed = self._driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        ).text
        print(f"Download speed: {self._download_speed}")
        print(f"Upload speed: {self._upload_speed}")

    def tweet_at_provider(self):
        self._driver.get("https://twitter.com/")
        sleep(2)
        sign_in_button = self._driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a',
        )
        sign_in_button.click()
        sleep(2)
        email_input = self._driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input',
        )
        email_input.send_keys(self._twitter_email)
        email_input.send_keys(Keys.RETURN)
        sleep(2)

        password_input = self._driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
        password_input.send_keys(self._twitter_password)
        password_input.send_keys(Keys.RETURN)
        sleep(5)

        tweet_button = self._driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a',
        )
        tweet_button.click()
        sleep(5)

        tweet_input = self._driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span',
        )
        tweet_input.send_keys(
            f"Hey, why is my internet speed {self._download_speed} down/{self._upload_speed} up when I pay for {self._promised_down}/{self._primised_up}?"
        )
        sleep(5)

        post_button = self._driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]',
        )
        post_button.click()
        print("Tweet sent")
        # self._driver.quit()
