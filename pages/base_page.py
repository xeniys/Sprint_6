import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.question_page_locators import AccordionButtonsLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def find_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator)).click()

    def open_page(self, url):
        self.driver.get(url)
