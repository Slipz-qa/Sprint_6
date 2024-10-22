from pages.main_page import MainPage
import time
from urls import MAIN_URL

class TestMainPage:
    def test_yandex_logo_navigates_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open(MAIN_URL)

        main_page.click_yandex_logo()

        main_page.switch_to_last_window()

        time.sleep(2)

        assert driver.current_url == "https://dzen.ru/?yredirect=true"
