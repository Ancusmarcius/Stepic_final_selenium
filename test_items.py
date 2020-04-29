# import pytest
import time


def test_button_for_language(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(1)
    browser.implicitly_wait(10)
    btn = browser.find_elements_by_css_selector("button.btn-primary")
    print("кнопок с добавлением в корзину:", len(btn))
    assert len(btn) == 1, "кнопку украли"
    time.sleep(1)
