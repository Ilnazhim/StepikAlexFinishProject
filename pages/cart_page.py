from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from base.base_class import BaseClass
import allure

class CartPage(BaseClass):


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators

    checkout_button = "//button[@id='checkout']"


    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    #Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout_button")


    # Metods
    def prouct_confirmation(self):
        with allure.step("prouct_confirmation"):
            Logger.add_start_step(method="prouct_confirmation")
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method="prouct_confirmation")

