from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    RESULTS_TEXT = (By.XPATH, "//span[contains(text(),'Sonuçlar')]")
    SECOND_PAGE = (By.XPATH, "//a[contains(text(),'2')]")
    SECOND_PAGE_ACTIVE = (By.XPATH, "//a[contains(@class, 's-pagination-item--current') and text()='2']")

    def assert_search_results(self):

        assert self.find_element(*self.RESULTS_TEXT).is_displayed()
        # Arama sonuçlarının bulunduğu kontrol edilir.

    def go_to_second_page(self):

        self.click_element(*self.SECOND_PAGE)
        # 2. sayfaya geçiş yapılır.

    def assert_on_second_page(self):

        assert self.find_element(*self.SECOND_PAGE_ACTIVE).is_displayed()
        # 2. sayfanın aktif olduğu doğrulanır.

    def select_product(self):

        product = self.find_element(By.XPATH, "(//div[contains(@class, 's-main-slot')]//div[@data-component-type='s-search-result'])[position()=5]")
        product.click()
        # 5. satır 1. sütundaki ürüne tıklanır.
