 

# Amazon Otomasyon Projesi
Bu proje, Amazon Türkiye web sitesi için Selenium ile Python kullanarak Page Object Model (POM) tasarım desenine göre hazırlanmış bir otomasyon betiğidir. Betik, web sitesinde ürün arama, arama sonuçlarında gezinme ve bir ürünü sepete ekleme gibi bir dizi işlemi gerçekleştirir.

# Özellikler

- Amazon Türkiye'ye Gitme: Amazon Türkiye ana sayfasını açar ve doğru şekilde yüklendiğini doğrular.  
- "Samsung" Araması Yapma: Arama çubuğuna "Samsung" yazar ve arama işlemini gerçekleştirir.
- Arama Sonuçlarını Doğrulama: "Samsung" için arama sonuçlarının görüntülendiğini onaylar.
- 2.Arama Sonuç Sayfasına Gitme: Sayfalama yoluyla ikinci arama sonuçları sayfasına gider ve bu sayfanın şu an görüntülendiğini doğrular.
- Bir Ürün Seçme: İkinci sayfada 5. satırın 1. sütununda bulunan ürüne tıklar.
- Ürün Sayfasını Doğrulama: Ürün sayfasının doğru şekilde yüklendiğini doğrular.
- Ürünü Sepete Ekleme: Ürünü alışveriş sepetine ekler.
- Sepet Sayfasını Doğrulama: Sepet sayfasının yüklendiğini ve eklenen ürünün görüntülendiğini doğrular.
- Ana Sayfaya Dönüş: Amazon logosuna tıklayarak ana sayfaya geri döner.

# Proje Yapısı
- pages/: Amazon'un farklı sayfaları için Page Object sınıflarını içerir.

- home_page.py: Amazon ana sayfası ile etkileşim için sınıf.
- search_results_page.py: Arama sonuçları sayfası ile etkileşim için sınıf.
- product_page.py: Ürün detay sayfası ile etkileşim için sınıf.
- cart_page.py: Alışveriş sepeti sayfası ile etkileşim için sınıf.

- tests/: Otomasyonu çalıştıran test betiklerini içerir.
- test_amazon.py: Yukarıda tanımlanan işlem sırasını yürüten ana test betiği.
- conftest.py: Testler için WebDriver'ı kurma ve kapatma işlemlerini gerçekleştiren yapılandırma dosyası.

