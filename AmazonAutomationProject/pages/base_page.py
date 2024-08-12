from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value, timeout=10):

        # Bir elementi bulana kadar belirli bir süre bekler.

        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
            return element
        except TimeoutException:
            print(f"Element bulunamadı: {value}")
            return None

    def find_elements(self, by, value, timeout=10):

        # Bir elementi bulana kadar belirli bir süre bekler.

        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((by, value)))
            return elements
        except TimeoutException:
            print(f"Elementler bulunamadı: {value}")
            return []

    def click_element(self, by, value, timeout=10):

        # Bir elemente tıklama işlemi yapar.

        element = self.find_element(by, value, timeout)
        if element:
            element.click()
        else:
            print(f"Elemente tıklanamadı: {value}")

    def wait_for_element(self, by, value, timeout=10):

       #  Bir elementin görünür olmasını bekler.

        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))
            return element
        except TimeoutException:
            print(f"Element zaman aşımına uğradı: {value}")
            return None
