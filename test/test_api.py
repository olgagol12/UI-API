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

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
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


driver.find_element (By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]').send_keys("лллл")
driver.find_element (By.CSS_SELECTOR, '[aria-label="Найти"]').click()
driver.find_element (By.CSS_SELECTOR, '[alt="Кинопоиск"]').click()

driver.find_element (By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]').send_keys("Благословение небожителей") #поиск фильма по названию
driver.find_element (By.CSS_SELECTOR, '[aria-label="Найти"]').click()



driver.find_element (By.XPATH, '//span[text()="Изменить оценку"]').click()



driver.find_element (By.XPATH, '//span[text()="Удалить оценку"]').click()

driver.find_element (By.CSS_SELECTOR, '[data-tid="410c06ef"]').click()


driver.find_element (By.XPATH, '//span[text()="10"]').click()

driver.find_element (By.CSS_SELECTOR, '[alt="Кинопоиск"]').click()
title = driver.title
print(title) 



totallabel = driver.find_element (By.XPATH, '//a[text()="Кинопоиск"]').text


def test_1():
    assert totallabel == "Кинопоиск"

sleep (5)

driver.quit()

sleep (20)