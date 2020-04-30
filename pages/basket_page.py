from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_empty()
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "в адресе отсутствует basket"

    def should_be_basket_empty(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text,\
            "нет надписи о том что корзина пуста"

    def should_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "в корзине что то есть"
