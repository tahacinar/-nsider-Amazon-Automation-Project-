from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_TEXT = (By.XPATH, "//h1[contains(text(),'Sepetiniz')]")

    def assert_on_cart_page(self):

        assert self.find_element(*self.CART_TEXT).is_displayed()
        # Sepet sayfasında olduğunuz doğrulanır.
