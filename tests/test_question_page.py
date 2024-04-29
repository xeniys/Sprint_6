import allure
import pytest

from locators.question_page_locators import AccordionButtonsLocators
from locators.question_page_locators import AccordionResponseLocators
from constants import Questions
from constants import Urls
from pages.main_page import MainPage


class TestQuestion:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что при нажатии на вопрос открывается соответствующий ответ.')
    @pytest.mark.parametrize('question, response, text_response',
                             [
                                (AccordionButtonsLocators.PRICE_QUESTION, AccordionResponseLocators.PRICE_RESPONSE, Questions.PRICE_QUESTION_TEXT),
                                (AccordionButtonsLocators.FEW_SCOOTERS_QUESTION, AccordionResponseLocators.FEW_SCOOTERS_RESPONSE, Questions.FEW_SCOOTERS_QUESTION_TEXT),
                                (AccordionButtonsLocators.RENT_TIME_QUESTION, AccordionResponseLocators.RENT_TIME_RESPONSE, Questions.RENT_TIME_QUESTION_TEXT),
                                (AccordionButtonsLocators.SCOOTER_TODAY_QUESTION, AccordionResponseLocators.SCOOTER_TODAY_RESPONSE, Questions.SCOOTER_TODAY_QUESTION_TEXT),
                                (AccordionButtonsLocators.EXTEND_TIME_QUESTION, AccordionResponseLocators.EXTEND_TIME_RESPONSE, Questions.EXTEND_TIME_QUESTION_TEXT),
                                (AccordionButtonsLocators.CHARGER_QUESTION, AccordionResponseLocators.CHARGER_RESPONSE, Questions.CHARGER_QUESTION_TEXT),
                                (AccordionButtonsLocators.CANCEL_ORDER_QUESTION, AccordionResponseLocators.CANCEL_ORDER_RESPONSE,Questions.CANCEL_ORDER_QUESTION_TEXT),
                                (AccordionButtonsLocators.DISTANCE_QUESTION, AccordionResponseLocators.DISTANCE_RESPONSE, Questions.DISTANCE_QUESTION_TEXT)
                             ]
                             )
    def test_check_question_response(self, driver, question, response, text_response):
        page = MainPage(driver)
        page.open_page(Urls.BASE_URL)
        page.loading_main_page()
        page.scroll_to_accordion_items()
        page.find_question(question)
        page.click_on_question(question)
        response = page.wait_for_response(response).text

        assert response == text_response



