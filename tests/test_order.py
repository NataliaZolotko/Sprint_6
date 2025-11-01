import allure
import pytest


import data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.page_order_locators import OrderLocators


class TestOrder:
    @allure.title("Заказ самоката: {user_data[name]} через {button_type} кнопку")
    @pytest.mark.parametrize('button_type,user_fixture', [
        (OrderLocators.BUTTON_ORDER_AT_THE_TOP, 'order_user_1'),
        (OrderLocators.BUTTON_ORDER_AT_THE_BOTTOM, "order_user_2")
    ])
    def test_question_names(self, driver, button_type, user_fixture, request):
        user_data = request.getfixturevalue(user_fixture)
        main_page = MainPage(driver)
        order_page = OrderPage (driver)
        main_page.open_main_page()
        order_page.click_order_button(button_type)
        order_page.fill_order_name(user_data['name'])
        order_page.fill_order_surname(user_data['surname'])
        order_page.fill_order_address(user_data['address'])
        order_page.click_on_metro('Черкизовская')
        order_page.fill_order_phone(user_data['phone'])
        order_page.click_on_further()
        order_page.fill_order_when()
        order_page.click_lease()
        order_page.click_submit_order()
        assert "Заказ оформлен" in order_page.get_registration_popup_text(), "Ошибка: текст не содержит 'Заказ оформлен'"

        order_page.click_on_status()
        order_page.click_on_scooter()
        order_page.click_on_yandex_logo_and_check_dzen()
        



        
        
       