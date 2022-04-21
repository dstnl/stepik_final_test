from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_BOOK_ADDED = (By.CSS_SELECTOR, ".product_main > h1")
    PAGE_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    BASKET_PRICE_ADDED = (By.CSS_SELECTOR, ".product_main > p")
    PAGE_PRICE_COST = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")