from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from base.base_class import BaseClass
import allure

class PaymentPage(BaseClass):


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators

    finish_button = "//button[@id='finish']"

    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    #Actions
    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish_button")

    # Metods
    def payment(self):
        """login page enter"""
        with allure.step("payment"):
            Logger.add_start_step(method="payment")
            # self.get_current_url()
            self.click_finish_button()
            Logger.add_end_step(url=self.driver.current_url, method="payment")




