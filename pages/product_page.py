from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def get_product_name(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return prod_name.text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name2(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME2).text

    def get_product_price2(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE2).text
