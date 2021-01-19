import time
import allure
import pytest

from allure_commons.types import AttachmentType
from appium.webdriver.common.touch_action import TouchAction
from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import send_keys_by_xpath
from confHelper.configHelperAndroid.authAndroid import *


@allure.epic("Epic #2 - Модуль Личного кабинета О!")
@allure.feature("Feature #1 - Личный кабинет")
@allure.story("Story #1 - Главная страница Личного кабинета")
@allure.severity(allure.severity_level.CRITICAL)
class Test_lk(capsAnroid):
    @allure.title("Тест.переходы на главном экране ЛК")
    @allure.description("Проверка работоспособности переходов на главной странице ЛК")
    @pytest.mark.skip(reason="не требуется")
    def test_main_page(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода на пополнение мобильного баланса"):
            click_by_id(driverAndroid, "btn_refill", scrn=True, sleep=True)
            driverAndroid.back()
        with allure.step("Step 2 проверка перехода в окно доступного интернет трафика"):
            click_by_id(driverAndroid, "btn_internet", scrn=True, sleep=True)
            driverAndroid.back()
        with allure.step("Step 3 проверка перехода в окно доступного трафика билинга"):
            click_by_id(driverAndroid, "btn_outgoing_call", scrn=True, sleep=True)
            driverAndroid.back()
        with allure.step("Step 4 проверка перехода в окно 'Мои номера'"):
            click_by_id(driverAndroid, "btn_sub_numbers", scrn=True, sleep=True)
            driverAndroid.back()
        # with allure.step("Step 5 проверка перехода в окно 'Лотерея'"):
        #     click_by_id(driver, "btn_lottery", scrn=True, sleep=True)
        #     driver.back()
        with allure.step("Step 6 проверка перехода в окно 'Сервисы'"):
            click_by_id(driverAndroid, "btn_services", scrn=True, sleep=True)
            driverAndroid.back()
        with allure.step("Step 7 проверка перехода в окно 'Тарифы'"):
            click_by_id(driverAndroid, "btn_tariffs", scrn=True, sleep=True)
            driverAndroid.back()
        with allure.step("Step 8 проверка перехода в окно 'Детализация'"):
            TouchAction(driverAndroid).press(x=478, y=1612).move_to(x=503, y=895).release().perform()
            click_by_id(driverAndroid, "btn_detalizatation", scrn=True, sleep=True)
            driverAndroid.back()



@allure.epic("Epic #2 - Модуль Личного кабинета О!")
@allure.feature("Feature #2 - боковое меню ЛК")
class Test_left_menu(capsAnroid):
    @allure.story("Story #1 - Профиль ЛК")
    @allure.title("Тест.сохранения профиля ЛК")
    @allure.description("Проверка работоспособности сохраниения профиля ЛК")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.skip(reason="не требуется")
    def test_lk_save_profile(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно  'Профиля'"):
            click_by_id(driverAndroid, "btn_edit_profile", scrn=True, sleep=True)
        with allure.step("Step 3 проверка заполнения почты в окне 'Профиля'"):
            send_keys_by_xpath(driverAndroid, "cnt_email", "ripvantesla@gmail.com", scrn=True, sleep=True)
        with allure.step("Step 4 проверка заполнения имени в окне 'Профиля'"):
            send_keys_by_xpath(driverAndroid, "cnt_name", "Anatolii", scrn=True, sleep=True)
        with allure.step("Step 5 проверка заполнения фамилии в окне 'Профиля'"):
            send_keys_by_xpath(driverAndroid, "cnt_last_name1", "Petrov", scrn=True, sleep=True)
        with allure.step("Step 6 проверка нажатия кнопки сохранения"):
            click_by_xpath(driverAndroid, "btn_profile_save", scrn=True, sleep=True)

    @allure.story("Story #2 - Смена языка")
    @allure.title("Тест.Смена языка")
    @allure.description("Проверка работоспособности смены языка профиля ЛК")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="не требуется")
    def test_lk_change_lang(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно смена языка"):
            click_by_id(driverAndroid, "btn_menu_change_lang", scrn=True, sleep=True)
        with allure.step("Step 3 проверка выбора другого языка"):
            click_by_id(driverAndroid, "btn_choose_ru_lang", scrn=True, sleep=True)
        with allure.step("Step 4 проверка выбора другого языка подтверждение"):
            c = driverAndroid.find_element_by_id("android:id/button1")
            c.click()
            time.sleep(5)
            allure.attach(driverAndroid.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.story("Story #3 - офисы и терминалы")
    @allure.title("Тест.Офисы и терминалы")
    @allure.description("Проверка работоспособности отображения офисов и перехода в окне 'Офисы и терминалы'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="не требуется")
    def test_office_and_terminals(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в боковое меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно 'Офисы и терминалы'"):
            click_by_id(driverAndroid, "btn_menu_office_map", scrn=True, sleep=True)
        with allure.step("Step 3 проверка перехода в список офисов"):
            click_by_id(driverAndroid, "btn_office_list", scrn=True, sleep=True)
        with allure.step("Step 4 проверка перехода в первый офис в списке"):
            click_by_xpath(driverAndroid, "btn_first_office", scrn=True, sleep=True)
            driverAndroid.back()
        with allure.step("Step 5 проверка переъода в список терминалов"):
            click_by_xpath(driverAndroid, "btn_page_terminals", scrn=True, sleep=True)
        with allure.step("Step 6 проверка перехода в первый терминал в списке"):
            click_by_xpath(driverAndroid, "btn_first_terminal", scrn=True, sleep=True)
            driverAndroid.back()

    @allure.story("Story #4 - места оплаты")
    @allure.title("Тест.Места оплаты")
    @allure.description("Проверка работоспособности отображения мест оплаты в 'Места оплаты'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="не требуется")
    def test_place_of_payment(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в боковое меню"):
            click_by_xpath(driverAndroid, "btn_left_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно 'Места оплаты'"):
            click_by_xpath(driverAndroid, "btn_place_of_payment", scrn=True, sleep=True)
        with allure.step("Step 3 проверка перехода в окно 'Офисы и терминалы'"):
            click_by_xpath(driverAndroid, "cnt_search_place_of_payment", scrn=True, sleep=True)
        with allure.step("Step 4 проверка открытия поиска в окне 'Офисы и терминалы'"):
            send_keys_by_id(driverAndroid, "cnt_search_field_place_of_payment", "boris", scrn=True, sleep=True)
        with allure.step("Step 5 проверка ввода в поиск в 'Офисы и терминалы'"):
            click_by_xpath(driverAndroid, "btn_search_result_place_of_payment", scrn=True, sleep=True)
        with allure.step("Step 6 проверка перехода в окно оплаты после поиска в 'Офисы и терминалы'"):
            click_by_id(driverAndroid, "btn_place_of_payment_payment", scrn=True, sleep=True)