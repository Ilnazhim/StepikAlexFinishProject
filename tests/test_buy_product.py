import time
import allure
from pages.login_page import LoginPage


@allure.description("Test select product 1")
def test_select_product_1(browser):

    link = "https://www.dns-shop.ru/"
    print("\nStart Test 1")

    page = LoginPage(browser, link)
    page.open()
    page.authorization()

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
    time.sleep(3)
