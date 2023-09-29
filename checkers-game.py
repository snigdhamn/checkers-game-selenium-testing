from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.gamesforthebrain.com/game/checkers/")

assert "Checkers" in driver.title

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div[6]/img[6]"))
    )
    print("Orange piece found. Clicking...")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div[6]/img[6]").click()
    print("Clicked orange piece.")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/p[2]/a[1]"))
    )
    print("Restart button found. Clicking...")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/p[2]/a[1]").click()
    print("Clicked restart button.")
except Exception as e:
    print("Error occurred:", e)

if "game/checkers" in driver.current_url:
    pass

# Adding sleep here to verify if the click is working
# The code from here is very incomplete due to time constraints and can be discussed during the meeting.

import time

for move_count in range(5):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div[6]/img[6]").click()
    time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/p[2]/a[1]").click()
# Adding a 3-second sleep after clicking the restart button
time.sleep(3)

driver.close()
