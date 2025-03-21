import math
import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

_MINUTES_TO_RUN = 5
_TIMEOUT = _MINUTES_TO_RUN * 60
_MAX_WAIT_TIME = _TIMEOUT * 0.375


def find_most_expensive_element(current_money: float):
    store = driver.find_element(By.ID, value="store")
    items = store.find_elements(By.CSS_SELECTOR, value="div:not(.grayed)>b")

    most_expensive_index = -1
    most_expensive_price = 0.0

    for index, item in enumerate(items):
        price = float(item.text.split("-")[1].strip().replace(",", ""))
        if price > most_expensive_price and price <= current_money:
            most_expensive_index = index
            most_expensive_price = price

    return items[most_expensive_index] if most_expensive_index != -1 else None


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")

start_time = time.time()
x = 1.0
checking_time = 2

while time.time() < start_time + _TIMEOUT:
    cookie.click()
    diff_time = int(time.time() - start_time)

    if diff_time != 0 and diff_time % checking_time == 0:
        best_element = find_most_expensive_element(float(money.text.replace(",", "")))

        if (
            start_time + _TIMEOUT - time.time() < checking_time
            or checking_time > _MAX_WAIT_TIME
        ):
            # we need to buy something before the time runs out
            # or we are taking too long to buy something
            print(
                "Time is running out, buying the best item available or taking too long to buy something"
            )
            x = 1.0

        checking_time = int(math.exp(x))
        x += 0.25

        print(f"Checking time: {checking_time} seconds")
        if best_element:
            try:
                best_element.click()
            except StaleElementReferenceException:
                # see https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/#stale-element-reference-exception
                print("Element is no longer attached to the DOM")

print(driver.find_element(By.ID, value="cps").text)
driver.quit()
