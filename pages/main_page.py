import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Дождаться открытия страницы Самоката')
    def loading_main_page(self):
        return self.find_element_located(MainPageLocators.MAIN_PAGE)

    @allure.step('Проскроллить страницу к блоку с вопросами')
    def scroll_to_accordion_items(self):
        accordion_items = self.find_element_located(MainPageLocators.ACCORDION_ITEMS)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_items)

    @allure.step('Найти вопрос')
    def find_question(self, question):
        return self.find_element_located(question)

    @allure.step('Кликнуть на  вопрос и развернуть его')
    def click_on_question(self, question):
        return self.find_element_clickable(question)

    def wait_for_response(self, response):
        return self.find_element_located(response)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_on_upper_order_button(self):
        return self.find_element_clickable(MainPageLocators.UP_ORDER_BUTTON)

    @allure.step('Проскроллить страницу вниз')
    def scroll_to_down_order_button(self):
        down_order_button = self.find_element_located(MainPageLocators.DOWN_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", down_order_button)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_on_down_order_button(self):
        return self.find_element_clickable(MainPageLocators.DOWN_ORDER_BUTTON)

    @allure.step('Нажать на кнопку лого Яндекса')
    def click_on_yandex_logo(self):
        return self.find_element_clickable(MainPageLocators.YANDEX_LOGO)

    @allure.step('Открыть вкладку со страницой редиректа')
    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])







