import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from class_kino.kinopoisk import Kino


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


# Авторизация
def test_log():
    logi = Kino
    with allure.step("Выполнение авторизации"): 
        logi.login
    with allure.step("авторизация прошла успешно"): 
        assert True 

# Поиск фильма
def test_film():
    logi = Kino
    with allure.step("Авторизация"): 
        logi.login
    with allure.step("Поиск фильма"): 
        logi.seek_film
    with allure.step("Проверки"):
        assert "Майор Гром: Игра (2024)"

# Оценка фильма
def test_estimation():
    logi = Kino
    with allure.step("Авторизация"): 
        logi.login
    with allure.step("Поиск фильма"): 
        logi.seek_film
    with allure.step("Оценка"): 
        logi.estimation
    with allure.step("Проверки"):
        assert "Майор Гром: Игра (2024)"

# Поиск канала 
def test_TV():
    logi = Kino
    with allure.step("Авторизация"): 
        logi.login
    with allure.step("TV"): 
        logi.seek_TV
    with allure.step("Проверки"):
        assert "СТС"

# Переход на главную страницу
def test_page():
    logi = Kino
    with allure.step("Авторизация"): 
        logi.login
    with allure.step("TV"): 
        logi.seek_TV
    with allure.step("главная страница"): 
        logi.go_page
    with allure.step("Проверки"):
        assert "Кинопоиск"
