from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def click_question(self, num):
        question_locator = self.format_locators(MainPageLocators.QUESTION_BUTTON, num)
        self.driver.find_element(By.ID, question_locator).click()

    def get_answer_text(self, num):
        answer_locator = self.format_locators(MainPageLocators.ANSWER_PANEL, num)[1]
        return self.get_text(answer_locator)

    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_logo(self):
        self.click_element(MainPageLocators.LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def switch_to_last_window(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])






