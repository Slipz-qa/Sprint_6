from selenium.webdriver.common.by import By
class MainPageLocators:
    QUESTION_BUTTON = "accordion__heading-{}"

    ANSWER_PANEL = "accordion__panel-{}"

    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')][1]")

    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')][2]")

    LOGO = (By.XPATH, "//img[@alt='Scooter']")

    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    LAST_QUESTION = (By.ID, "accordion__heading-7")

