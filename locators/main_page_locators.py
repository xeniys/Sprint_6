from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = (By.CLASS_NAME, 'Home_HomePage__ZXKIX')
    ACCORDION_ITEMS = (By.CLASS_NAME, 'accordion')
    UP_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    DOWN_ORDER_BUTTON = (By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')


