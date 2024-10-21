from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
import pytest


class TestMainPage:
    @pytest.mark.parametrize(
        "num, result",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
        ]
    )
    def test_question_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open("https://qa-scooter.praktikum-services.ru/")

        last_question_locator = (By.ID, "accordion__heading-7")
        main_page.scroll_to_element(last_question_locator)

        question_locator = main_page.format_locators(MainPageLocators.QUESTION_BUTTON, num)


        question_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, question_locator)))

        question_element.click()

        answer_locator = MainPageLocators.ANSWER_PANEL.format(num)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, answer_locator)))

        actual_answer = driver.find_element(By.ID, answer_locator).text
        assert result in actual_answer, f"Ответ не соответствует ожидаемому для вопроса {num}."
