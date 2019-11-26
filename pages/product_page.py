from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def check_adding_to_basket(self):
        self.should_be_message_about_adding()
        self.should_be_message_with_total_price()
        self.should_be_name_in_message_correct()
        self.should_be_basket_price_correct()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDING), \
            'Message about adding to basket is absent'

    def should_be_message_with_total_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), \
            'Message about basket total price is absent'

    def should_be_name_in_message_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET).text
        print(product_name, name_in_basket)
        assert product_name == name_in_basket, 'Product name in basket is not equal product name on page'

    def should_be_basket_price_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        print(product_price, price_in_basket)
        assert product_price == price_in_basket, 'Price in basket is not correct'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print("Your code: {}".format(alert_text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDING), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDING), \
            "Success message should be disappeared, but not"

