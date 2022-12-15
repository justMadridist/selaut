import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:    
    browser = webdriver.Chrome()
    #browser.implicitly_wait(12)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, "book")
    prc = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    if prc:    
        button.click()
    treasure = browser.find_element(By.ID, "input_value").text
    y = calc(treasure)
    element = browser.find_element(By.CSS_SELECTOR, "#answer")
    element.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
