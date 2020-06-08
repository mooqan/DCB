
import allure
import pytest
from allure_commons.types import AttachmentType

from confHelper.configHelper import capsAnroid
from confHelper.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from confHelper.auth import *
import time


@allure.epic("Epic #2 - Модуль Личного кабинета О!")
@allure.feature("Feature #1 - Личный кабинет")
@allure.severity(allure.severity_level.CRITICAL)
class Test_lk(capsAnroid):
    @allure.story("Story #1 - Главная страница Личного кабинета")
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



@allure.epic("Epic #2 - Модуль Личного кабинета О!")
@allure.feature("Feature #2 - боковое меню ЛК")
class Test_left_menu(capsAnroid):
    @allure.story("Story #1 - Профиль ЛК")
    @allure.title("Тест.сохранения профиля ЛК")
    @allure.description("Проверка работоспособности сохраниения профиля ЛК")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.skip(reason="не требуется")
    def test_lk_save_profile(self, driver):
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
        with allure.step("Step 6 проверка нажатия кнопки сохранения"):
            click_by_id(driver, "btn_profile_save", scrn=True, sleep=True)

    @allure.story("Story #2 - Смена языка")
    @allure.title("Тест.Смена языка")
    @allure.description("Проверка работоспособности смены языка профиля ЛК")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.skip(reason="не требуется")
    def test_lk_change_lang(self, driver):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driver)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в боковое меню"):
            click_by_xpath(driver, "btn_left_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно смена языка"):
            click_by_xpath(driver, "btn_choose_language", scrn=True, sleep=True)
        with allure.step("Step 3 проверка выбора другого языка"):
            click_by_id(driver, "btn_choose_ru_lang", scrn=True, sleep=True)
        with allure.step("Step 4 проверка выбора другого языка подтверждение"):
            c = driver.find_element_by_id("android:id/button1")
            c.click()
            time.sleep(5)
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.story("Story #3 - офисы и терминалы")
    @allure.title("Тест.Офисы и терминалы")
    @allure.description("Проверка работоспособности отображения офисов и перехода в окне 'Офисы и терминалы'")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.skip(reason="не требуется")
    def test_office_and_terminals(self, driver):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driver)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в боковое меню"):
            click_by_xpath(driver, "btn_left_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно 'Офисы и терминалы'"):
            click_by_xpath(driver, "btn_office_terminals", scrn=True, sleep=True)
        with allure.step("Step 3 проверка перехода в список офисов"):
            click_by_id(driver, "btn_office_list", scrn=True, sleep=True)
        with allure.step("Step 4 проверка перехода в первый офис в списке"):
            click_by_xpath(driver, "btn_first_office", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 5 проверка переъода в список терминалов"):
            click_by_xpath(driver, "btn_page_terminals", scrn=True, sleep=True)
        with allure.step("Step 6 проверка перехода в первый терминал в списке"):
            click_by_xpath(driver, "btn_first_terminal", scrn=True, sleep=True)
            driver.back()

    @allure.story("Story #4 - места оплаты")
    @allure.title("Тест.Места оплаты")
    @allure.description("Проверка работоспособности отображения мест оплаты в 'Места оплаты'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_place_of_payment(self, driver):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driver)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в боковое меню"):
            click_by_xpath(driver, "btn_left_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно 'Места оплаты'"):
            click_by_xpath(driver, "btn_place_of_payment", scrn=True, sleep=True)
        with allure.step("Step 3 проверка перехода в окно 'Офисы и терминалы'"):
            click_by_xpath(driver, "cnt_search_place_of_payment", scrn=True, sleep=True)
        with allure.step("Step 4 проверка открытия поиска в окне 'Офисы и терминалы'"):
            send_keys_by_id(driver, "cnt_search_field_place_of_payment", "boris", scrn=True, sleep=True)
        with allure.step("Step 5 проверка ввода в поиск в 'Офисы и терминалы'"):
            click_by_xpath(driver, "btn_search_result_place_of_payment", scrn=True, sleep=True)
        with allure.step("Step 6 проверка перехода в окно оплаты после поиска в 'Офисы и терминалы'"):
            click_by_id(driver, "btn_place_of_payment_payment", scrn=True, sleep=True)











