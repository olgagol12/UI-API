import pytest
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #вызов веб драйвер
actions = ActionChains (driver) 
wait = WebDriverWait(driver,30) 
driver.get("https://ya.ru")
driver.get ("https://www.kinopoisk.ru/")





driver.find_element (By.CSS_SELECTOR, ".styles_loginButton__LWZQp").click()
driver.find_element (By.CSS_SELECTOR,'[placeholder="Логин или email"]').send_keys("1jqwotrnszno@mail.ru")
driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()
wait.until(EC.visibility_of_all_elements_located ((By.XPATH,'//span[text()= "Отправить письмо для входа"]')))
driver.find_element (By.CSS_SELECTOR, "[name='passwd']").send_keys("KXpbu=EV!x79ghT")
driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()

wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Фильмы, сериалы, персоны"]')))
driver.find_element (By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]').send_keys("Майор Гром: Игра")
driver.find_element (By.CSS_SELECTOR, '[aria-label="Найти"]').click()
driver.find_element (By.CSS_SELECTOR, '[aria-label="Все детали"]').click()
sleep(5)
driver.find_element (By.CSS_SELECTOR, '[data-tid="340369cf"]').click()
driver.find_element (By.CSS_SELECTOR, '[alt="Кинопоиск"]').click()
driver.find_element (By.XPATH, '//a[text()="Телеканалы"]').click()
wait.until(EC.visibility_of_all_elements_located ((By.XPATH,'//button[text()="СТС"]')))
driver.find_element (By.XPATH,'//button[text()="СТС"]').click() 
sleep (5)
wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Закрыть плеер"]')))
driver.find_element (By.CSS_SELECTOR,'[aria-label="Закрыть плеер"]').click() 
wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[aria-label="Меню навигации"]')))
driver.find_element (By.CSS_SELECTOR,'[aria-label="Кинопоиск"]').click() 



sleep (10)

totallabel = driver.find_element (By.XPATH, '//a[text()="Кинопоиск"]').text


def test_1():
    assert totallabel == "Кинопоиск"

sleep (5)

driver.quit()