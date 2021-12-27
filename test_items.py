import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_is_true(browser):
    browser.get(link)
    wait = WebDriverWait(browser, 10)
    try:
        button_is = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')))
        button_value = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    except NameError as nameErr:
        print('Кнопки нет', nameErr)
    time.sleep(30)

    assert button_value.text == button_is.text, 'Кнопки нет'