import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

_MINUTES_TO_RUN = 5
_TIMEOUT = _MINUTES_TO_RUN * 60


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

while time.time() < start_time + _TIMEOUT:
    cookie.click()
    diff_time = int(time.time() - start_time)

    if diff_time != 0 and diff_time % 5 == 0:
        best_element = find_most_expensive_element(float(money.text.replace(",", "")))

        if best_element:
            best_element.click()

print(driver.find_element(By.ID, value="cps").text)
driver.quit()
