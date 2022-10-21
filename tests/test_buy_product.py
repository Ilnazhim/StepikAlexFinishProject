import time
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.description("Test select product 1")
def test_select_product_1(browser):

    link = "https://www.dns-shop.ru/"
    print("\nStart Test 1")

    lp = LoginPage(browser, link)
    lp.open()
    lp.authorization()
    mp = MainPage(browser, link)
    mp.select_products_1()


    # mp = MainPage(browser)
    # mp.select_products_1()
    #
    # cp = CartPage(browser)
    # cp.prouct_confirmation()
    #
    # cip = ClientInformationPage(browser)
    # cip.input_information()
    #
    # pay = PaymentPage(browser)
    # pay.payment()
    #
    # fp = FinishPage(browser)
    # fp.finish()

    print("Finish Test 1")
    time.sleep(5)
