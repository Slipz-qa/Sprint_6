from pages.main_page import MainPage
from urls import ORDER_PAGE_URL

class TestLogoNavigation:
    def test_logo_navigates_to_home_page(self, driver):
        main_page = MainPage(driver)
        main_page.open(ORDER_PAGE_URL)

        main_page.click_logo()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
