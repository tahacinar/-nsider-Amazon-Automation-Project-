from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    LOGO = (By.ID, "nav-logo-sprites")
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def load(self):

        self.driver.get("https://www.amazon.com.tr/")
        # Doğru URL'yi girdiğinizden emin olun.

    def search_item(self, item):

        self.find_element(*self.SEARCH_BAR).send_keys(item)
        # Arama kutusuna ürün adı yazılır.
        self.find_element(*self.SEARCH_BUTTON).click()
        # Arama butonuna tıklanır.
