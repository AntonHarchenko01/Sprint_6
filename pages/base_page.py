import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')
    def go_to_site(self):
        url = Urls.MAIN_PAGE
        self.driver.get(url)

    def find_element(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find element {locator}')

    def find_elements(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not find elements {locator}')

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url