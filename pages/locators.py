from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    MESSAGE_ADDING = (By.CSS_SELECTOR, '#messages > .alert-success:nth-child(1) > .alertinner')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages > .alert-info > .alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages > .alert-success:nth-child(1) > .alertinner > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages > .alert-info > .alertinner strong')