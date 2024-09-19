import pytest
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from api import Api

@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(20) 
    browser.maximize_window()
    yield browser 
    browser.quit()


def test(driver):
        api_page = Api(driver)
        api_page.registration()
        api_page.not_film()
        api_page.name_film()
        api_page.ocenka()
        api_page.kino()
        text = api_page.kino()
        assert text == ("Кинопоиск")














