from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "H1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME2 = (By.CSS_SELECTOR, "div.alertinner>strong")
    PRODUCT_PRICE2 = (By.CSS_SELECTOR, "div.alertinner>p>strong")


#name - //div[@class="col-sm-5"]/p/strong
#price - //div[@class="alertinner "]/p/strong
