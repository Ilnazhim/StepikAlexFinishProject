import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure
from base.base_class import BaseClass


class FinishPage(BaseClass):

    # Locators
    DELETE_PRODUCT = "//p[@class='remove-button__title']"
    NAME_PHONE_CART = "//a[@class='base-ui-link base-ui-link_gray_dark']"
    PRICE_PHONE_CART = "//div[@class='price__block price__block_main']//span"

    # Getters
    def get_delete_product(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.DELETE_PRODUCT)))

    def get_name_phone_cart(self):
        return self.browser.find_element(By.XPATH, self.NAME_PHONE_CART)

    def get_price_phone_cart(self):
        return self.browser.find_element(By.XPATH, self.PRICE_PHONE_CART)

    # Actions
    def click_delete_product(self):
        self.get_delete_product().click()
        print("Click delete product")

    # Metods
    def finish_action(self):
        """Finish actions"""
        with allure.step("finish_action"):
            self.get_screenshot()
            self.click_delete_product()
            Logger.add_end_step(url=self.browser.current_url, method="finish_action")
