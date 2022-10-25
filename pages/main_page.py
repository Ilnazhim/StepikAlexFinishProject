import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure
from base.base_class import BaseClass


class MainPage(BaseClass):

    # Locators
    SMARTPHONE_AND_GADGETS_CATEGORY = "//div[2][@class='menu-desktop__root']"
    SMARTPHONE_SUBCATEGORY = "//a[text()='Смартфоны']"

    # Getters
    def get_smartphone_and_gadgets_category(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.SMARTPHONE_AND_GADGETS_CATEGORY)))

    def get_smartphone_subcategory(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.SMARTPHONE_SUBCATEGORY)))

    # Actions
    def click_smartphone_and_gadgets_category(self):
        self.get_smartphone_and_gadgets_category().click()
        print("Click smartphone and gadgets category")

    def click_smartphone_subcategory(self):
        self.get_smartphone_subcategory().click()
        print("Click smartphone subcategory")


    # Metods
    def select_products_1(self):
        """Select product"""
        with allure.step("select_products_1"):
            Logger.add_start_step(method="select_products_1")

            self.get_current_url()
            self.click_smartphone_and_gadgets_category()
            self.click_smartphone_subcategory()
            Logger.add_end_step(url=self.browser.current_url, method="select_products_1")
