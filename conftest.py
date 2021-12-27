import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    print('ВЫБРАН ЯЗЫК:', lang)
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()