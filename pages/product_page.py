from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_basket(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button_add_product.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Не найдено имя продукта")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Не найдено сообщение с именем продукта о том что добавлено в корзину")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name in message, "имя продукта нет в сообщении о том что добавили в корзину"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Не найдено сообщение с ценой в корзине")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Не найден текст с ценой товара")
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "нет цены продукта в сообщении с ценой в корзине"
