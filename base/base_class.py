import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class BaseClass:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    """Metod get current url"""
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Current url " + get_url)

    """Metod assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Metod is element present"""
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((how, what)))
            print("Assert element is present")
        except NoSuchElementException:
            return False
        return True


    """Metod screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.browser.save_screenshot("C:\\Users\\ilnazhim\\environments\\StepikAlexAutomationPython\\screen\\" + name_screenshot)
        print("Screenshot")

    """Metod assert url"""
    def assert_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Good value url")
