import allure
import pytest


from conftest import driver
from data import QaScooterOrderPageCorrectData
from locators import QaScooterOrderPageLocators
from pages.order_page import QaScooterOrderPage
from urls import Urls


class TestQaScooterOrderPage:
    @allure.title('Создание заказа через верхнюю кнопку "Заказать"')
    @allure.description('Проверка, через верхнюю кнопку "Заказать", что при корректном заполнении всех полей заказ успешно оформится и присвоится номер')
    @pytest.mark.parametrize('correct_data1', [QaScooterOrderPageCorrectData.correct_data1])
    def test_order_page_through_upper_order_button_order_created_successfully(self, driver, correct_data1):
        qa_scooter_order_page = QaScooterOrderPage(driver)
        qa_scooter_order_page.go_to_site()
        qa_scooter_order_page.click_cookie_accept()
        qa_scooter_order_page.click_upper_button_order()
        qa_scooter_order_page.fill_user_data(correct_data1)
        qa_scooter_order_page.click_next_button()
        qa_scooter_order_page.fill_about_rent(correct_data1)
        qa_scooter_order_page.click_order_button()
        qa_scooter_order_page.click_accept_button()
        result = 'Номер заказа'
        assert result in qa_scooter_order_page.receiving_the_order_text()

    @allure.title('Создание заказа через нижнюю кнопку "Заказать"')
    @allure.description('Проверка, через нижнюю кнопку "Заказать", что при корректном заполнении всех полей заказ успешно оформится и присвоится номер')
    @pytest.mark.parametrize('correct_data2', [QaScooterOrderPageCorrectData.correct_data2])
    def test_order_page_through_lower_order_button_order_created_successfully(self, driver, correct_data2):
        qa_scooter_order_page = QaScooterOrderPage(driver)
        qa_scooter_order_page.go_to_site()
        qa_scooter_order_page.click_cookie_accept()
        qa_scooter_order_page.click_lower_button_order()
        qa_scooter_order_page.fill_user_data(correct_data2)
        qa_scooter_order_page.click_next_button()
        qa_scooter_order_page.fill_about_rent(correct_data2)
        qa_scooter_order_page.click_order_button()
        qa_scooter_order_page.click_accept_button()
        result = 'Номер заказа'
        assert result in qa_scooter_order_page.receiving_the_order_text()

    @allure.title('Проверка кнопки "Самокат" для перехода на главную страницу')
    @allure.description('Проверка кнопки "Самокат" для перехода на главную страницу, через страницу заказа')
    def test_order_page_click_button_samokat_go_to_home_page(self, driver):
        qa_scooter_order_page = QaScooterOrderPage(driver)
        qa_scooter_order_page.go_to_site()
        qa_scooter_order_page.click_cookie_accept()
        qa_scooter_order_page.click_upper_button_order()
        qa_scooter_order_page.click_button_samokat()
        current_url = qa_scooter_order_page.current_url()
        assert Urls.MAIN_PAGE == current_url

    @allure.title('Проверка кнопки "Яндекс" для перехода на страницу Яндекс Дзен')
    @allure.description('Проверка кнопки "Яндекс" для перехода на страницу Яндекс Дзен, через страницу заказа')
    def test_order_page_click_button_dzen_go_to_dzen_page(self, driver):
        qa_scooter_order_page = QaScooterOrderPage(driver)
        qa_scooter_order_page.go_to_site()
        qa_scooter_order_page.click_cookie_accept()
        qa_scooter_order_page.click_upper_button_order()
        qa_scooter_order_page.click_button_dzen()
        qa_scooter_order_page.switch_windows(1)
        qa_scooter_order_page.wait_url()
        current_url = qa_scooter_order_page.current_url()
        assert Urls.DZEN_PAGE == current_url








