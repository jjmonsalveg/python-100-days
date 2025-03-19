from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

statistics_link = driver.find_element(
    By.CSS_SELECTOR,
    value='#articlecount > ul > li:nth-child(2) > a[title="Special:Statistics"]',
)

print(statistics_link.text)
# statistics_link.click()

# Find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" input by Name
search = driver.find_element(By.NAME, value="search")
# It is not working because the search input is not interactable
# search.send_keys("Python", Keys.ENTER)

# driver.quit()
