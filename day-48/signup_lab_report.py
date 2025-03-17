from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

name_input = driver.find_element(By.NAME, value="fName")
name_input.send_keys("John")

last_name_input = driver.find_element(By.NAME, value="lName")
last_name_input.send_keys("Doe")

email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys("john.doe@gmail.com")

button = driver.find_element(
    By.CSS_SELECTOR, value="button.btn.btn-lg.btn-primary.btn-block"
)
button.click()
