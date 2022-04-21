from .pages.product_page import ProductPage
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_quiz_product_code(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_to_basket()
    assert True