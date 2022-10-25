import time

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass
from utilities.logger import Logger
import allure


class LoginPage(BaseClass):


    # Locators
    CHOOSE_LOCATION = "//button[@class='base-ui-button-v2_medium base-ui-button-v2_brand base-ui-button-v2_ico-none " \
                      "base-ui-button-v2 v-confirm-city__btn']"
    ENTER_BUTTON = "//div[@class='user-profile__login']"
    ENTER_BUTTON_V2 = "//span[@class='base-ui-button-v2__text']"
    ENTER_WITH_PASSWORD = "//div[@class='block-other-login-methods__password-caption']"
    INPUT_EMAIL = "//div[@class='form-entry-with-password__input']//input"
    INPUT_PASSWORD = "//div[@class='form-entry-with-password__password']//input"
    ENTER_TO_LK_BUTTON = "//div[@class='form-entry-with-password__main-button']//button"
    CHECK_AVATAR_USER = "//div[@class='user-profile__avatar-wrapper']"

    # Getters
    def get_choose_locations(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.CHOOSE_LOCATION)))

    def get_enter_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ENTER_BUTTON)))

    def get_enter_button_v2(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ENTER_BUTTON_V2)))

    def get_enter_with_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ENTER_WITH_PASSWORD)))

    def get_input_email(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_EMAIL)))

    def get_input_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_PASSWORD)))

    def get_enter_to_lk_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ENTER_TO_LK_BUTTON)))

    # Actions
    def click_choose_locations(self):
        self.get_choose_locations()
        print("Choose local town")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click enter button")

    def click_enter_button_v2(self):
        self.get_enter_button_v2().click()
        print("Click enter button v2")

    def click_enter_with_password(self):
        self.get_enter_with_password().click()
        print("Click enter with password")

    def input_email(self, email):
        self.get_input_email().send_keys(email)
        print("Input email")

    def input_password(self, password):
        self.get_input_password().send_keys(password)
        print("Input password")

    def click_enter_to_lk_button(self):
        self.get_enter_to_lk_button().click()
        print("Click enter to lk button")

    # Metods
    def authorization(self):
        """login page enter"""
        with allure.step("authorization"):
            Logger.add_start_step(method="authorization")
            self.browser.get(self.url)
            self.browser.maximize_window()
            self.get_current_url()

            self.click_enter_button()
            try:
                self.click_enter_button_v2()
            except ElementClickInterceptedException or TimeoutException:
                time.sleep(3)
                self.click_enter_button_v2()
            self.click_enter_with_password()
            self.input_email("marinin.am@mail.ru")
            self.input_password("Test2022")
            self.click_enter_to_lk_button()
            assert self.is_element_present(By.XPATH, self.CHECK_AVATAR_USER), "Avatar logo wasn't found"
            self.get_screenshot()
            Logger.add_end_step(url=self.browser.current_url, method="authorization")
