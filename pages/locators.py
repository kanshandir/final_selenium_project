from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CLASS_NAME, ".basket-items")

