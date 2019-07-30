import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es',
                    help="Choose language: es, fr or something else")


@pytest.fixture(scope="function")
def browser(request):
    #options from cmd line
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    #chrome or firefox
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    #some sleep for better view :)
    #time.sleep(10)
    browser.quit()
