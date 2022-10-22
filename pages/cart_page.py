import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from base.base_class import BaseClass
import allure
from pages.main_page import MainPage


class CartPage(BaseClass):


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


    #Actions
    def click_delete_product(self):
        self.get_delete_product().click()
        print("Click delete product")


    # Metods
    def cart_product(self):
        with allure.step("Cart product"):
            Logger.add_start_step(method="cart_product")
            self.assert_word(self.get_name_phone_cart(), self.get_name_phone())
            self.assert_word(self.get_price_phone_cart(), self.get_price_phone())
            time.sleep(3)
            self.click_delete_product()
            Logger.add_end_step(url=self.browser.current_url, method="cart_product")

