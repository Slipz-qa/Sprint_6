import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestLogoNavigation:
    def test_logo_navigates_to_home_page(self, driver):
        main_page = MainPage(driver)
        main_page.open("https://qa-scooter.praktikum-services.ru/order")

        main_page.click_logo()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
