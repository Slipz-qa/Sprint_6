import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from urls import MAIN_URL

class TestOrderScooter:
    @pytest.mark.parametrize(
        "name, surname, address, phone",
        [
            ("Артём", "Бочков", "Москва", "+79001234567"),
            ("Анна", "Петрова", "Санкт-Петербург", "+79007654321")
       ]
    )
    def test_order_scooter_flow(self, driver, name, surname, address, phone):
        main_page = MainPage(driver)
        main_page.open(MAIN_URL)

        main_page.click_order_button_top()

        order_page = OrderPage(driver)

        order_page.fill_order_form(name, surname, address, phone)

        order_page.select_station()

        order_page.click_next_button()

        order_page.select_delivery_date()

        order_page.select_rental_period()

        order_page.select_black_pearl_checkbox()

        order_page.enter_text(OrderPageLocators.COMMENT_FIELD, "Привет")

        order_page.click_order_buttonn()

        order_page.confirm_order()

        order_page.verify_order_confirmation()







