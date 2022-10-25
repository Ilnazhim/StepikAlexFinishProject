import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure
from base.base_class import BaseClass


class CartPage(BaseClass):

    # Locators
    NAME_PHONE = "//div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/a/span"
    PRICE_PHONE = "//div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]"
    BUY_BUTTON = "//div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]"
    CART_BUTTON = "//span[@class='cart-link__lbl']"
    NAME_PHONE_CART = "//a[@class='base-ui-link base-ui-link_gray_dark']"
    PRICE_PHONE_CART = "//div[@class='price__block price__block_main']//span"

    # Getters
    def get_name_phone(self):
        return self.browser.find_element(By.XPATH, self.NAME_PHONE)

    def get_price_phone(self):
        return self.browser.find_element(By.XPATH, self.PRICE_PHONE)

    def get_buy_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.BUY_BUTTON)))

    def get_cart_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.CART_BUTTON)))

    def get_name_phone_cart(self):
        return self.browser.find_element(By.XPATH, self.NAME_PHONE_CART)

    def get_price_phone_cart(self):
        return self.browser.find_element(By.XPATH, self.PRICE_PHONE_CART)

    # Actions

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click buy button")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    # Metods
    def go_to_cart(self):
        """Go to cart"""
        with allure.step("go_to_cart"):
            Logger.add_start_step(method="go_to_cart")
            phone_name = self.get_name_phone().text
            phone_price = self.get_price_phone().text
            try:
                self.click_buy_button()
            except StaleElementReferenceException:
                time.sleep(3)
                self.click_buy_button()
            self.click_cart_button()
            self.browser.refresh()
            phone_name_cart = self.get_name_phone_cart().text
            phone_price_cart = self.get_price_phone_cart().text
            assert phone_name_cart in phone_name
            assert phone_price_cart in phone_price
            Logger.add_end_step(url=self.browser.current_url, method="go_to_cart")
