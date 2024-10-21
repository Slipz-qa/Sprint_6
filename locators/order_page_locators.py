from selenium.webdriver.common.by import By
class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")  # Локатор для имени
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Локатор для фамилии
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Локатор для адреса
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Локатор для телефона
    NEXT_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")  # Локатор для кнопки "Далее"
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ успешно создан!')]")  # Локатор для успешного сообщения
    STATION_DROPDOWN = (By.CLASS_NAME, "select-search__input")
    METRO_STATION_OPTION = (By.XPATH, "//li[@data-value='1']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and normalize-space()='Про аренду']")
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DELIVERY_DATE_OPTION = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='21']")
    RENTAL_PERIOD_INPUT = (By.XPATH, "//div[@class='Dropdown-placeholder' and contains(text(), '* Срок аренды')]")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and contains(text(), 'сутки')]")
    BLACK_PEARL_CHECKBOX = (By.XPATH, "//label[@for='black']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTONN = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_MODAL_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
