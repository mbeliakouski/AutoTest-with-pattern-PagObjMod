from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISER_FORM = (By.CSS_SELECTOR,"form#register_form.well")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")