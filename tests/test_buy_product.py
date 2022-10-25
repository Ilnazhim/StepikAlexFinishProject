import time
import allure

from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.user_input_information import InputInformations


@allure.description("Test select product 1")
def test_select_product_1(browser):

    link = "https://www.dns-shop.ru/"
    print("\nStart Test 1")

    lp = LoginPage(browser, link)
    lp.open()
    lp.authorization()

    mp = MainPage(browser, link)
    mp.select_products_1()

    ui = InputInformations(browser, link)
    ui.choose_filter()

    cp = CartPage(browser, link)
    cp.go_to_cart()

    fp = FinishPage(browser, link)
    fp.finish_action()

    print("Finish Test 1")
    time.sleep(3)
