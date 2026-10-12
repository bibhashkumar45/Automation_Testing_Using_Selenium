from selenium import webdriver
from selenium.webdriver.common.by import By
import time

for browser in ["chrome", "edge"]:

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Edge()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(3)

    print(browser, "- Dashboard opened!")

    input("Press Enter to close the browser...")

    driver.quit()