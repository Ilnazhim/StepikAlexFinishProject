import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure
from base.base_class import BaseClass


class MainPage(BaseClass):
    # def __init__(self, driver):
    #     self.driver = driver
    #     super().__init__(driver)

    # Locators
    SMARTPHONE_AND_GADGETS_CATEGORY = "//div[2][@class='menu-desktop__root']"
    SMARTPHONE_SUBCATEGORY = "//a[text()='Смартфоны']"
    INPUT_COST_MIN = "//input[@placeholder='от 2 899']"
    INPUT_COST_MAX = "//input[@placeholder='до 139 999']"
    CHOOSE_MODEL_SAMSUNG = "//label[24][@class='ui-checkbox ui-checkbox_list']"
    SUBMIT_BUTTON = "//button[@data-role='filters-submit']"
    NAME_PHONE = "//a[@class='catalog-product__name ui-link ui-link_black']//span"
    PRICE_PHONE = "//div[@class='product-buy__price']"
    BUY_BUTTON = "//button[@class='button-ui buy-btn button-ui_brand button-ui_passive']"
    CART_BUTTON = "//span[@class='cart-link__lbl']"
    DELETE_PRODUCT = "//p[@class='remove-button__title']"


    # Getters
    def get_smartphone_and_gadgets_category(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.SMARTPHONE_AND_GADGETS_CATEGORY)))

    def get_smartphone_subcategory(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.SMARTPHONE_SUBCATEGORY)))

    def get_input_cost_min(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_COST_MIN)))

    def get_input_cost_max(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_COST_MAX)))

    def get_choose_model_samsung(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.CHOOSE_MODEL_SAMSUNG)))

    def get_submit_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON)))

    def get_name_phone(self):
        return self.browser.find_element(By.XPATH, self.NAME_PHONE)
        # return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.NAME_PHONE)))

    def get_price_phone(self):
        return self.browser.find_element(By.XPATH, self.PRICE_PHONE)
        # return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.PRICE_PHONE)))

    def get_buy_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.BUY_BUTTON)))

    def get_cart_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.CART_BUTTON)))

    def get_delete_product(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.DELETE_PRODUCT)))


    # Actions
    def click_smartphone_and_gadgets_category(self):
        self.get_smartphone_and_gadgets_category().click()
        print("Click smartphone and gadgets category")

    def click_smartphone_subcategory(self):
        self.get_smartphone_subcategory().click()
        print("Click smartphone subcategory")

    def input_cost_min(self, min_price):
        self.get_input_cost_min().send_keys(min_price)
        print("Input cost min")

    def input_cost_max(self, max_price):
        self.get_input_cost_max().send_keys(max_price)
        print("Input cost max")

    def click_choose_model_samsung(self):
        self.get_choose_model_samsung().click()
        print("Choose model Samsung")

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click buy button")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    def click_delete_product(self):
        self.get_delete_product().click()
        print("Click delete product")


    # Metods
    def select_products_1(self):
        with allure.step("select_products_1"):
            Logger.add_start_step(method="select_products_1")

            self.get_current_url()
            self.click_smartphone_and_gadgets_category()
            self.click_smartphone_subcategory()
            self.browser.execute_script("window.scrollBy(0, +1000);")
            self.input_cost_min("15000")
            self.input_cost_max("20000")
            self.click_choose_model_samsung()
            self.browser.execute_script("window.scrollBy(0, +1000);")
            time.sleep(1)
            self.click_submit_button()
            self.browser.execute_script("window.scrollBy(0, -1600);")
            # value_name = self.get_name_phone().text
            # value_price = self.get_price_phone().text
            self.click_buy_button()
            self.click_cart_button()
            # print(value_price, value_name, sep="")
            self.click_delete_product()

            Logger.add_end_step(url=self.browser.current_url, method="select_products_1")

