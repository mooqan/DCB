import allure

from confHelper.configHelper import capsAnroid
from confHelper.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from confHelper.auth import *

@allure.epic("Epic #2")
@allure.feature("Feature #1 - Личный кабинет")
@allure.story("Story #1 - Личный кабинет")
class Test_lk1(capsAnroid):
    @allure.title("Тест.переходы на главном экране ЛК")
    @allure.description("Проверка работоспособности переходов на главной странице ЛК")
    def test_main_page(self, driver):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driver)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода на пополнение мобильного баланса"):
            click_by_id(driver, "btn_refill", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 2 проверка перехода в окно доступного интернет трафика"):
            click_by_id(driver, "btn_internet", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 3 проверка перехода в окно доступного трафика билинга"):
            click_by_id(driver, "btn_outgoing_call", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 4 проверка перехода в окно 'Мои номера'"):
            click_by_id(driver, "btn_sub_numbers", scrn=True, sleep=True)
            driver.back()
        # with allure.step("Step 5 проверка перехода в окно 'Лотерея'"):
        #     click_by_id(driver, "btn_lottery", scrn=True, sleep=True)
        #     driver.back()
        with allure.step("Step 6 проверка перехода в окно 'Сервисы'"):
            click_by_id(driver, "btn_services", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 7 проверка перехода в окно 'Тарифы'"):
            click_by_id(driver, "btn_tariffs", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 8 проверка перехода в окно 'Детализация'"):
            click_by_id(driver, "btn_detalizatation", scrn=True, sleep=True)
            driver.back()
    @allure.title("Тест.сохранения профиля ЛК")
    @allure.description("Проверка работоспособности сохраниения профиля ЛК")
    def test_left_menu_profile(self, driver):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driver)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в боковое меню"):
            click_by_xpath(driver, "btn_left_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно  'Профиля'"):
            click_by_id(driver, "btn_edit_profile", scrn=True, sleep=True)
        with allure.step("Step 3 проверка заполнения почты в окне 'Профиля'"):
            send_keys_by_id(driver, "cnt_email", "ripvantesla@gmail.com", scrn=True, sleep=True)
        with allure.step("Step 4 проверка заполнения имени в окне 'Профиля'"):
            send_keys_by_id(driver, "cnt_name", "Anatolii", scrn=True, sleep=True)
        with allure.step("Step 5 проверка заполнения фамилии в окне 'Профиля'"):
            send_keys_by_xpath(driver, "cnt_last_name", "Petrov", scrn=True, sleep=True)
        with allure.step("Step 6 проверка заполнения почты в окне 'Профиля'"):
            click_by_id(driver, "btn_profile_save", scrn=True, sleep=True)