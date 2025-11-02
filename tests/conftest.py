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
    