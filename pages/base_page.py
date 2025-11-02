import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
       
    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()
    
    @allure.step("Подождать кликабельности элемента")
    def wait_for_clickability(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))
    
    @allure.step("Ждём появления списка (минимум 1 элемент)")
    def wait_for_list(self,locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    
    
    @allure.step("Ждем, что URL содержит указанный текст")    
    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
    
    @allure.step("Получаем handle текущего окна") 
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    @allure.step("Получаем список всех handles окон") 
    def get_window_handles(self):
        return self.driver.window_handles
    
    @allure.step("Переключаемся на указанное окно") 
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
    
    @allure.step("Получаем URL") 
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Закрытие текущего окно") 
    def close_current_window(self):
        self.driver.close()
    
    @allure.step("Ожидание появления нового окна") 
    def wait_for_new_window(self, original_windows, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda driver: len(driver.window_handles) > len(original_windows))
        # находим новое окно
        for window_handle in self.driver.window_handles:
            if window_handle not in original_windows:
                return window_handle
        return None
    
   