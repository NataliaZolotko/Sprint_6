import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import *
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    @allure.step('Открываем страницу "Главная"')
    def open_main_page(self):
        self.open(main_site)
        self._assert_cookies()

    @allure.step('Соглашаемся с принятием кук')
    def _assert_cookies(self):
        try:
            self.click_on_element(MainPageLocators.ASSERT_COOKIE_BTN)
        except:
            pass
    
    
    @allure.step("Подождать загрузки списка вопросов")
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.QUESTIONS)

    @allure.step("Открыть вопрос")
    def click_on_question(self, question):
        question_locator = MainPageLocators.question_button_number(question)
        self.scroll_to_element(question_locator)
        self.wait_for_clickability(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравнить ответ текста в вопросе")
    def check_answers(self, question, expected_text):
        answer_locator = MainPageLocators.answer_number(question)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == expected_text
    
   
    


