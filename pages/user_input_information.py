import time
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure
from base.base_class import BaseClass


class InputInformations(BaseClass):

    # Locators
    INPUT_COST_MIN = "//input[@placeholder='от 2 899']"
    INPUT_COST_MAX = "//input[@placeholder='до 139 999']"
    CHOOSE_MODEL_SAMSUNG = "//label[27][@class='ui-checkbox ui-checkbox_list']"
    SUBMIT_BUTTON = "//button[@data-role='filters-submit']"


    # Getters
    def get_input_cost_min(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_COST_MIN)))

    def get_input_cost_max(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_COST_MAX)))

    def get_choose_model_samsung(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.CHOOSE_MODEL_SAMSUNG)))

    def get_submit_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON)))


    # Actions
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

    # Metods
    def choose_filter(self):
        """Choose filters"""
        with allure.step("choose_filter"):
            Logger.add_start_step(method="choose_filter")
            self.browser.execute_script("window.scrollBy(0, +1000);")
            self.input_cost_min("15000")
            self.input_cost_max("20000")
            self.click_choose_model_samsung()
            self.browser.execute_script("window.scrollBy(0, +1000);")
            time.sleep(1)
            try:
                self.click_submit_button()
            except ElementClickInterceptedException:
                self.click_submit_button()
            self.browser.execute_script("window.scrollBy(0, -1700);")
            time.sleep(3)
            Logger.add_end_step(url=self.browser.current_url, method="choose_filter")
