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
actions = ActionChains (driver) #двойноц клик
wait = WebDriverWait(driver,30) #ожидание 5 сек 
driver.get("https://ya.ru")
driver.get ("https://www.kinopoisk.ru/")


driver.find_element (By.CSS_SELECTOR, "[width= '24px']").click()
driver.find_element (By.CSS_SELECTOR, ".styles_loginButton__LWZQp").click()
driver.find_element (By.CSS_SELECTOR,'[placeholder="Логин или email"]').send_keys("1jqwotrnszno@mail.ru")
driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()
wait.until(EC.visibility_of_all_elements_located ((By.XPATH,'//span[text()= "Отправить письмо для входа"]')))
driver.find_element (By.CSS_SELECTOR, "[name='passwd']").send_keys("KXpbu=EV!x79ghT")
driver.find_element (By.CSS_SELECTOR, '[type="submit"]').click()
wait.until(EC.visibility_of_all_elements_located ((By.CSS_SELECTOR,'[class="TitleWithDescription TitleWithDescription_marginBottom_24"]')))
sleep (5)
#driver.find_element (By.CSS_SELECTOR, ".Button2.Button2_size_xxl.Button2_view_contrast-pseudo.Button2_width_max").click()
driver.find_element (By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]').send_keys("Майор Гром: Игра")
driver.find_element (By.CSS_SELECTOR, '[aria-label="Найти"]').click()
sleep(5)