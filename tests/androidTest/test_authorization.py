from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import *
import allure
import pytest


@allure.epic("Epic #1 - Модуль авторизации в приложении Мой О!")
@allure.feature("Feature #1 - Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
class Test_auth(capsAnroid):
    # !!!Внимание!!! Для успешной проверки этого кейса обязательно потребуется физический девайс
    # в котором будет установлена симкарта с возможностью получения смс кода
    # Также понадобится подписанное приложение продовыми сертификатами (signed)
    # Убедись, что номер в кейсе соответствует номеру симкарты установленной в девайсе
    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка авторизации через смс пользователя НУР-а")
    @allure.description("Проверка прохождения авторизаци пользователем у которого не установлен пароль")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.skip(reason="Требуются особые условия")
    def test_auth_sms(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 241 942", scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Отменяем запрос на включение биометрии и открываем экран ЛК"):
            driverAndroid.switch_to_alert().dismiss()
            driverAndroid.wait_activity(".ui.main.MainActivity", 10)
            screenshot(driverAndroid, sleep=True)
            click_by_id(driverAndroid, "space_out_cntn")
            click_by_id(driverAndroid, "btn_scanner_cancel", sleep=True, scrn=True)

    # !!!Для этого кейса нужно сбрасывать счетчик блокировки ввода смс кода
    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка ввода неверного смс кода")
    @allure.description("Проверка отображения ошибки при вводе неверного смс кода")
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.skip(reason="Требуются особые условия")
    def test_auth_incorrect_sms_code(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 245 443", scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Вводим неверный смс код"):
            send_keys_by_xpath(driverAndroid, "cnt_phone_pswrd", "123456", scrn=True)
        with allure.step("Step #4 Нажимаем далее и видим ошибку"):
            click_by_id(driverAndroid, "btn_phone_pswrd_next", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка авторизации пользователя НУР-а через пароль")
    @allure.description("Проверка работы авторизации")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_pass(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 243 851", scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Вводим действующий пароль"):
            send_keys_by_xpath(driverAndroid, "cnt_phone_pswrd", "Test12345", scrn=True)
        with allure.step("Step #4 Нажимаем на Далее"):
            click_by_id(driverAndroid, "btn_phone_pswrd_next", sleep=True, scrn=True)
        with allure.step("Step #5 Отменяем запрос на включение биометрии и открываем экран ЛК"):
            driverAndroid.switch_to_alert().dismiss()
            driverAndroid.wait_activity(".ui.main.MainActivity", 10)
            screenshot(driverAndroid, sleep=True)
            click_by_id(driverAndroid, "btn_scanner_cancel", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка авторизации пользователя других операторов")
    @allure.description("Проверка работы авторизации абонентов других операторов")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_other_operators_pass(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 777 395 669", scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Вводим действующий пароль"):
            send_keys_by_xpath(driverAndroid, "cnt_phone_pswrd", "Test12345", scrn=True)
        with allure.step("Step #4 Нажимаем на Далее"):
            click_by_id(driverAndroid, "btn_phone_pswrd_next", sleep=True, scrn=True)
        with allure.step("Step #5 Отменяем запрос на включение биометрии и открываем экран ЛК"):
            driverAndroid.switch_to_alert().dismiss()
            driverAndroid.wait_activity(".ui.main.MainActivity", 10)
            back(driverAndroid)
            screenshot(driverAndroid, sleep=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка открытия экрана условий предоставления сервисов")
    @allure.description("Проверка перехода на экран условий предоставления сервисов")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_service_conditions(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 777 395 669", scrn=True)
        with allure.step("Step #2 Переход к условиям предоставления сервисов"):
            click_by_id(driverAndroid, "btn_service_conditions", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка переключения кнопки при отмене/согласии с условиями сервиса")
    @allure.description("Проверка переключения кнопки (неактивна/активна) на экране подтверждения условий сервиса при "
                        "отмене/согласии с условиями сервиса")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_service_conditions_not_accept(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 777 395 669", scrn=True)
        with allure.step("Step #2 Переход к условиям предоставления сервисов"):
            click_by_id(driverAndroid, "btn_service_conditions", sleep=True, scrn=True)
        with allure.step("Step #3 Отмена согласия на сбор информации"):
            click_by_id(driverAndroid, "checkbox_conditions", sleep=True, scrn=True)
        with allure.step("Step #4 Отмена условий пользовательского соглашения"):
            click_by_id(driverAndroid, "checkbox_terms_of_use", sleep=True, scrn=True)
        with allure.step("Step #5 Отмена согласия с возрастом"):
            click_by_id(driverAndroid, "checkbox_18_years", sleep=True, scrn=True)
        with allure.step("Step #6 Согласие на сбор информации"):
            click_by_id(driverAndroid, "checkbox_conditions", sleep=True, scrn=True)
        with allure.step("Step #7 Согласие с пользовательским соглашением и офертой"):
            click_by_id(driverAndroid, "checkbox_terms_of_use", sleep=True, scrn=True)
        with allure.step("Step #8 Согласие с возрастом"):
            click_by_id(driverAndroid, "checkbox_18_years", sleep=True, scrn=True)
        with allure.step("Step #9 Переход на экран пароля согласившись с условиями сервиса"):
            click_by_id(driverAndroid, "btn_next_condition", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка перехода на экран оферт нажав на кнопку войти без согласия с офертами")
    @allure.description("Проверка перехода на экран оферт нажав на кнопку войти без согласия с офертами")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_service_conditions_not_accept_from_enter(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 777 395 669", scrn=True)
        with allure.step("Step #2 Переход к условиям предоставления сервисов"):
            click_by_id(driverAndroid, "btn_service_conditions", sleep=True, scrn=True)
        with allure.step("Step #3 Отмена согласия на сбор информации"):
            click_by_id(driverAndroid, "checkbox_conditions", sleep=True, scrn=True)
        with allure.step("Step #4 Отмена условий пользовательского соглашения"):
            click_by_id(driverAndroid, "checkbox_terms_of_use", sleep=True, scrn=True)
        with allure.step("Step #5 Отмена согласия с возрастом"):
            click_by_id(driverAndroid, "checkbox_18_years", sleep=True, scrn=True)
        with allure.step("Step #6 Возврат на ввод номера не соглашаясь с условиями"):
            back(driverAndroid, sleep=True, scrn=True)
        with allure.step("Step #7 Нажимаем Войти без согласия с условиями"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка перехода на оферту оденег")
    @allure.description("Проверка открытия оферты оденег")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_offer(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 777 395 669", scrn=True)
        with allure.step("Step #2 Переход к условиям предоставления сервисов"):
            click_by_id(driverAndroid, "btn_service_conditions", sleep=True, scrn=True)
        with allure.step("Step #3 Просмотр оферты О!Денег"):
            click_by_id(driverAndroid, "btn_wallet_use_term", sleep=True, scrn=True)

    # !!!Для этого кейса нужно сбрасывать счетчик блокировки ввода пароля
    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка ввода неверного пароля")
    @allure.description("Проверка отображения ошибки при вводе неверного пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip(reason="Требуются особые условия")
    def test_auth_incorrect_pass(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 243 851",  scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Вводим неверный пароль"):
            send_keys_by_xpath(driverAndroid, "cnt_phone_pswrd", "Passwords", scrn=True)
        with allure.step("Step #4 Нажимаем далее и видим ошибку"):
            click_by_id(driverAndroid, "btn_phone_pswrd_next", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка перехода на список офисов")
    @allure.description("Проверка открытия карты офисов и списка всех офисов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_offices(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 243 851", scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Вводим неверный пароль"):
            send_keys_by_xpath(driverAndroid, "cnt_phone_pswrd", "Passwords", scrn=True)
        with allure.step("Step #4 Нажимаем далее и видим ошибку"):
            click_by_id(driverAndroid, "btn_phone_pswrd_next", sleep=True, scrn=True)
        with allure.step("Step #5 Открываем карту офисов обслуживания"):
            click_by_xpath(driverAndroid, "btn_maps_opio", sleep=True, scrn=True)
        with allure.step("Step #6 Нажимаем на список офисов"):
            click_by_id(driverAndroid, "btn_list_offices", sleep=True, scrn=True)
        with allure.step("Step #20 Нажимаем на конкретный офис"):
            click_by_xpath(driverAndroid, "btn_offices", sleep=True, scrn=True)

    # !!!Внимание!!! Для успешной проверки этого кейса обязательно потребуется физический девайс
    # в котором будет установлена симкарта с возможностью получения смс кода
    # Также понадобится подписанное приложение продовыми сертификатами (signed)
    # Убедись, что номер в кейсе соответствует номеру симкарты установленной в девайсе
    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка сброса пароля через смс код")
    @allure.description("Проверка сброса пароля через смс код")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip(reason="Требуются особые условия")
    def test_auth_reset_pass_via_sms(self, driverAndroid):
        with allure.step("Step Открытие приложения"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 243 851", scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Нажимаем на сброс пароля"):
            click_by_id(driverAndroid, "btn_reset_pass", sleep=True, scrn=True)
        with allure.step("Step #4 Подтверждаем выбор сброса пароля по смс"):
            confirm_allert(driverAndroid, sleep=True, scrn=True)
        with allure.step("Step #5 Нажимаем далее для сброса пароля"):
            click_by_id(driverAndroid, "btn_reset_pswrd_next", sleep=True, scrn=True)
        with allure.step("Step #6 Вводим новый пароль"):
            send_keys_by_xpath(driverAndroid, "cnt_new_pass", "Test12345", scrn=True)
        with allure.step("Step #7 Подтверждаем смену пароля нажимая на далее"):
            click_by_id(driverAndroid, "btn_reset_pswrd_next", sleep=True, scrn=True)
        with allure.step("Step #8 Отменяем запрос на включение биометрии и открываем экран ЛК"):
            driverAndroid.switch_to_alert().dismiss()
            driverAndroid.wait_activity(".ui.main.MainActivity", 10)
            screenshot(driverAndroid, sleep=True)

    # !!!Для этого кейса нужно сбрасывать счетчик блокировки ввода кода из email-a
    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка отображения ошибки при неверном вводе кода сброса пароля с email-а")
    @allure.description("Проверка отображения ошибки при неверном вводе кода сброса пароля с email-а")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip(reason="Требуются особые условия")
    def test_auth_incorrect_reset_pass(self, driverAndroid):
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 243 851", scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Нажимаем на сброс пароля"):
            click_by_id(driverAndroid, "btn_reset_pass", sleep=True, scrn=True)
        with allure.step("Step #4 Выбираем сброс пароля по email-у"):
            click_by_xpath(driverAndroid, "btn_reset_pass_email", sleep=True, scrn=True)
        with allure.step("Step #5 Подтверждаем выбор сброса пароля по email-у"):
            confirm_allert(driverAndroid, sleep=True, scrn=True)
        with allure.step("Step #6 Вводим неверный код сброса пароля"):
            send_keys_by_xpath(driverAndroid, "cnt_code_reset_pass", "123456", sleep=True, scrn=True)
        with allure.step("Step #7 Нажимаем далее для сброса пароля"):
            click_by_id(driverAndroid, "btn_reset_pswrd_next", sleep=True, scrn=True)


    # !!!Для этого кейса нужно сбрасывать счетчик блокировки ввода смс кода
    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка отображения ошибки при неверном вводе кода сброса пароля с смс")
    @allure.description("Проверка отображения ошибки при неверном вводе кода сброса пароля с смс")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip(reason="Требуются особые условия")
    def test_auth_incorrect_reset_pass_via_sms(self, driverAndroid):
        with allure.step("Step #1 Вводим номер"):
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 243 851", scrn=True)
        with allure.step("Step #2 Нажимаем Войти"):
            click_by_id(driverAndroid, "btn_phone_number_next", sleep=True, scrn=True)
        with allure.step("Step #3 Нажимаем на сброс пароля"):
            click_by_id(driverAndroid, "btn_reset_pass", sleep=True, scrn=True)
        with allure.step("Step #4 Подтверждаем выбор сброса пароля по смс"):
            confirm_allert(driverAndroid, sleep=True, scrn=True)
        with allure.step("Step #5 Вводим неверный код сброса пароля"):
            send_keys_by_xpath(driverAndroid, "cnt_code_reset_pass", "123456", sleep=True, scrn=True)
        with allure.step("Step #6 Нажимаем далее для сброса пароля"):
            click_by_id(driverAndroid, "btn_reset_pswrd_next", sleep=True, scrn=True)
