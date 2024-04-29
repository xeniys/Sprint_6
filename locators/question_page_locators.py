from selenium.webdriver.common.by import By


class AccordionButtonsLocators:
    PRICE_QUESTION = (By.ID, 'accordion__heading-0')
    FEW_SCOOTERS_QUESTION = (By.ID, 'accordion__heading-1')
    RENT_TIME_QUESTION = (By.ID, 'accordion__heading-2')
    SCOOTER_TODAY_QUESTION = (By.ID, 'accordion__heading-3')
    EXTEND_TIME_QUESTION = (By.ID, 'accordion__heading-4')
    CHARGER_QUESTION = (By.ID, 'accordion__heading-5')
    CANCEL_ORDER_QUESTION = (By.ID, 'accordion__heading-6')
    DISTANCE_QUESTION = (By.ID, 'accordion__heading-7')


class AccordionResponseLocators:
    PRICE_RESPONSE = (By.ID, 'accordion__panel-0')
    FEW_SCOOTERS_RESPONSE = (By.ID, 'accordion__panel-1')
    RENT_TIME_RESPONSE = (By.ID, 'accordion__panel-2')
    SCOOTER_TODAY_RESPONSE = (By.ID, 'accordion__panel-3')
    EXTEND_TIME_RESPONSE = (By.ID, 'accordion__panel-4')
    CHARGER_RESPONSE = (By.ID, 'accordion__panel-5')
    CANCEL_ORDER_RESPONSE = (By.ID, 'accordion__panel-6')
    DISTANCE_RESPONSE = (By.ID, 'accordion__panel-7')
