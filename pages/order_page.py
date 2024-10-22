from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_order_form(self, name, surname, address, phone):
        self.enter_text(OrderPageLocators.NAME_INPUT, name)
        self.enter_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.enter_text(OrderPageLocators.PHONE_INPUT, phone)


    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def select_station(self):
        self.driver.find_element(*OrderPageLocators.METRO_INPUT).click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.METRO_STATION_OPTION))

        self.driver.find_element(*OrderPageLocators.METRO_STATION_OPTION).click()

    def verify_order_header(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_HEADER))
        return self.driver.find_element(*OrderPageLocators.ORDER_HEADER).text

    def select_delivery_date(self):
        self.click_element(OrderPageLocators.DELIVERY_DATE_INPUT)

        self.click_element(OrderPageLocators.DELIVERY_DATE_OPTION)

    def select_rental_period(self):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_INPUT)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_OPTION))

        self.click_element(OrderPageLocators.RENTAL_PERIOD_OPTION)

    def select_black_pearl_checkbox(self):
        self.click_element(OrderPageLocators.BLACK_PEARL_CHECKBOX)

    def enter_comment(self, comment_text):
        self.enter_text(OrderPageLocators.COMMENT_FIELD, comment_text)

    def click_order_buttonn(self):
        self.click_element(OrderPageLocators.ORDER_BUTTONN)

    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    def verify_order_confirmation(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_MODAL_HEADER)
        )
        order_header = self.driver.find_element(*OrderPageLocators.ORDER_MODAL_HEADER)
        assert "Заказ оформлен" in order_header.text, "Заказ не оформлен!"





