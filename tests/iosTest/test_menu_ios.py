import allure

from appium.webdriver.common.touch_action import TouchAction
from confHelper.configHelperIOS.authIOS import Test_authorization
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import find_element_by_xpath, send_keys_by_xpath,\
    click_by_xpath, click_by_accessibility_id, send_keys_by_accessibility_id, find_element_by_accessibility_id

# Устройство для тестов на английском языке
# Абонент должен быть юзером НУРа не корпоративным, проверить личный профиль - поля ввода должны быть пустыми
@allure.epic("Epic #2 - Личный кабинет в приложении МойО!")
@allure.feature("Feature #1 - Раздел меню")
@allure.severity(allure.severity_level.BLOCKER)
class Test_menu(capsIOS):
    @allure.title("Проверка cохранения личного профиля положительный")
    @allure.description("Проверка успешного сохранения профиля после изменений")
    @allure.severity(allure.severity_level.NORMAL)
    def test_save_change_name(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 переход в редактирование личного профиля"):
            click_by_xpath(driver, "btn_personal_profile", scrn=True, sleep=True)
        with allure.step("Step 4 ввод данных"):
            send_keys_by_xpath(driver, "name_lk", "Win", scrn=True, sleep=True)
            send_keys_by_xpath(driver, "last_name_lk", "Test", scrn=True, sleep=True)
        with allure.step("Step 5 сохранение профиля"):
            click_by_xpath(driver, "done", scrn=True, sleep=True)
            click_by_accessibility_id(driver, "back_to_menu", sleep=True, scrn=True)

    # Убедиться что поле ввода почты не заполнено
    @allure.title("Проверка cохранения личного профиля положительный")
    @allure.description("Проверка успешного сохранения профиля после изменений в поле почты")
    @allure.severity(allure.severity_level.NORMAL)
    def test_save_change_email(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 переход в редактирование личного профиля"):
            click_by_xpath(driver, "btn_personal_profile", scrn=True, sleep=True)
        with allure.step("Step 4 ввод данных"):
            send_keys_by_xpath(driver, "field_email_lk", "eefimenko@nurtelecom.kg", scrn=True, sleep=True)
        with allure.step("Step 5 сохранение профиля"):
            click_by_xpath(driver, "done", scrn=True, sleep=True)
            click_by_accessibility_id(driver, "back_to_menu", sleep=True, scrn=True)

    @allure.title("Проверка открытия событий в меню")
    @allure.description("Проверка перехода во вкладку событий")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_events(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 открыть события"):
            click_by_accessibility_id(driver, "events", sleep=True, scrn=True)
        with allure.step("Step 4 вернуться на экран меню"):
            click_by_accessibility_id(driver, "back_to_menu", sleep=True, scrn=True)

    # У пользователя не должен быть подключенным сервис ОТВ
    @allure.title("Проверка открытия вкладки отв в меню")
    @allure.description("Проверка перехода во вкладку отв")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_otv(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 открыть вкладку отв"):
            click_by_accessibility_id(driver, "btn_otv", sleep=True, scrn=True)
        with allure.step("Step 4 вернуться на экран меню"):
            click_by_accessibility_id(driver, "back_to_menu", sleep=True, scrn=True)

    @allure.title("Проверка открытия онлайн поддержки")
    @allure.description("Проверка открытия онлайн поддержки")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_online_support(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 открыть боттом лист онлайн поддержки"):
            click_by_accessibility_id(driver, "btn_online_support", sleep=True, scrn=True)
        with allure.step("Step 4 закрыть боттом лист онлайн поддержки"):
            click_by_accessibility_id(driver, "btn_close_online_support", sleep=True, scrn=True)

    @allure.title("Проверка открытия вкладки карта офисов и терминалов в меню")
    @allure.description("Проверка перехода во вкладку карты офисов и терминалов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_map_from_menu(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 открыть карту офисов и терминалов"):
            click_by_accessibility_id(driver, "btn_map_menu", sleep=True, scrn=True)
        with allure.step("Step 4 выдать доступ к геолокации в карте"):
            click_by_accessibility_id(driver, "perm_offices", sleep=True, scrn=True)
        with allure.step("Step 5 вернуться на экран меню"):
            click_by_accessibility_id(driver, "back_to_menu", sleep=True, scrn=True)

    @allure.title("Проверка открытия вкладки Остор")
    @allure.description("Проверка перехода во вкладку магазина Остор")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_ostore(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 открыть магазин остор"):
            click_by_accessibility_id(driver, "btn_ostore", sleep=True, scrn=True)
        with allure.step("Step 4 вернуться на экран меню"):
            click_by_accessibility_id(driver, "back_to_menu", sleep=True, scrn=True)

    # Проверка работы боттом листа и отображения диалога на языке смены
    # Язык может быть сменен после выгрузки приложения и открытия снова но при смене языка последущие автотесты не будут
    # воспроизводиться потому проверяется кликабельность и диалоги
    @allure.title("Проверка отображения диалога на выбранном для смены в приложении языка")
    @allure.description("Проверка открытия боттом листа смены языка и отоборажения диалога на выбранном языке")
    @allure.severity(allure.severity_level.NORMAL)
    def test_lang_dialog(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 нажать на кнопку сменить язык"):
            click_by_accessibility_id(driver, "btn_change_lang_menu", sleep=True, scrn=True)
        with allure.step("Step 4 в боттом листе нажать на кыргызский язык"):
            click_by_xpath(driver, "lang_kg", sleep=True, scrn=True)
        with allure.step("Step 5 в диалоге нажать на кнопку ок"):
            click_by_xpath(driver, "btn_ok_lang_kg_menu", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на кнопку сменить язык"):
            click_by_accessibility_id(driver, "btn_change_lang_menu", sleep=True, scrn=True)
        with allure.step("Step 7 в боттом листе нажать на русский язык"):
            click_by_xpath(driver, "lang_ru", sleep=True, scrn=True)
        with allure.step("Step 8 в диалоге нажать на кнопку ок"):
            click_by_xpath(driver, "btn_ok_lang_ru_menu", sleep=True, scrn=True)
        with allure.step("Step 9 нажать на кнопку сменить язык"):
            click_by_accessibility_id(driver, "btn_change_lang_menu", sleep=True, scrn=True)
        with allure.step("Step 10 в боттом листе нажать на английский язык"):
            click_by_xpath(driver, "lang_en", sleep=True, scrn=True)
        with allure.step("Step 11 в диалоге нажать на кнопку ок"):
            click_by_xpath(driver, "btn_ok_lang_en_menu", sleep=True, scrn=True)


    @allure.title("Проверка открытия вкладки безопасность")
    @allure.description("Проверка перехода во вкладку безопасность")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_ostore(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 открыть экран безопасность"):
            click_by_accessibility_id(driver, "btn_security", sleep=True, scrn=True)
        with allure.step("Step 4 вернуться на экран меню"):
            click_by_accessibility_id(driver, "back_to_menu", sleep=True, scrn=True)

    @allure.title("Проверка открытия экрана описания о приложении")
    @allure.description("Проверка перехода во вкладку о приложении")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_about_app(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 открыть экран о приложении"):
            click_by_accessibility_id(driver, "btn_about_application", sleep=True, scrn=True)
        with allure.step("Step 4 вернуться на экран меню"):
            click_by_accessibility_id(driver, "back_to_menu", sleep=True, scrn=True)

    @allure.title("Проверка отключения отображения раздела Мектеп в боттом меню")
    @allure.description("Проверка работы ползунка в ячейке Мектеп")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_close_mektep_in_menu(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 отключить ползунок в ячейке Мектеп в меню пропадет раздел"):
            TouchAction(driver).press(x=222, y=329).move_to(x=273, y=308).release().perform()
            click_by_accessibility_id(driver, "btn_mektep", sleep=True, scrn=True)

    @allure.title("Проверка кнопки поделиться")
    @allure.description("Проверка появления системного боттом листа при нажатии на кнопку поделиться")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_share_myo(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 нажать на кнопку поделиться"):
            click_by_xpath(driver, "share_myo_in_menu", sleep=True, scrn=True)
        with allure.step("Step 4 скрыть боттом лист кнопки поделиться системным свайпом"):
            TouchAction(driver).press(x=222, y=329).move_to(x=191, y=622).release().perform()

    @allure.title("Проверка выхода из профиля")
    @allure.description("Проверка открытия экрана авторизации после нажатия на кнопку выход")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_exit(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 нажать на кнопку выход"):
            TouchAction(driver).press(x=222, y=329).move_to(x=273, y=308).release().perform()
            click_by_accessibility_id(driver, "btn_exit", sleep=True, scrn=True)





