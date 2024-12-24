import pytest
import allure

from data import QaScooterHomePageAnswers
from locators import QaScooterHomePageLocators
from pages.home_page import QaScooterHomePage
from conftest import driver

class TestQaScooterQuestionsPage:
    @allure.title('При нажатии на первый вопрос раскрывается ответ')
    @allure.description('Проверка, что при нажатии первого вопроса (первого сверху), в секции "Вопросы о важном", раскрывается ожидаемый ответ')
    def test_questions_click_first_question_show_answer(self, driver):
        qa_scooter_home_page = QaScooterHomePage(driver)
        qa_scooter_home_page.go_to_site()
        qa_scooter_home_page.click_cookie_accept()
        qa_scooter_home_page.click_first_question()
        answer = qa_scooter_home_page.get_first_answer()
        assert answer.is_displayed() and answer.text == QaScooterHomePageAnswers.answer1, f'Ответ на первый вопрос не соответствует ожидаемому значению{answer}'

    @allure.title('При нажатии на второй вопрос раскрывается ответ')
    @allure.description('Проверка, что при нажатии второго вопроса (второго сверху), в секции "Вопросы о важном", раскрывается ожидаемый ответ')
    def test_questions_click_second_question_show_answer(self, driver):
        qa_scooter_home_page = QaScooterHomePage(driver)
        qa_scooter_home_page.go_to_site()
        qa_scooter_home_page.click_cookie_accept()
        qa_scooter_home_page.click_second_question()
        answer = qa_scooter_home_page.get_second_answer()
        assert answer.is_displayed() and answer.text == QaScooterHomePageAnswers.answer2, 'Ответ на второй вопрос не соответствует ожидаемому значению'

    @allure.title('При нажатии на третий вопрос раскрывается ответ')
    @allure.description('Проверка, что при нажатии третьего вопроса (третьего сверху), в секции "Вопросы о важном", раскрывается ожидаемый ответ')
    def test_question_click_third_question_show_answer(self, driver):
        qa_scooter_home_page = QaScooterHomePage(driver)
        qa_scooter_home_page.go_to_site()
        qa_scooter_home_page.click_cookie_accept()
        qa_scooter_home_page.click_third_question()
        answer = qa_scooter_home_page.get_third_answer()
        assert answer.is_displayed() and answer.text == QaScooterHomePageAnswers.answer3, 'Ответ на третий вопрос не соответствует ожидаемому значению'

    @allure.title('При нажатии на четвертый вопрос раскрывается ответ')
    @allure.description('Проверка, что при нажатии четвертого вопроса (четвертого сверху), в секции "Вопросы о важном", раскрывается ожидаемый ответ')
    def test_question_click_fourth_question_show_answer(self, driver):
        qa_scooter_home_page = QaScooterHomePage(driver)
        qa_scooter_home_page.go_to_site()
        qa_scooter_home_page.click_cookie_accept()
        qa_scooter_home_page.click_fourth_question()
        answer = qa_scooter_home_page.get_fourth_answer()
        assert answer.is_displayed() and answer.text == QaScooterHomePageAnswers.answer4, 'Ответ на четвертый вопрос не соответствует ожидаемому значению'

    @allure.title('При нажатии на пятый вопрос раскрывается ответ')
    @allure.description('Проверка, что при нажатии пятого вопроса (пятого сверху), в секции "Вопросы о важном", раскрывается ожидаемый ответ')
    def test_question_click_fifth_question_show_answer(self, driver):
        qa_scooter_home_page = QaScooterHomePage(driver)
        qa_scooter_home_page.go_to_site()
        qa_scooter_home_page.click_cookie_accept()
        qa_scooter_home_page.click_fifth_question()
        answer = qa_scooter_home_page.get_fifth_answer()
        assert answer.is_displayed() and answer.text == QaScooterHomePageAnswers.answer5, 'Ответ на пятый вопрос не соответствует ожидаемому значению'

    @allure.title('При нажатии на шестой вопрос раскрывается ответ')
    @allure.description('Проверка, что при нажатии шестого вопроса (шестого сверху), в секции "Вопросы о важном", раскрывается ожидаемый ответ')
    def test_question_click_sixth_question_show_answer(self, driver):
        qa_scooter_home_page = QaScooterHomePage(driver)
        qa_scooter_home_page.go_to_site()
        qa_scooter_home_page.click_cookie_accept()
        qa_scooter_home_page.click_sixth_question()
        answer = qa_scooter_home_page.get_sixth_answer()
        assert answer.is_displayed() and answer.text == QaScooterHomePageAnswers.answer6, 'Ответ на шестой вопрос не соответствует ожидаемому значению'

    @allure.title('При нажатии на седьмой вопрос раскрывается ответ')
    @allure.description('Проверка, что при нажатии седьмого вопроса (седьмого сверху), в секции "Вопросы о важном", раскрывается ожидаемый ответ')
    def test_question_click_seventh_question_show_answer(self, driver):
        qa_scooter_home_page = QaScooterHomePage(driver)
        qa_scooter_home_page.go_to_site()
        qa_scooter_home_page.click_cookie_accept()
        qa_scooter_home_page.click_seventh_question()
        answer = qa_scooter_home_page.get_seventh_answer()
        assert answer.is_displayed() and answer.text == QaScooterHomePageAnswers.answer7, 'Ответ на седьмой вопрос не соответствует ожидаемому значению'

    @allure.title('При нажатии на восьмой вопрос раскрывается ответ')
    @allure.description('Проверка, что при нажатии восьмого вопроса (восьмого сверху), в секции "Вопросы о важном", раскрывается ожидаемый ответ')
    def test_question_click_eighth_question_show_answer(self, driver):
        qa_scooter_home_page = QaScooterHomePage(driver)
        qa_scooter_home_page.go_to_site()
        qa_scooter_home_page.click_cookie_accept()
        qa_scooter_home_page.click_eighth_question()
        answer = qa_scooter_home_page.get_eighth_answer()
        assert answer.is_displayed() and answer.text == QaScooterHomePageAnswers.answer8, 'Ответ на восьмой вопрос не соответствует ожидаемому значению'