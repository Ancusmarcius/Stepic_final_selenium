from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_basket(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button_add_product.click()