import allure

from constants import Urls
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from pages.order_page import OrderPage


class TestRedirect:
    @allure.title('Проверка редиректа на страницу дзена при нажатии на лого Яндекса в хедере')
    @allure.description('На странице ищем  лого Яндекса в хедере и проверяем переход к Дзену')
    def test_redirect_to_dzen_from_yandex_logo(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.BASE_URL)
        page.loading_main_page()
        page.click_on_yandex_logo()
        page.switch_to_window()
        dzen = DzenPage(driver)
        dzen.loading_dzen_page()

        assert Urls.DZEN_URL in dzen.get_current_url()

    @allure.title('Проверка редиректа на главную страницу при нажатии на лого самоката в хедере')
    @allure.description('На странице ищем  лого самоката и проверяем переход на главную страницу')
    def test_redirect_to_main_from_samokat_logo(self, driver):
        page = OrderPage(driver)
        page.open_page(Urls.ORDER_URL)
        page.loading_order_page()
        page.click_on_samokat_logo()
        main = MainPage(driver)
        main.loading_main_page()

        assert Urls.BASE_URL == main.get_current_url()
