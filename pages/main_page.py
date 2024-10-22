from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def click_question_button(self, num):
        question_locator = self.format_locators(MainPageLocators.QUESTION_BUTTON, num)
        question_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, question_locator))
        )
        question_element.click()

    def wait_for_answer_panel(self, num):
        answer_locator = MainPageLocators.ANSWER_PANEL.format(num)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, answer_locator))
        )

    def get_answer_text(self, num):
        answer_locator = MainPageLocators.ANSWER_PANEL.format(num)
        return self.driver.find_element(By.ID, answer_locator).text






