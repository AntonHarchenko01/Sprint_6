from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_ACCEPT_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]
    UPPER_BUTTON_ORDER = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/button[1]"]
    LOWER_BUTTON_ORDER = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[5]/button[1]"]


class QaScooterHomePageLocators:
    FIRST_QUESTION = [By.XPATH, "//div[@id='accordion__heading-0']"]
    FIRST_ANSWER = [By.XPATH, "//div[@id='accordion__panel-0']"]
    SECOND_QUESTION = [By.XPATH, "//div[@id='accordion__heading-1']"]
    SECOND_ANSWER = [By.XPATH, "//div[@id='accordion__panel-1']"]
    THIRD_QUESTION = [By.XPATH, "//div[@id='accordion__heading-2']"]
    THIRD_ANSWER = [By.XPATH, "//div[@id='accordion__panel-2']"]
    FOURTH_QUESTION = [By.XPATH, "//div[@id='accordion__heading-3']"]
    FOURTH_ANSWER = [By.XPATH, "//div[@id='accordion__panel-3']"]
    FIFTH_QUESTION = [By.XPATH, "//div[@id='accordion__heading-4']"]
    FIFTH_ANSWER = [By.XPATH, "//div[@id='accordion__panel-4']"]
    SIXTH_QUESTION = [By.XPATH, "//div[@id='accordion__heading-5']"]
    SIXTH_ANSWER = [By.XPATH, "//div[@id='accordion__panel-5']"]
    SEVENTH_QUESTION = [By.XPATH, "//div[@id='accordion__heading-6']"]
    SEVENTH_ANSWER = [By.XPATH, "//div[@id='accordion__panel-6']"]
    EIGHTH_QUESTION = [By.XPATH, "//div[@id='accordion__heading-7']"]
    EIGHTH_ANSWER = [By.XPATH, "//div[@id='accordion__panel-7']"]

class QaScooterOrderPageLocators:
    NAME_INPUT = [By.XPATH, "//input[contains(@placeholder, 'Имя')]"]
    SURNAME_INPUT = [By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"]
    ADDRESS_INPUT = [By.XPATH, "//input[contains(@placeholder, 'Адрес')]"]
    METRO_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Станция метро')]"]
    @staticmethod
    def metro_button(metro_station: str):
        return [By.XPATH, f".//div[text()='{metro_station}']/parent::button"]
    TELEPHONE_NUMBER = [By.XPATH, "//input[contains(@placeholder, 'Телефон: на него позвонит курьер')]"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    DATE = [By.XPATH, "//input[contains(@placeholder, 'Когда привезти самокат')]"]
    RENTAL_PERIOD_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    RENTAL_PERIOD = [By.XPATH, ".//div[@class='Dropdown-option']"]
    COLOR_CHOICE = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    COMMENT = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    ORDER_BUTTON = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/button[2]"]
    ACCEPT_BUTTON = [By.XPATH, " //button[contains(text(),'Да')]"]
    order_number = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    SAMOKAT_BUTTON = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/a[2]/img[1]"]
    DZEN_BUTTON = [By.XPATH,  "//body/div[@id='root']/div[1]/div[1]/div[1]/a[1]/img[1]"]

