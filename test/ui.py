from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Ui:


    def __init__(self, driver ): 
        self._driver = driver
        self._driver.get("https://www.kinopoisk.ru/")
        self.actions = ActionChains (driver) 
        self._wait = WebDriverWait(driver,30) 





    def registration(self):
        self._driver.find_element (By.CSS_SELECTOR, ".styles_loginButton__LWZQp").click()
        self._driver.find_element (By.CSS_SELECTOR,'[placeholder="Логин или email"]').send_keys("1jqwotrnszno@mail.ru")
        self._driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()
        self._wait.until (EC.visibility_of_all_elements_located ((By.XPATH,'//span[text()= "Отправить письмо для входа"]')))
        self._driver.find_element (By.CSS_SELECTOR, "[name='passwd']").send_keys("KXpbu=EV!x79ghT")
        self._driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()
        self._wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Фильмы, сериалы, персоны"]')))

    

    def seek_film(self):
        self._driver.find_element (By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]').send_keys("Майор Гром: Игра")
        self._driver.find_element (By.CSS_SELECTOR, '[aria-label="Найти"]').click()
        self._driver.find_element (By.CSS_SELECTOR, '[aria-label="Все детали"]').click()

    def seek_TV(self):
        self._driver.find_element (By.CSS_SELECTOR, '[data-tid="340369cf"]').click()
        self._driver.find_element (By.CSS_SELECTOR, '[alt="Кинопоиск"]').click()
        self._driver.find_element (By.XPATH, '//a[text()="Телеканалы"]').click()
        self._wait.until(EC.visibility_of_all_elements_located ((By.XPATH,'//button[text()="СТС"]')))
        self._driver.find_element (By.XPATH,'//button[text()="СТС"]').click() 
        self._wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Закрыть плеер"]')))


    def seek_menu(self):
        self._driver.find_element (By.CSS_SELECTOR,'[aria-label="Закрыть плеер"]').click() 
        self._wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Меню навигации"]')))
        self._driver.find_element (By.CSS_SELECTOR,'[aria-label="Кинопоиск"]').click() 


    def text(self):
        totallabel = self._driver.find_element (By.XPATH, '//a[text()="Кинопоиск"]')
        totallabel.text
        return ("Кинопоиск")
 
