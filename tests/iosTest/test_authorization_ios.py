import allure
import cnt as cnt

from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import *
from confHelper.configHelperIOS.standards import click_by_accessibility_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from elements.elementsIOS import *

@allure.epic("Epic #1 - Авторизация в приложении Мой О!")
@allure.feature("Feature #1 - Авторизация")
@allure.story("Story #1 - Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
# Устройство для тестов должно быть на английском языке
# При такой локализации приложение для тестов также установиться на английском
# Необходимо для поиска элементов на экране
# Убедиться что в телефоне установлена симкарта того номера который используется в тестах
# Обязательное условие иметь специальный пароль для данного номера
class Test_auth(capsIOS):
    @allure.title("Проверка авторизации через специальный пароль")
    @allure.description("Проверка авторизации пользователем НУРа, у которого установлен спец. пароль")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_valid_password(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 введение номера авторизации"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
            click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)
        with allure.step("Step 3 введение пароля авторизации"):
            send_keys_by_accessibility_id(driver, "phone_pass_cnt", "Qwerty65", sleep=False, scrn=True)
        with allure.step("Step 4 нажатие кнопки продолжить после введения пароля"):
            click_by_accessibility_id(driver, "pass_number_next", sleep=False, scrn=True)
            click_by_accessibility_id(driver, "cancel")
        with allure.step("Step 5 создание пинкода для авторизации"):
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
        with allure.step("Step 6 подтверждение пинкода для авторизации"):
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка ввода неверного специального пароля")
    @allure.description("Проверка отображения ошибки при неверном специальном пароле")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_password(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 введение номера авторизации"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
            click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)
        with allure.step("Step 3 введение неверное пароля авторизации"):
            send_keys_by_accessibility_id(driver, "phone_pass_cnt", "asdfgh76", sleep=False, scrn=True)
        with allure.step("Step 4 нажатие кнопки продолжить после введения неверного пароля"):
            click_by_accessibility_id(driver, "pass_number_next", sleep=True, scrn=True)

    # Для данной проверки убедиться что симкарта стоит в устройстве
    # Номер должен соответствовать вводимому номеру в тесте
    # У профиля должен быть установлен специальныцй пароль
    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка ввода неверного кода из сброса пароля по смс")
    @allure.description("Проверка отображения ошибки о неверном коде")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_sms_code(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 ввести номер для авторизации оператора НУРа"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
            click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)
        with allure.step("Step 3 нажатие на кнопку сбросить пароль"):
            click_by_accessibility_id(driver, "reset_the_password", sleep=True, scrn=True)
        with allure.step("Step 4 нажатие на кнопку смс"):
            click_by_xpath(driver, "reset_by_sms", scrn=True)
            time.sleep(15)
        with allure.step("Step 5 ввод неверного кода вручную"):
            send_keys_by_accessibility_id(driver, "otp_field", "123456", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка отображения экрана условий предоставления сервиса")
    @allure.description("Проверка перехода на экран условий предоставления сервиса")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_terms(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 введение номера авторизации"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=True, scrn=True)
        with allure.step("Step 2 нажатие по ссылке условий предоставления сервиса"):
            click_by_accessibility_id(driver, "link_agreements", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка открытия экрана оферт без согласия с условиями оферт")
    @allure.description("Проверка невозможности открытия экрана ввода пароля без согласия с условиями оферт")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_nonactive_checkbox(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 введение номера авторизации"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие по ссылке условий предоставления сервиса"):
            click_by_accessibility_id(driver, "link_agreements", sleep=False, scrn=True)
        with allure.step("Step 3 чекбокс неактивен - пользовательское соглашение"):
            click_by_accessibility_id(driver, "user_agreement", sleep=False, scrn=True)
        with allure.step("Step 4 чекбокс неактивен - согласие на сбор информации"):
            click_by_accessibility_id(driver, "user_terms_collection", sleep=False, scrn=True)
        with allure.step("Step 5 чекбокс неактивен - 18 лет"):
            click_by_accessibility_id(driver, "age_qualification", sleep=False, scrn=True)
        with allure.step("Step 6 возврат на экран введенного номера авторизации"):
            click_by_xpath(driver, "back", sleep=True, scrn=True)
        with allure.step("Step 7 нажать на кнопку далее без согласия с условиями сервиса"):
            click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)


    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка работы чекбоксов на экране условий предоставления сервиса")
    @allure.description("Проверка переключения активности в чекбоксах на экране условий предоставления сервиса")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_active_checkbox(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 введение номера авторизации"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие по ссылке условий предоставления сервиса"):
            click_by_accessibility_id(driver, "link_agreements", sleep=False, scrn=True)
        with allure.step("Step 3 чекбокс неактивен - пользовательское соглашение"):
            click_by_accessibility_id(driver, "user_agreement", sleep=False, scrn=True)
        with allure.step("Step 4 чекбокс неактивен - согласие на сбор информации"):
            click_by_accessibility_id(driver, "user_terms_collection", sleep=False, scrn=True)
        with allure.step("Step 5 чекбокс неактивен - 18 лет"):
            click_by_accessibility_id(driver, "age_qualification", sleep=True, scrn=True)
        with allure.step("Step 6 чекбокс активен - пользовательское соглашение"):
            click_by_accessibility_id(driver, "user_agreement", sleep=False, scrn=True)
        with allure.step("Step 7 чекбокс активен - согласие на сбор информации"):
            click_by_accessibility_id(driver, "user_terms_collection", sleep=False, scrn=True)
        with allure.step("Step 8 чекбокс активен - 18 лет"):
            click_by_accessibility_id(driver, "age_qualification", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на кнопку далее на экране условий с неактивными чекбоксами"):
            click_by_accessibility_id(driver, "terms_further", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка открытия оферт")
    @allure.description("Проверка перехода по офертам условий предоставления сервиса")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_open_offers(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 введение номера авторизации"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие по ссылке условий предоставления сервиса"):
            click_by_accessibility_id(driver, "link_agreements", sleep=False, scrn=True)
        with allure.step("Step 3 нажать на ссылку пользовательского соглашения"):
            click_by_accessibility_id(driver, "user_agreement_offert", sleep=True, scrn=True)
        with allure.step("Step 4 нажать назад на оферте пользовательского соглашения"):
            click_by_xpath(driver, "back", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на оферту на соглаcие сбора информации"):
            click_by_accessibility_id(driver, "user_terms_collection_offer",sleep=True, scrn=True)
        with allure.step("Step 6 нажать назад на оферте пользовательского соглашения"):
            click_by_xpath(driver, "back", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка авторизации пользователем другого оператора")
    @allure.description("Проверка авторизации в приложение пользователем другого оператора со спец. паролем")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_other_user(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 введение номера авторизации"):
            send_keys_by_accessibility_id(driver, "number_field", "220596397", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
            click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)
        with allure.step("Step 3 введение пароля авторизации"):
            send_keys_by_accessibility_id(driver, "phone_pass_cnt", "Qwerty65", sleep=False, scrn=True)
        with allure.step("Step 4 нажатие кнопки продолжить после введения пароля"):
            click_by_accessibility_id(driver, "pass_number_next", sleep=False, scrn=True)
            click_by_accessibility_id(driver, "cancel")
        with allure.step("Step 5 создание пинкода для авторизации"):
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
        with allure.step("Step 6 подтверждение пинкода для авторизации"):
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1")
            click_by_accessibility_id(driver, "pin_1", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка успешной смены специального пароля через сброс старого специального пароля по смс")
    @allure.description("Проверка смены специального пароля на экранах авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_special_password(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 ввести номер для авторизации оператора НУРа"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
            click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)
        with allure.step("Step 3 нажатие на кнопку сбросить пароль"):
            click_by_accessibility_id(driver, "reset_the_password", sleep=True, scrn=True)
        with allure.step("Step 4 нажатие на кнопку смс"):
            click_by_xpath(driver, "reset_by_sms", scrn=True)
            time.sleep(15)
        with allure.step("Step 5 подстановка кода из клавиатуры"):
            click_by_xpath(driver, "sms_code", sleep=True, scrn=True)
        with allure.step("Step 6 ввод нового специального пароля на экране создания специального пароля"):
            send_keys_by_accessibility_id(driver, "password_field", "Qwerty65", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку далее после ввода специального пароля"):
            click_by_accessibility_id(driver, "further", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка перехода на список офисов")
    @allure.description("Проверка открытия карты офисов и списка всех офисов после введения неверного спец. пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_maps(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 введение номера авторизации"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
            click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)
        with allure.step("Step 3 введение неверного пароля для авторизации"):
            send_keys_by_accessibility_id(driver, "phone_pass_cnt", "asdfgh76", sleep=False, scrn=True)
        with allure.step("Step 4 нажатие кнопки продолжить после введения неверного пароля"):
            click_by_accessibility_id(driver, "pass_number_next", sleep=False, scrn=True)
        with allure.step("Step 5 нажать на ссылку карт офисов"):
            click_by_accessibility_id(driver, "map_of_services", sleep=True, scrn=True)
        with allure.step("Step 6 выдать доступ к использованию геолокации"):
            click_by_accessibility_id(driver, "perm_offices", sleep=True, scrn=True)
        with allure.step("Step 7 нажать на иконку списка офиссов и терминалов"):
            click_by_accessibility_id(driver, "icon_map", sleep=True, scrn=True)
        with allure.step("Step 8 нажать на ячейку офиса"):
            click_by_xpath(driver, "btn_office", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка изменения языка экарнов авторизации")
    @allure.description("Проверка изменения языка приложения на главном экране авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_lang(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 нажать на иконку смены языка на экране авторизации"):
            click_by_xpath(driver, "lang", sleep=True, scrn=True)
        with allure.step("Step 2 нажать на ячейку кыргызский язык"):
            click_by_xpath(driver, "lang_kg", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на иконку смены языка"):
            click_by_xpath(driver, "lang", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на ячейку английский язык"):
            click_by_xpath(driver, "lang_en", sleep=True, scrn=True )
        with allure.step("Step 5 нажать на иконку смены языка"):
            click_by_xpath(driver, "lang", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на ячейку русский язык"):
            click_by_xpath(driver, "lang_ru", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка открытия карты офисов")
    @allure.description("Проверка перехода на экран офисов с экрана ввода номера для авторизации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_maps_from_auth(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 нажать на иконку карты офисов"):
            click_by_accessibility_id(driver, "maps_login", sleep=True, scrn=True)
        with allure.step("Step 2 выдать доступ к определению местонахождения карте"):
            click_by_accessibility_id(driver, "perm_offices")
        with allure.step("Step 3 открыть список офисов по иконке"):
            click_by_accessibility_id(driver, "icon_map", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на ячейку офиса"):
            click_by_xpath(driver, "btn_office", sleep=True, scrn=True)

    @allure.story("Story #1 - Авторизация")
    @allure.title("Проверка создания слабого пароля при сбросе специального пароля")
    @allure.description("Проверка отображения ошибки о слабом созданном специальном пароле")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_weak_special_password(self, driver):
        with allure.step("Step 0 выдать разрешение на доступ"):
            click_by_xpath(driver, "accept_main_alert")
        with allure.step("Step 1 ввести номер для авторизации оператора НУРа"):
            send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
        with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
            click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)
        with allure.step("Step 3 нажатие на кнопку сбросить пароль"):
            click_by_accessibility_id(driver, "reset_the_password", sleep=True, scrn=True)
        with allure.step("Step 4 нажатие на кнопку смс"):
            click_by_xpath(driver, "reset_by_sms", scrn=True)
            time.sleep(15)
        with allure.step("Step 5 подстановка кода из клавиатуры"):
            click_by_xpath(driver, "sms_code", sleep=True, scrn=True)
        with allure.step("Step 6 открыть видимость клавиатуры"):
            click_by_accessibility_id(driver, "close_eye")
        with allure.step("Step 6 ввод слабого пароля на экране создания спец пароля"):
            send_keys_by_accessibility_id(driver, "password_field", "qwertyui", sleep=False, scrn=True)
        with allure.step("Step 7 нажать далее после ввода специального пароля"):
            click_by_accessibility_id(driver, "further", sleep=True, scrn=True)





























