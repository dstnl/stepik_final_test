import pytest
from .pages.product_page import ProductPage
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"


@pytest.mark.parametrize('promo', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_quiz_product_code(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_to_basket()
    assert True
