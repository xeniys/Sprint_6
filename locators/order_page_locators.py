from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')
    NAME_FIELD = (By.XPATH, './/input[@placeholder = "* Имя"]')
    SURNAME_FIELD = (By.XPATH, './/input[@placeholder = "* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]')
    SUBWAY_FIELD = (By.XPATH, './/input[@placeholder = "* Станция метро"]')
    SUBWAY_STATION_LST = [By.CLASS_NAME, 'select-search__options']
    SUBWAY_FIELD_SELECT = (By.XPATH, ".//li[@class = 'select-search__row']/button[@value = '6']/div[text() = 'Комсомольская']")
    PHONE_FIELD = (By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]')


    ABOUT_RENT_HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')

    DELIVERY_TIME = (By.XPATH, ".//input[@placeholder= '* Когда привезти самокат']")
    CALENDAR = (By.CLASS_NAME, 'react-datepicker__month')
    DATE = (By.XPATH,
                 ".//div[@class = 'react-datepicker__week']/div[@class = 'react-datepicker__day react-datepicker__day--005']")

    TIME_FIELD = (By.CLASS_NAME, 'Dropdown-control')
    TIME_DROPDOWN = (By.CLASS_NAME, 'Dropdown-menu')
    TIME_CHOOSE = (By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'трое суток']")
    COLOR_BLACK = (By.XPATH, ".//input[@id='black']")
    COLOR_GREY = (By.XPATH, ".//input[@id='grey']")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Заказать']")

    CONFIRM_MODAL = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    CONFIRM_BUTTON = (By.XPATH, ".//button[text() = 'Да']")

    ORDER_MODAL = (By.CLASS_NAME, 'Order_Modal__YZ-d3')

    SAMOKAT_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

