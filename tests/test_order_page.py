import allure
import pytest

import locators.order_page_locators
from pages.order_page import OrderPage
from pages.main_page import MainPage
from constants import Urls


class TestOrderPage:

    @allure.title('Проверка редиректа на страницу заказа при нажатии на кнопку "Заказать" в хедере')
    @allure.description('На странице ищем  кнопку "Заказать" в хедере и проверяем переход к станице с формой заказа')
    def test_redirect_to_order_page_from_upper_button(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.BASE_URL)
        page.loading_main_page()
        page.click_on_upper_order_button()
        order_page = OrderPage(driver)
        order_page.loading_order_page()

        assert driver.current_url == Urls.ORDER_URL

    @allure.title('Проверка редиректа на страницу заказа при нажатии на кнопку "Заказать" на главной странице')
    @allure.description('На странице ищем кнопку "Заказать" в теле станицы и проверяем переход к станице с формой '
                        'заказа')
    def test_redirect_to_order_page_from_down_button(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.BASE_URL)
        page.loading_main_page()
        page.scroll_to_down_order_button()
        page.click_on_down_order_button()
        order_page = OrderPage(driver)
        order_page.loading_order_page()

        assert driver.current_url == Urls.ORDER_URL

    @allure.title('Проверка успешного оформления заказа')
    @allure.description('Проверяем успешное создание заказа при заполнении всех полей в форме заказа')
    @pytest.mark.parametrize('name, surname, address, phone, comment',
                             [
                                ('Ксения', 'Головина', 'Ворошиловский 35', '89110005678', ''),
                                ('Имя', 'Фамилия', 'Ардес 34', '89100783683', 'комментарий')
                             ]
                             )
    def test_success_order(self, driver, name, surname, address, phone, comment):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_URL)
        order_page.loading_order_page()
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.click_on_subway_station_field()
        order_page.wait_for_subway_station()
        order_page.scroll_to_subway_station()
        order_page.set_subway()
        order_page.set_phone(phone)
        order_page.click_next_button()
        order_page.wait_order_about_loading()
        order_page.click_on_delivery_time_field()
        order_page.loading_month_calendar()
        order_page.choose_the_date()
        order_page.click_rent_field()
        order_page.wait_rent_dropdown_show()
        order_page.choose_rent_time()
        order_page.choose_grey_color()
        order_page.set_comment(comment)
        order_page.click_next_button()
        order_page.wait_confirm_modal()
        order_page.click_yes_button()
        result = order_page.wait_order_confirm()

        assert "Заказ оформлен" in result.text


