import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TestPages(unittest.TestCase):
    def test_page_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        firstname = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        firstname.send_keys('Edd')

        lastname = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        lastname.send_keys('Second')

        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys('email@email.com')

        # Отправляем заполненную форму
        button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert ("Congratulations! You have successfully registered!", welcome_text, 'Произошла ошибка')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.close()
        browser.quit()

    def test_page_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        firstname = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        firstname.send_keys('Edd')

        lastname = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        lastname.send_keys('Second')

        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys('email@email.com')

        # Отправляем заполненную форму
        button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Произошла ошибка')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.close()
        browser.quit()


if __name__ == "__main__":
    unittest.main()