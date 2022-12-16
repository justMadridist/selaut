import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def chk(browser, cssselector):
    try:
        browser.find_element(By.CSS_SELECTOR, cssselector)
    except NoSuchElementException:
        return False
    return True

@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1', 
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'])
def test_login(browser, link):
        browser.get(link)
        entr = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
        entr.click()
        lgin = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        lgin.send_keys('login')
        pswrd = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        pswrd.send_keys('password')
        entr = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        entr.click()
        time.sleep(3)
        if chk(browser, "button.again-btn"):
            browser.find_element(By.CSS_SELECTOR, "button.again-btn").click()
            time.sleep(3)
        ans = browser.find_element(By.CSS_SELECTOR, "textarea")
        ans.send_keys(math.log(int(time.time())))
        but = WebDriverWait(browser, 5).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
             )
        but.click()
        check = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        assert check.text == 'Correct!'


