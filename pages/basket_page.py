from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_be_message_basket_empty()
        self.should_not_products_in_basket()

    def should_not_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty'

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), 'No message about empty basket'
