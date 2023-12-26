from pages.product_page import ProductPage
import pytest


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_click_basket()
    page.should_be_find_value()
    page.should_be_is_disappeared()