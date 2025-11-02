import allure
import pytest
from data import User_1, User_2
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.page_order_locators import OrderLocators

class TestLogo:
    @allure.title("Проверка перехода на главную страницу через логотип Самоката")
    def test_click_on_scooter_logo(self,driver):
        main_page = MainPage(driver)
        order_page = OrderPage (driver)
        main_page.open_main_page()
        order_page.click_order_button(OrderLocators.BUTTON_ORDER_AT_THE_TOP)
        order_page.click_on_scooter()
        current_url = order_page.get_current_url().lower()
        assert "scooter" in current_url, f"Ожидался переход на главную страницу, но URL: {current_url}"
        assert order_page.is_main_page_loaded()
        
    @allure.title("Проверка перехода на Дзен через логотип Яндекса")
    def test_click_on_yandex_logo(self,driver): 
        main_page = MainPage(driver)
        order_page = OrderPage (driver)
        main_page.open_main_page()
        main_window = order_page.get_current_window_handle()
        original_windows = order_page.get_window_handles()
        order_page.click_on_yandex_logo()
        dzen_url, dzen_window = order_page.check_dzen_opened(original_windows)
        assert dzen_url is not None, "Новое окно с Дзеном не открылось"
        assert "dzen.ru" in dzen_url, f"Должен открыться Дзен, но URL: {dzen_url}"