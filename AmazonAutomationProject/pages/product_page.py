from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    def assert_on_product_page(self):

        assert "samsung" in self.driver.title.lower()
        # Ürün sayfasında olduğunuzu doğrulamak için başlık kontrolü yapılır.

    def add_to_cart(self):

        self.click_element(*self.ADD_TO_CART_BUTTON)
        # Ürün sepete eklenir.
