from .pages.product_page import ProductPage
# import pytest


# @pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
