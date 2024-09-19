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
from selenium.webdriver.common.keys import Keys

from ui import Ui


@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(20) 
    browser.maximize_window()
    yield browser 
    browser.quit()

def test(driver):
        ui_page = Ui(driver)
        ui_page.registration()
        ui_page.seek_film()
        ui_page.seek_TV()
        ui_page.seek_menu()
        ui_page.text()
        te= ui_page.text()
        assert te == "Кинопоиск"

