from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import *
from confHelper.configHelperAndroid.authAndroid import Test_authorization
import pytest


@allure.epic("Epic #1 - Модуль авторизации DCB360")
@allure.feature("Feature #1 - Авторизация в DCB360")
@allure.severity(allure.severity_level.CRITICAL)
class Test_Auth_DCB360(capsAnroid):
    @allure.story("Story #1 - Авторизация зарегистрированного пользователя")
    @allure.title("Проверка входа с валидными данными")
    @allure.description("Проверка входа в приложение DCB360 зарегистрированного пользователя")
    @allure.issue("https://mail.ru/")  # Пример ссылки на задачу или дефект
    @allure.testcase("https://app.qase.io/case/DCB360-1")  # Пример ссылки на тест-кейс
    def test_auth_positive(self, driverAndroid):
        with allure.step("Step #0 Открытие приложения"):
            screenshot(driverAndroid)
            click_by_id(driverAndroid, "tab_payment", scrn=True)
        with allure.step("Step #1 Ввод номера/логина"):
            click_by_xpath(driverAndroid, "view_dcb", scrn=True)
            send_keys_by_xpath(driverAndroid, "cnt_phoneNumber", "773 252 919", scrn=True)
        with allure.step("Step #2 Ввод пароля"):
            send_keys_by_xpath(driverAndroid, "cnt_phonePassword", "Makiavelli01", scrn=True)
        with allure.step("Step #3 Нажатие кнопки входа"):
            click_by_xpath(driverAndroid,"btn_enter", scrn=True)
        with allure.step("Step #4 Создание пинкода"):
            for _ in range(4):
                click_by_id(driverAndroid, "btn_5pincode", scrn=True)
        with allure.step("Step #5 Подтверждение пинкода"):
            for _ in range(4):
                click_by_id(driverAndroid, "btn_5pincode", scrn=True)

    @allure.story("Story #1 - Авторизация зарегистрированного пользователя")
    @allure.title("Проверка входа с не валидными данными")
    @allure.description("Проверка входа в приложение DCB360 неверными данными для авторизации")
    @allure.issue("https://mail.ru/")  # Пример ссылки на задачу или дефект
    @allure.testcase("https://app.qase.io/case/DCB360-1")  # Пример ссылки на тест-кейс
    def test_auth_negative(self, driverAndroid):
        with allure.step("Step #0 Открытие приложения"):
            screenshot(driverAndroid)
            click_by_id(driverAndroid, "tab_payment", scrn=True)
        with allure.step("Step #1 Ввод номера невалидного номера"):
            click_by_xpath(driverAndroid, "view_dcb", scrn=True)
            send_keys_by_xpath(driverAndroid, "cnt_phoneNumber", "000 000 000", scrn=True)
        with allure.step("Step #2 Ввод невалидного пароля"):
            send_keys_by_xpath(driverAndroid, "cnt_phonePassword", "Makiavelli06", scrn=True)
        with allure.step("Step #3 Нажатие кнопки входа"):
            click_by_xpath(driverAndroid,"btn_enter", scrn=True)
        with allure.step("Step #4 Нажатие кнопки попробуйте еще раз"):
            screenshot(driverAndroid)
            click_by_xpath(driverAndroid,"btn_try_again", scrn=True)

    @allure.story("Story #2 - Регистрация нового пользователя")
    @allure.title("Проверка флоу регистрации нового пользователя")
    @allure.description("Проверка регистрации нового пользователя по флоу регистрации")
    @allure.issue("https://mail.ru/")  # Пример ссылки на задачу или дефект
    @allure.testcase("https://app.qase.io/case/DCB360-1")  # Пример ссылки на тест-кейс
    def test_register_positive(self, driverAndroid):
        with allure.step("Step #0 Открытие приложения"):
            screenshot(driverAndroid)
            click_by_id(driverAndroid, "tab_payment", scrn=True)
        with allure.step("Step #1 Нажатие кнопки зарегистрироваться"):
            click_by_xpath(driverAndroid, "view_dcb", scrn=True)
            click_by_xpath(driverAndroid,"btn_register", scrn=True)
        with allure.step("Step #2 Ввод номера для регистрации"):
            send_keys_by_xpath(driverAndroid, "cnt_phoneNumber_register", "773 252 919", scrn=True)
        with allure.step("Step #3 Нажатие кнопки далее"):
            click_by_xpath(driverAndroid, "btn_next_register", scrn=True)
        with allure.step("Step #4 Ввод пароля для регистрации"):
            send_keys_by_xpath(driverAndroid, "cnt_password_register", "Makiavelli94", scrn=True)
        with allure.step("Step #5 Ввод пароля для одтверждения пароля"):
            send_keys_by_xpath(driverAndroid, "cnt_password1_register", "Makiavelli94", scrn=True)
        with allure.step("Step #6 Нажатие кнопки далее"):
            click_by_xpath(driverAndroid, "btn_next1_register", scrn=True)
