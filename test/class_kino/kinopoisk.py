from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest

@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(20) 
    browser.maximize_window()
    yield browser 
    browser.quit()

@allure.title("Поиск на русском языке") 
@allure.description("Тест проверяет поиск на русском языке") 
@allure.severity("blocker") 


class Kino:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        driver.get("https://www.kinopoisk.ru/")
        self._wait = WebDriverWait(driver,30) 
    
    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, ".styles_loginButton__LWZQp").click()
        self.driver.find_element (By.CSS_SELECTOR,'[placeholder="Логин или email"]').send_keys("1jqwotrnszno@mail.ru")
        self.driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()
        self.driver.find_element (By.CSS_SELECTOR, "[name='passwd']").send_keys("KXpbu=EV!x79ghT")
        self.driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()

    def login_visible(self):
        logo=self.driver.find_element(By.CSS_SELECTOR, ('[alt="Кинопоиск"]')).text
        return logo
    
    def seek_film(self):
        self.driver.find_element (By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]').send_keys("Майор Гром: Игра")
        self.driver.find_element (By.CSS_SELECTOR, '[aria-label="Найти"]').click()

    def seek_film_visible(self):
        movie = self.driver.find_element(By.XPATH, "//span[text='Майор Гром: Игра (2024)']").text
        return movie
    
    def estimation(self):
        self.driver.find_element (By.XPATH, '//span[text()="Изменить оценку"]').click()
        self.driver.find_element (By.XPATH, '//span[text()="Удалить оценку"]').click()
        self.driver.find_element (By.CSS_SELECTOR, '[data-tid="410c06ef"]').click()
        self.driver.find_element (By.XPATH, '//span[text()="10"]').click()
    
    def estimation_visible(self):
        est = self.driver.find_element(By.XPATH, "//span[text='Майор Гром: Игра (2024)']" ).text
        return est
    
    def seek_TV(self):
        self.driver.find_element (By.CSS_SELECTOR, '[data-tid="340369cf"]').click()
        self.driver.find_element (By.CSS_SELECTOR, '[alt="Кинопоиск"]').click()
        self.driver.find_element (By.XPATH, '//a[text()="Телеканалы"]').click()
        self._wait.until(EC.visibility_of_all_elements_located ((By.XPATH,'//button[text()="СТС"]')))
        self.driver.find_element (By.XPATH,'//button[text()="СТС"]').click() 
        self._wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Закрыть плеер"]')))

    def seek_TV_visible(self):
        TV = self.driver.driver.find_element(By.XPATH, '//button[text()="СТС"]' ).text 
        return TV
    
    def go_page (self):
        self.driver.find_element (By.CSS_SELECTOR,'[aria-label="Закрыть плеер"]').click() 
        self._wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Меню навигации"]')))
        self.driver.find_element (By.CSS_SELECTOR,'[aria-label="Кинопоиск"]').click()

    def go_page_visible(self):    
       page = driver.find_element (By.XPATH, '//a[text()="Кинопоиск"]').text 
       return page
