import allure
import pytest

from data import Data
from pages.main_page import MainPage

class TestAnswersQuestion:
    @allure.title("Проверка текста ответов в разделе 'Вопросы о важном")
    @pytest.mark.parametrize('question, expected_text', Data.question_name)
    def test_question_names(self, driver, question, expected_text):
        # Arrange
       main_page = MainPage(driver)
       main_page.open_main_page()
       main_page.wait_for_questions_list()
        # Act
       main_page.click_on_question(question)
        # Assert
       assert main_page.check_answers(question, expected_text), \
            f"Текст ответа не совпадает. Ожидалось: '{expected_text}'"