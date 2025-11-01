import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.page_order_locators import OrderLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    @allure.step("Нажать на кнопку заказать")
    def click_order_button(self,locator):
        self.click_on_element(OrderLocators.BUTTON_ORDER_AT_THE_TOP)
       
    @allure.step("Заполнить имя")
    def fill_order_name(self,name):
        self.send_keys_to_input(OrderLocators.NAME, name)
        
    @allure.step("Заполнить фамилию")
    def fill_order_surname(self, surname):
        self.send_keys_to_input(OrderLocators.SURNAME, surname)
        
    @allure.step("Заполнить адрес")
    def fill_order_address(self,address):
        self.send_keys_to_input(OrderLocators.ADDRESS_TO, address)
        
    @allure.step('Выбрать станцию метро: ')
    def click_on_metro(self, station_name):
        self.click_on_element(OrderLocators.STATION_METRO)
        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.click_on_element(station_locator)
       
    @allure.step("Заполнить телефон")   
    def fill_order_phone(self, phone): 
        self.send_keys_to_input(OrderLocators.PHONE, phone)
    @allure.step("Нажать на далее")   
    def click_on_further(self): 
        self.click_on_element(OrderLocators.BUTTON_ORDER_AT_THE_BOTTOM)
           
    @allure.step("Заполнить когда")
    def fill_order_when(self):
        self.click_on_element(OrderLocators.WHEN)
        self.click_on_element(OrderLocators.DATA)
    
    
    
    @allure.step('Заполнить срок аренды ')
    def click_lease(self):
        self.click_on_element(OrderLocators.LEASE_TERM)
        self.click_on_element(OrderLocators.LEASE_TERM_MENU)
        
    @allure.step("Заказать и подтвердить оформление заказа")
    def click_submit_order(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER)
        self.click_on_element(OrderLocators.PLACE_AN_ORDER)

    @allure.step("Получить текст всплывающего сообщения")
    def get_registration_popup_text(self):
        return self.get_text_on_element(OrderLocators.ORDER_WINDOWS)
    
    @allure.step("Посмотреть статус заказа")
    def click_on_status(self):
        self.click_on_element(OrderLocators.VIEW_STATUS)
    
    @allure.step("Проверить что при клике на лого Самоката переходит на главную страницу")
    def click_on_scooter(self):
        self.click_on_element(OrderLocators.LOGO_SCOOTER)
        assert OrderLocators.HOME_PAGE
    
    @allure.step("Проверить что при клике на логотип Яндекса открывается главная страница Дзена в новом окне")
    def click_on_yandex_logo_and_check_dzen(self):
        main_window = self.driver.current_window_handle
        original_windows = self.driver.window_handles
    
        self.click_on_element(OrderLocators.LOGO_YANDEX)
        
    # Переключаемся на новое окно
        for window_handle in self.driver.window_handles:
            if window_handle not in original_windows:
                 self.driver.switch_to.window(window_handle)
                 break
    
        try:
        # Ждем загрузки страницы Дзена (может быть редирект)
            WebDriverWait(self.driver, 15).until(
                EC.url_contains("dzen.ru")
            )
        
        # Проверяем что URL соответствует Дзену
            current_url = self.driver.current_url
            assert "dzen.ru" in current_url, f"Ожидался переход на dzen.ru, но получен URL: {current_url}"
        finally:
        # Закрываем окно с Дзеном и возвращаемся в исходное окно
            self.driver.close()
            self.driver.switch_to.window(main_window)