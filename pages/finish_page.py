from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from base.base_class import BaseClass
import allure

class FinishPage(BaseClass):


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    # Metods
    def finish(self):
        """login page enter"""
        with allure.step("finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url("https://www.saucedemo.com/checkout-complete.html")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")




