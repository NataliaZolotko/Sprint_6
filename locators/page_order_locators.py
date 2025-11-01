from selenium.webdriver.common.by import By


class OrderLocators:
    BUTTON_ORDER_AT_THE_TOP = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    BUTTON_ORDER_AT_THE_BOTTOM = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_TO = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_METRO = (By.XPATH, ".//input[contains(@placeholder,'* Станция метро')]")
    PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    WHEN = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATA = (By.XPATH, "//div[@aria-label='Choose понедельник, 10-е ноября 2025 г.']")
    LEASE_TERM = (By.XPATH, "//div[@aria-haspopup='listbox']")
    LEASE_TERM_MENU = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='двое суток']")
    BUTTON_ORDER = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    PLACE_AN_ORDER = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Да']")
    ORDER_WINDOWS = (By.XPATH, ".//div[text()='Заказ оформлен']")
    
    VIEW_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
    LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    HOME_PAGE = (By.XPATH, "//div[@class='Home_HomePage__ZXKIX']")
    LOGO_YANDEX = (By.XPATH, "//a[@target='_blank']")
    YANDEX_PAGE = (By.XPATH, "//body[@class='Theme utilityfocus _theme_white Theme_color_light Theme_root_light']")
   
   