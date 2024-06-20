from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging


class BasePage:
    def __init__(self, driver, wait=10):
        self.driver = driver
        self.logger = driver.logger
        self.wait = WebDriverWait(self.driver, wait)
        self.action = ActionChains(self.driver)
        self.class_name = self.__class__.__name__

    def element_name(self, element):
        for name, value in vars(self.__class__).items():
            if isinstance(value, (list, tuple)) and element in value:
                return f"{name}[{value.index(element)}]"
            elif value == element:
                return name
        return str(element)

    def find_element(self, element_locator):
        try:
            if isinstance(element_locator, tuple):
                return self.driver.find_element(*element_locator)
            else:
                return self.driver.find_element(element_locator)
        except Exception as e:
            self.logger.error(f"finding element: {e}")
            return None

    def click(self, element_locator):
        try:
            element = self.find_element(element_locator)
            if element is None:
                raise Exception("Element not found")
            element_name = self.element_name(element_locator)
            self.wait.until(EC.element_to_be_clickable(element)).click()
            self.logger.info(f"{self.class_name}: Clicked |{element_name}|")
        except Exception as e:
            self.logger.error(f"clicking element: {e}")

        return self

    def input(self, element_locator, value):
        try:
            element = self.find_element(element_locator)
            if element is None:
                raise Exception("Element not found")
            self.click(element_locator)
            self.wait.until(EC.visibility_of(element))
            element.clear()
            element.send_keys(value)
            self.logger.info(f"{self.class_name}: Writing |{value}| to |{self.element_name(element_locator)}|")
            self.wait.until(EC.text_to_be_present_in_element_value(element_locator, value))
        except Exception as e:
            self.logger.error(f"inputting to element: {e}")

        return self
