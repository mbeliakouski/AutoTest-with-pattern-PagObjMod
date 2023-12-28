from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISER_FORM = (By.CSS_SELECTOR,"form#register_form.well")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_BOOK_ADDET_TO_BASKET = (By.CSS_SELECTOR,".alert-safe:nth-of-type(1) .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    COST_BOOK = (By.CSS_SELECTOR, 'p.price_color')
    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")