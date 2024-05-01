import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Открыть страницу с заказом в Самокате')
    def loading_order_page(self):
        return self.find_element_located(OrderPageLocators.ORDER_HEADER)

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        return self.find_element_located(OrderPageLocators.NAME_FIELD).send_keys(name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_surname(self, surname):
        return self.find_element_located(OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        return self.find_element_located(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    @allure.step('Нажать на  поле "Метро"')
    def click_on_subway_station_field(self):
        return self.find_element_clickable(OrderPageLocators.SUBWAY_FIELD)

    @allure.step('Просколлить список метро до нужной станции')
    def scroll_to_subway_station(self):
        subway_station = self.find_element_located(OrderPageLocators.SUBWAY_FIELD_SELECT)
        self.scroll_elements(subway_station)

    def wait_for_subway_station(self):
        return self.find_element_located(OrderPageLocators.SUBWAY_STATION_LST)

    @allure.step('Выбрать нужную станцию метро')
    def set_subway(self):
        return self.find_element_clickable(OrderPageLocators.SUBWAY_FIELD_SELECT)

    @allure.step('Заполнить поле "Номер"')
    def set_phone(self, phone):
        return self.find_element_located(OrderPageLocators.PHONE_FIELD).send_keys(phone)

    @allure.step('Нажать на кнопку продолжения')
    def click_next_button(self):
        return self.find_element_clickable(OrderPageLocators.NEXT_BUTTON)

    def wait_order_about_loading(self):
        return self.find_element_located(OrderPageLocators.ABOUT_RENT_HEADER)

    def click_on_delivery_time_field(self):
        return self.find_element_clickable(OrderPageLocators.DELIVERY_TIME)

    @allure.step('Найти поле "Когда привезти самокат"')
    def loading_month_calendar(self):
        return self.find_element_located(OrderPageLocators.CALENDAR)

    @allure.step('Выбрать дату начала аренды')
    def choose_the_date(self):
        return self.find_element_clickable(OrderPageLocators.DATE)

    @allure.step('Найти поле "Срок аренды"')
    def click_rent_field(self):
        return self.find_element_clickable(OrderPageLocators.TIME_FIELD)

    def wait_rent_dropdown_show(self):
        return self.find_element_located(OrderPageLocators.TIME_DROPDOWN)

    @allure.step('Выбрать срок аренды')
    def choose_rent_time(self):
        return self.find_element_clickable(OrderPageLocators.TIME_CHOOSE)

    @allure.step('Выбрать черный цвет самоката')
    def choose_black_color(self):
        return self.find_element_clickable(OrderPageLocators.COLOR_BLACK)

    @allure.step('Выбрать серый цвет самоката')
    def choose_grey_color(self):
        return self.find_element_clickable(OrderPageLocators.COLOR_GREY)

    @allure.step('Заполнить поле "Комментарий"')
    def set_comment(self, comment):
        return self.find_element_located(OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    @allure.step('Дождаться открытия модального окна с подтверждением заказа')
    def wait_confirm_modal(self):
        return self.find_element_located(OrderPageLocators.CONFIRM_MODAL)

    @allure.step('Нажать на кнопку "Да"')
    def click_yes_button(self):
        return self.find_element_clickable(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Дождаться открытия модального окна с оформлением заказа')
    def wait_order_confirm(self):
        return self.find_element_located(OrderPageLocators.ORDER_MODAL)

    @allure.step('Нажать на лого Самоката')
    def click_on_samokat_logo(self):
        return self.find_element_clickable(OrderPageLocators.SAMOKAT_LOGO)
