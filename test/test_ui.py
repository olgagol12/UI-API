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
import allure

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from ui import Ui


@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(20) 
    browser.maximize_window()
    yield browser 
    browser.quit()


@allure.title("Поиск книги на русском языке") 
@allure.description("Тест проверяет поиск книги на русском языке") 
@allure.severity("blocker") 
@allure.registration

def test_regestrasion(driver, wait):
    driver.get("https://www.chitai-gorod.ru/")
    with allure.step("Добавлены ожидания и открытие окна"): 
        driver.implicitly_wait(10)
        driver.maximize_window()
    with allure.step("Выполнение регистрацию"): 
        driver.find_element (By.CSS_SELECTOR, ".styles_loginButton__LWZQp").click()
        driver.find_element (By.CSS_SELECTOR,'[placeholder="Логин или email"]').send_keys("1jqwotrnszno@mail.ru")
        driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()
        wait.until (EC.visibility_of_all_elements_located ((By.XPATH,'//span[text()= "Отправить письмо для входа"]')))
        driver.find_element (By.CSS_SELECTOR, "[name='passwd']").send_keys("KXpbu=EV!x79ghT")
        driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()
        wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Фильмы, сериалы, персоны"]')))
        assert "Кинопоиск" in driver.find_element(By.CSS_SELECTOR, ('[alt="Кинопоиск"]')).text    


def test_seek_film(driver):
    with allure.step(): 
        driver.find_element (By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]').send_keys("Майор Гром: Игра")
        driver.find_element (By.CSS_SELECTOR, '[aria-label="Найти"]').click()
        assert "Майор Гром: Игра (2024)" in driver.find_element(By.XPATH, "//span[text='Майор Гром: Игра (2024)']" ).text    



def test_seek_TV (driver, wait):
    with allure.step():
        driver.find_element (By.CSS_SELECTOR, '[data-tid="340369cf"]').click()
        driver.find_element (By.CSS_SELECTOR, '[alt="Кинопоиск"]').click()
        driver.find_element (By.XPATH, '//a[text()="Телеканалы"]').click()
        wait.until(EC.visibility_of_all_elements_located ((By.XPATH,'//button[text()="СТС"]')))
        driver.find_element (By.XPATH,'//button[text()="СТС"]').click() 
        wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Закрыть плеер"]')))
        assert "СТС" in driver.find_element(By.XPATH, '//button[text()="СТС"]' ).text    


def test_seek_menu (driver, wait):
    with allure.step():    
        driver.find_element (By.CSS_SELECTOR,'[aria-label="Закрыть плеер"]').click() 
        wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Меню навигации"]')))
        driver.find_element (By.CSS_SELECTOR,'[aria-label="Кинопоиск"]').click() 




        

         
    
