from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "?promo=newYear" in login_url, "Not a promo page"
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
        assert self.browser.find_element(*ProductPageLocators.BASKET_BOOK_ADDED).text in self.browser.find_element(
            *ProductPageLocators.PAGE_BOOK_NAME).text, "Wrong book added"
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRICE_ADDED).text in self.browser.find_element(
            *ProductPageLocators.PAGE_PRICE_COST).text.split()[-1], "Wrong basket price"
