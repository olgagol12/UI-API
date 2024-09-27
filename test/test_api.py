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

import requests



#найти фильм по id 
def test_api_id():
    base_URL = '"https://api.kinopoisk.dev/v1.4/movie/'
    headers = {
    "accept": "application/json",
    "X-API-KEY": "WFTJMHF-1BN4VZ4-JABV824-KNBV92M"
    }
    id = 2043475
    response = requests.get(base_URL + id, headers=headers)
    assert response.status_code == 200



#название фильма 

def test_api_name():
    base_URL = "https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query="
    headers = {
    "accept": "application/json",
    "X-API-KEY": "WFTJMHF-1BN4VZ4-JABV824-KNBV92M"
    }
    query = 'Игры'
    response = requests.get(base_URL + query, headers=headers)
    assert response.status_code == 200


#  поиск по id известной личности
def test_api_reshisor():
    base_URL = "https://api.kinopoisk.dev/v1.4/person/"
    headers = {
    "accept": "application/json",
    "X-API-KEY": "WFTJMHF-1BN4VZ4-JABV824-KNBV92M"
    }
    id = 200
    response = requests.get(base_URL + id, headers=headers)
    assert response.status_code == 200

#поиск актера 
def test_api_actor():
    base_URL = "https://api.kinopoisk.dev/v1.4/person/search?page=1&limit=10&query="
    headers = {
    "accept": "application/json",
    "X-API-KEY": "WFTJMHF-1BN4VZ4-JABV824-KNBV92M"
    }
    query = "Александр Сетейкин"
    response = requests.get(base_URL + query, headers=headers)
    assert response.status_code == 200



#коллекция фильмов 

def test_api_actor():
    base_URL = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/collections?type='
    headers = {
    "accept": "application/json",
    "X-API-KEY": "WFTJMHF-1BN4VZ4-JABV824-KNBV92M"
    }
    type = "TOP_POPULAR_ALL"
    response = requests.get(base_URL + type, headers=headers)
    assert response.status_code == 200

