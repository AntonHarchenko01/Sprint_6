import allure

from locators import BasePageLocators, QaScooterHomePageLocators
from pages.base_page import BasePage



class QaScooterHomePage(BasePage):
    @allure.step('Нажать на кнопку "да все привыкли" в куках')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocators.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Нажать на первый вопрос')
    def click_first_question(self):
        return self.find_element(QaScooterHomePageLocators.FIRST_QUESTION).click()

    @allure.step('Нажать на второй вопрос')
    def click_second_question(self):
        return self.find_element(QaScooterHomePageLocators.SECOND_QUESTION).click()

    @allure.step('Нажать на третий вопрос')
    def click_third_question(self):
        return self.find_element(QaScooterHomePageLocators.THIRD_QUESTION).click()

    @allure.step('Нажать на четвертый вопрос')
    def click_fourth_question(self):
        return self.find_element(QaScooterHomePageLocators.FOURTH_QUESTION).click()

    @allure.step('Нажать на пятый вопрос')
    def click_fifth_question(self):
        return self.find_element(QaScooterHomePageLocators.FIFTH_QUESTION).click()

    @allure.step('Нажать на шестой вопрос')
    def click_sixth_question(self):
        return self.find_element(QaScooterHomePageLocators.SIXTH_QUESTION).click()

    @allure.step('Нажать на седьмой вопрос')
    def click_seventh_question(self):
        return self.find_element(QaScooterHomePageLocators.SEVENTH_QUESTION).click()

    @allure.step('Нажать на восьмой вопрос')
    def click_eighth_question(self):
        return self.find_element(QaScooterHomePageLocators.EIGHTH_QUESTION).click()