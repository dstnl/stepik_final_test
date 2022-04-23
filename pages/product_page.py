from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import ProductPageLocators
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "?promo=offer" in login_url, "Not a promo page"
        assert True

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_added_to_basket(self):
        basket_book_added = self.browser.find_element(*ProductPageLocators.BASKET_BOOK_ADDED).text
        page_book_name = self.browser.find_element(*ProductPageLocators.PAGE_BOOK_NAME).text
        print(f"Book names: {basket_book_added} and {page_book_name}")
        basket_price_added = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_ADDED).text
        page_price_cost = self.browser.find_element(*ProductPageLocators.PAGE_PRICE_COST).text.split()[-1]
        print(f"Book price: {basket_price_added} and {page_price_cost}")
        assert basket_book_added == page_book_name, "Wrong book added"
        assert basket_price_added == page_price_cost, "Wrong basket price"
