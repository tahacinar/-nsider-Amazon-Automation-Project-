import pytest
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup")
class TestAmazon:
    def test_amazon_shopping(self):
        home_page = HomePage(self.driver)
        search_results_page = SearchResultsPage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        # 1. Anasayfa açılır
        home_page.load()

        # 2. 'samsung' araması yapılır
        home_page.search_item('samsung')

        # 3. Arama sonuçları doğrulanır
        search_results_page.assert_search_results()

        # 4. 2. sayfaya geçilir
        search_results_page.go_to_second_page()
        search_results_page.assert_on_second_page()

        # 5. 2. sayfadaki 5. sıradaki ürüne tıklanır
        product_list = search_results_page.find_elements(By.CSS_SELECTOR, '.s-main-slot .s-result-item')
        product_list[4].click()

        # 6. Ürün sayfasında olduğumuz doğrulanır
        product_page.assert_on_product_page()

        # 7. Ürün sepete eklenir
        product_page.add_to_cart()

        # 8. Sepet sayfasında olduğumuz doğrulanır
        cart_page.assert_on_cart_page()

        # 9. Ana sayfaya geri dönülür
        home_page.find_element(*HomePage.LOGO).click()