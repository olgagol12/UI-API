import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests


# Базовый url
base_URL = "https://api.kinopoisk.dev/v1.4/"

# Заголовки 
headers = {
    "accept": "application/json",
    "X-API-KEY": "WFTJMHF-1BN4VZ4-JABV824-KNBV92M"
    }

# Найти фильм по id 
def test_seek_film_id():
    id = '685246'
    response = requests.get(base_URL, "movie/" + id, headers=headers)
    assert response.status_code == 200

# Найти фильм по названию
def test_seek_film_name():
    query = 'Игры'
    response = requests.get(base_URL + query, headers=headers)
    assert response.status_code == 200

# Поиск актера по id 
def test_seek_actor_id():
    id = "3720486"
    response = requests.get(base_URL, "movie/search?page=1&limit=10&query=" + id, headers=headers)
    assert response.status_code == 200

# Поиск актера по имени
def test_seek_actor_name():
    query = "Александр Сетейкин"
    response = requests.get(base_URL, "person/search?page=1&limit=10&query=" + query, headers=headers)
    assert response.status_code == 200

# Получить список стран фильмов
def test_list_countries():
    field="countries.name"
    response = requests.get(base_URL, "movie/possible/possible-values-by-field" + field, headers=headers)
    assert response.status_code == 200

