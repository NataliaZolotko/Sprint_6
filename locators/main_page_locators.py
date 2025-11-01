from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS = (By.XPATH, ".//div[@class='accordion__item']")
    QUESTIONS_BUTTON = (By.XPATH, ".//div[@class='accordion__button']")
    ANSWERS = (By.XPATH, "//div[@class='accordion__panel']")


    @staticmethod
    def question_button_number(question):
        return By.ID, f"accordion__heading-{question}"
    
    @staticmethod
    def answer_number(answer):
        return By.ID, f"accordion__panel-{answer}"