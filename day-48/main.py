from tkinter import Button

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# url = "https://www.amazon.com.mx/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
url = "https://www.python.org/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
# print(f"Price: ${price_dollar}.{price_cents}")

search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
# print(button.size)

documentation_link = driver.find_element(
    By.CSS_SELECTOR, value=".documentation-widget a"
)
# print(documentation_link.text)

bug_link = driver.find_element(
    By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
)
# print(bug_link.text)

# find all upcoming events
li_upcoming_events = driver.find_elements(
    By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li'
)

event_dict: dict = {}

for index, event in enumerate(li_upcoming_events):
    event_date_time = event.find_element(By.TAG_NAME, value="time").get_attribute(
        "datetime"
    )

    if event_date_time:
        event_date = event_date_time.split("T")[0]

    event_name = event.find_element(By.TAG_NAME, value="a").text

    event_dict[index] = {"time": event_date, "name": event_name}

print(event_dict)

# close the tab
# driver.close()

# close the browser
driver.quit()
