import allure

from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage


class DzenPage(BasePage):

    @allure.step('Дождаться открытия страницы Я.Дзен')
    def loading_dzen_page(self):
        return self.find_element_located(DzenPageLocators.DZEN)
