import pytest
from selenium import webdriver
from curl import *
from data import User_1
from data import User_2


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
    
@pytest.fixture(scope="function")
def order_user_1():
    # Учётные данные пользователя 1
    return {
        "name": User_1.name,
        "surname": User_1.surname,
        "address": User_1.address,
        "phone": User_1.phone,
      
    }
   

@pytest.fixture(scope="function")
def order_user_2():
    # Учётные данные пользователя 2
    return {
        "name": User_2.name,
        "surname": User_2.surname,
        "address": User_2.address,
        "phone": User_2.phone,
    }   