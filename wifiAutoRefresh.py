import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up options for headless mode and to prevent the Chrome tab from closing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

url_path = "https://snsr.sunet.stanford.edu/snsr/intro"

def do():
    driver = webdriver.Chrome(options=options)  # Initialize the web driver with headless options
    driver.implicitly_wait(5)  # wait time
    driver.get(url_path)  # Navigate to the URL
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '#content > div.well.instruction > div:nth-child(3) > div:nth-child(2) > a').click()
    driver.implicitly_wait(1)
    driver.quit()  # Close the browser

cnt = 0
while True:
    do()
    cnt += 1
    print(cnt)
    time.sleep(250)