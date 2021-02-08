import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", (pytest.param("7", marks=pytest.mark.xfail)), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()  # открываем страницу
    page.go_to_product_page()  # выполняем метод страницы
    page.solve_quiz_and_get_code()  # тут решаем проблему с выпадающим окном с формулой
    page.should_be_message()
    page.should_be_right_price()
