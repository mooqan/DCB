from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import *
from confHelper.configHelperAndroid.authAndroid import Test_authorization


@allure.epic("Epic #1 - Модуль Личного кабинета О!")
@allure.feature("Feature #2 - Раздел меню")
class Test_menu(capsAnroid):
    @allure.story("Story #1 - Профиль ЛК")
    @allure.title("Проверка сохранения профиля")
    @allure.description("Проверка работоспособности сохраниения профиля ЛК")
    @allure.severity(allure.severity_level.NORMAL)
    def test_lk_save_profile(self, driverAndroid):
        with allure.step("Step 0 Блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 проверка перехода в меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step #2 Проверка перехода в окно  'Профиля'"):
            click_by_id(driverAndroid, "btn_edit_profile", scrn=True, sleep=True)
        with allure.step("Step #3 Проверка заполнения почты в окне 'Профиля'"):
            send_keys_by_xpath(driverAndroid, "cnt_email", "vstatsenko@nurtelecom.kg", scrn=True, sleep=True)
        with allure.step("Step #4 Проверка заполнения имени в окне 'Профиля'"):
            send_keys_by_xpath(driverAndroid, "cnt_name", "Vlad 1#$%&", scrn=True, sleep=True)
        with allure.step("Step #5 Проверка заполнения фамилии в окне 'Профиля'"):
            send_keys_by_xpath(driverAndroid, "cnt_last_name1", "12365$E)", scrn=True, sleep=True)
        with allure.step("Step #6 Проверка нажатия кнопки сохранения"):
            click_by_id(driverAndroid, "btn_profile_save", scrn=True, sleep=True)

    @allure.story("Story #2 - Раздел события")
    @allure.title("Проверка перехода на экран события")
    @allure.description("Проверка работоспособности перехода на экран события")
    @allure.severity(allure.severity_level.NORMAL)
    def test_events(self, driverAndroid):
        with allure.step("Step #0 Блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Проверка перехода в меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step #2 Нажимаем на раздел события"):
            click_by_xpath(driverAndroid, "btn_events", sleep=True, scrn=True)

    @allure.story("Story #4 - Тех поддерхка")
    @allure.title("Тест перехода в раздел онлан поддержка")
    @allure.description("Проверка работоспособности перехода в раздел онлан поддержка")
    @allure.severity(allure.severity_level.NORMAL)
    def test_otv(self, driverAndroid):
        with allure.step("Step #0 Блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Проверка перехода в меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step #2 Проверка перехода в О!Тv"):
            click_by_xpath(driverAndroid, "btn_suppot", scrn=True, sleep=True)
        with allure.step("Step #3 Проверка перехода в онт=лайн поддержку"):
            click_by_id(driverAndroid, "btn_online_support", scrn=True, sleep=True)

    @allure.story("Story #2 - Смена языка")
    @allure.title("Тест смены языка")
    @allure.description("Проверка работоспособности смены языка профиля ЛК")
    @allure.severity(allure.severity_level.NORMAL)
    def test_lk_change_lang(self, driverAndroid):
        with allure.step("Step #0 Блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Проверка перехода в меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step #2 Проверка перехода в окно смена языка"):
            click_by_id(driverAndroid, "btn_menu_change_lang", scrn=True, sleep=True)
        with allure.step("Step #3 Проверка выбора Кыргызского языка"):
            click_by_xpath(driverAndroid, "btn_ky_language", sleep=True, scrn=True)
        with allure.step("Step #4 Подтверждение смены языка"):
            c = driverAndroid.find_element_by_id("android:id/button1")
            c.click()
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #5 Проверка смены языка на экране ЛК"):
            click_by_id(driverAndroid, "btn_LK", sleep=True, scrn=True)
        with allure.step("Step #6 Проверка смены языка на экране Оденег"):
            click_by_id(driverAndroid, "btn_dengi", sleep=True, scrn=True)
        with allure.step("Step #7 Проверка перехода в окно смена языка"):
            click_by_id(driverAndroid, "btn_menu")
            click_by_id(driverAndroid, "btn_menu_change_lang", scrn=True, sleep=True)
        with allure.step("Step #8 Проверка выбора Английского языка"):
            click_by_xpath(driverAndroid, "btn_en_language", sleep=True, scrn=True)
        with allure.step("Step #9 Подтверждение смены языка"):
            c.click()
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step #10 Проверка смены языка на экране ЛК"):
            click_by_id(driverAndroid, "btn_LK", sleep=True, scrn=True)
        with allure.step("Step #11 Проверка смены языка на экране Оденег"):
            click_by_id(driverAndroid, "btn_dengi", sleep=True, scrn=True)

    @allure.story("Story #2 - офисы и терминалы")
    @allure.title("Тест Офисы и терминалы")
    @allure.description("Проверка работоспособности отображения офисов и перехода в окне 'Офисы и терминалы'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_office_and_terminals(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в боковое меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно 'Офисы и терминалы'"):
            click_by_id(driverAndroid, "btn_menu_office_map", scrn=True, sleep=True)
        with allure.step("Step 3 проверка перехода в список офисов"):
            click_by_id(driverAndroid, "btn_office_list", scrn=True, sleep=True)
        with allure.step("Step 4 проверка перехода в первый офис в списке"):
            click_by_xpath(driverAndroid, "btn_first_office", scrn=True, sleep=True)
            back(driverAndroid)
        with allure.step("Step 5 проверка переъода в список терминалов"):
            click_by_xpath(driverAndroid, "btn_page_terminals", scrn=True, sleep=True)
        with allure.step("Step 6 проверка перехода в первый терминал в списке"):
            click_by_xpath(driverAndroid, "btn_first_terminal", scrn=True, sleep=True)

    @allure.story("Story #3 - O!Store")
    @allure.title("Тест открытия O!Store на языке приложения")
    @allure.description("Проверка работоспособности смены языка на экране O!Store")
    @allure.severity(allure.severity_level.NORMAL)
    def test_o_store(self, driverAndroid):
        with allure.step("Step 1 Блок авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step 2 Переход в боковое меню"):
            click_by_id(driverAndroid, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 Проверка перехода в O!Store на Ру локализации"):
            click_by_xpath(driverAndroid, "btn_o_store", sleep=True, scrn=True)
            back(driverAndroid)
        with allure.step("Step #4 Проверка перехода в окно смена языка"):
            click_by_id(driverAndroid, "btn_menu_change_lang", scrn=True, sleep=True)
        with allure.step("Step #5 Проверка выбора Кыргызского языка"):
            click_by_xpath(driverAndroid, "btn_ky_language", sleep=True, scrn=True)
            confirm_allert(driverAndroid)
        with allure.step("Step #6 Проверка перехода в O!Store на Кр локализации"):
            click_by_xpath(driverAndroid, "btn_o_store", sleep=True, scrn=True)
            back(driverAndroid)
        with allure.step("Step #7 Проверка перехода в окно смена языка"):
            click_by_id(driverAndroid, "btn_menu_change_lang", scrn=True, sleep=True)
        with allure.step("Step #8 Проверка выбора Английского языка"):
            click_by_xpath(driverAndroid, "btn_en_language", sleep=True, scrn=True)
            confirm_allert(driverAndroid)
        with allure.step("Step #9 Проверка перехода в O!Store на En локализации"):
            click_by_xpath(driverAndroid, "btn_o_store", sleep=True, scrn=True)