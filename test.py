import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links_url = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('links', links_url)
class TestPageResults:
    """ Заполнение форм и поиск ответа """
    def test_parametrize(self, browser, links):
        wait = WebDriverWait(browser, 10)
        print("start test_parametrize")
        browser.get(links)
        browser.implicitly_wait(3)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//textarea')))
            textarea = browser.find_element(By.XPATH, '//textarea')
            textarea.send_keys(str(math.log(int(time.time()) - 14720.6)))
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'submit-submission')))
            button_submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
            button_submit.click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//pre[@class="smart-hints__hint"]')))
        except NameError as nameErr:
            print('Ошибка парсинга ответа', nameErr)

        answer_message = browser.find_element(By.XPATH, '//pre[@class="smart-hints__hint"]').text
        print(answer_message)
        assert answer_message == 'Correct!', 'Неверный код!'

        print("finish test_parametrize")

