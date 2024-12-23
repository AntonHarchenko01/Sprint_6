import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators, QaScooterOrderPageLocators
from pages.base_page import BasePage
from urls import Urls


class QaScooterOrderPage(BasePage):
    @allure.step('Нажать на кнопку "да все привыкли" в куках')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocators.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_upper_button_order(self):
        return self.find_element(BasePageLocators.UPPER_BUTTON_ORDER).click()

    @allure.step('Ввод имени')
    def input_name(self, name: str):
        return self.find_element(QaScooterOrderPageLocators.NAME_INPUT).send_keys(name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname: str):
        return self.find_element(QaScooterOrderPageLocators.SURNAME_INPUT).send_keys(surname)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(QaScooterOrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбор метро')
    def metro_choice(self, metro_station: str):
        self.find_element(QaScooterOrderPageLocators.METRO_FIELD).click()
        return self.find_element(QaScooterOrderPageLocators.metro_button(metro_station)).click()

    @allure.step('Ввод номера телефона')
    def input_telephone_number(self, telephone_number: str):
        self.find_element(QaScooterOrderPageLocators.TELEPHONE_NUMBER).send_keys(telephone_number)

    @allure.step('Нажатие кнопки далее, переход для заполнения полей "Про аренду"')
    def click_next_button(self):
        return self.find_element(QaScooterOrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Ввод даты "Когда привезти самокат"')
    def input_date(self, date: str):
        return self.find_element(QaScooterOrderPageLocators.DATE).send_keys(date)

    @allure.step('Выбор срока аренды')
    def rental_period_choice(self, rental_period: int):
        self.find_element(QaScooterOrderPageLocators.RENTAL_PERIOD_FIELD).click()
        return self.find_elements(QaScooterOrderPageLocators.RENTAL_PERIOD)[rental_period].click()

    @allure.step('Выбор цвета')
    def color_choice(self, color: int):
        return self.find_elements(QaScooterOrderPageLocators.COLOR_CHOICE)[color].click()

    @allure.step('Ввод Комментария для курьера')
    def input_comment(self, comment_for_the_courier):
        return self.find_element(QaScooterOrderPageLocators.COMMENT).send_keys(comment_for_the_courier)

    def fill_user_data(self, correct_data1: dict):
        self.input_name(correct_data1['name'])
        self.input_surname(correct_data1['surname'])
        self.input_address(correct_data1['address'])
        self.metro_choice(correct_data1['metro_station'])
        self.input_telephone_number(correct_data1['telephone_number'])

    def fill_about_rent(self, correct_data1: dict):
        self.input_date(correct_data1['date'])
        self.rental_period_choice(correct_data1['rental_period'])
        self.color_choice(correct_data1['color'])
        self.input_comment(correct_data1['comment_for_the_courier'])

    @allure.step('Нажать кнопку заказать')
    def click_order_button(self):
        return self.find_element(QaScooterOrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Нажать кнопку подтверждения заказа')
    def click_accept_button(self):
        return self.find_element(QaScooterOrderPageLocators.ACCEPT_BUTTON).click()

    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_lower_button_order(self):
        return self.find_element(BasePageLocators.LOWER_BUTTON_ORDER).click()

    @allure.step('Нажать кнопку "Самокат"')
    def click_button_samokat(self):
        return self.find_element(QaScooterOrderPageLocators.SAMOKAT_BUTTON).click()

    @allure.step('Нажать кнопку "ЯндексДзен"')
    def click_button_dzen(self):
        return self.find_element(QaScooterOrderPageLocators.DZEN_BUTTON).click()

    @allure.step('Переключится на следующую вкладку браузера')
    def switch_windows(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Ожидание url для новой вкладки')
    def wait_url(self, time = 10):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(Urls.DZEN_PAGE))




