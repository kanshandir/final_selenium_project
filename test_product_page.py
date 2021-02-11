import pytest
from .pages.product_page import ProductPage
import time


# @pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", (pytest.param("7", marks=pytest.mark.xfail)), "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
# link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
# page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
# url адрес
# page.open()  # открываем страницу
# page.go_to_product_page()  # выполняем метод страницы
# page.solve_quiz_and_get_code()  # тут решаем проблему с выпадающим окном с формулой
# page.should_be_right_price()
# page.should_be_message()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# page = ProductPage(browser, link)
# page.open()
# page.go_to_product_page()
# page.should_not_be_success_message()


# def test_guest_cant_see_success_message(browser):
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# page = ProductPage(browser, link)
# page.open()
# page.should_not_be_success_message()


# def test_message_disappeared_after_adding_product_to_basket(browser):
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# page = ProductPage(browser, link)
# page.open()
# page.go_to_product_page()
# page.should_be_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()



def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

