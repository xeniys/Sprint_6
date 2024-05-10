from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def find_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator)).click()

    def open_page(self, url):
        self.driver.get(url)

    def scroll_elements(self, elements):
        return self.driver.execute_script("arguments[0].scrollIntoView();", elements)

    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        return self.driver.current_url
