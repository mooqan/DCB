import allure
from appium.webdriver.common.touch_action import TouchAction

from confHelper.configHelperIOS.authIOS import Test_authorization
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import click_by_xpath, click_by_accessibility_id, send_keys_by_accessibility_id, send_keys_by_xpath, find_element_by_accessibility_id

@allure.epic("Epic #3 - Модуль О!денег в приложении Мой О!")
@allure.feature("Feature #2 - функционал счетов и штрафов")
@allure.severity(allure.severity_level.BLOCKER)
class Test_bills_and_fines(capsIOS):
    @allure.title("Проверка открытия экрана счета и штрафы")
    @allure.description("Проверка перехода на экран счета и штрафы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_bills_and_fines(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)

    @allure.title("Проверка успешного добавления авто")
    @allure.description("Проверка отображения добавленного авто")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_avto(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на кнопку добавить"):
            click_by_xpath(driver, "btn_add_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на ячейку авто"):
            click_by_accessibility_id(driver, "btn_auto", sleep=True, scrn=True)
        with allure.step("Step 6 ввести госномер"):
            click_by_xpath(driver, "field_license_plate")
            send_keys_by_xpath(driver, "field_license_plate", "01KG702AAX", sleep=True, scrn=True)
        with allure.step("Step 7 ввести инн"):
            click_by_xpath(driver, "field_tin_auto")
            send_keys_by_xpath(driver, "field_tin_auto", "22411199201201", sleep=True, scrn=True)
        with allure.step("Step 8 ввести название авто"):
            click_by_xpath(driver, "field_create_name_auto")
            send_keys_by_xpath(driver, "field_create_name_auto", "Test", sleep=True, scrn=True)
        with allure.step("Step 9 нажать на кнопку сохранить авто"):
            click_by_accessibility_id(driver, "btn_save", sleep=True, scrn=True)

    @allure.title("Проверка успешного добавления счета газпрома")
    @allure.description("Проверка отображения добавленного счета газпрома")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_gazprom(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "btn_little_add", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на ячейку газпрома"):
            click_by_accessibility_id(driver, "btn_gazprom", sleep=True, scrn=True)
        with allure.step("Step 6 ввести лицевой счет в поле газпром"):
            click_by_xpath(driver, "field_receipt_gazprom")
            send_keys_by_xpath(driver, "field_receipt_gazprom", "030606302", sleep=True, scrn=True)
        with allure.step("Step 7 ввести фамилию в поле фамилия"):
            click_by_xpath(driver, "field_surname_gazprom", sleep=True, scrn=True)
            send_keys_by_xpath(driver, "field_surname_gazprom", "Ефименко", sleep=True, scrn=True)
        with allure.step("Step 8 ввести название счета"):
            click_by_xpath(driver, "field_name_gazprom", sleep=True, scrn=True)
            send_keys_by_xpath(driver, "field_name_gazprom", "test", sleep=True, scrn=True)
        with allure.step("Step 9 нажать кнопку сохранить"):
            click_by_accessibility_id(driver, "btn_save", sleep=True, scrn=True)

    @allure.title("Проверка добавления невалидного авто")
    @allure.description("Проверка отображения ошибки при невалидном инн")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_invalid_inn_avto(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на кнопку добавить"):
            click_by_xpath(driver, "btn_add_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на ячейку авто"):
            click_by_accessibility_id(driver, "btn_auto", sleep=True, scrn=True)
        with allure.step("Step 6 ввести госномер"):
            click_by_xpath(driver, "field_license_plate")
            send_keys_by_xpath(driver, "field_license_plate", "03KG631AAL", sleep=True, scrn=True)
        with allure.step("Step 7 ввести инн"):
            click_by_xpath(driver, "field_tin_auto")
            send_keys_by_xpath(driver, "field_tin_auto", "32411199201201", sleep=True, scrn=True)
        with allure.step("Step 8 ввести название авто"):
            click_by_xpath(driver, "field_create_name_auto")
            send_keys_by_xpath(driver, "field_create_name_auto", "Test", sleep=True, scrn=True)
        with allure.step("Step 9 нажать на кнопку сохранить авто"):
            click_by_accessibility_id(driver, "btn_save", sleep=True, scrn=True)

    @allure.title("Проверка добавления невалидного счета газпрома")
    @allure.description("Проверка отображения ошибки навалидного счета газпрома по имени")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_invalid_name_gazprom(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "btn_little_add", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на ячейку газпрома"):
            click_by_accessibility_id(driver, "btn_gazprom", sleep=True, scrn=True)
        with allure.step("Step 6 ввести лицевой счет в поле газпром"):
            click_by_xpath(driver, "field_receipt_gazprom")
            send_keys_by_xpath(driver, "field_receipt_gazprom", "030606302", sleep=True, scrn=True)
        with allure.step("Step 7 ввести фамилию в поле фамилия"):
            click_by_xpath(driver, "field_surname_gazprom", sleep=True, scrn=True)
            send_keys_by_xpath(driver, "field_surname_gazprom", "test", sleep=True, scrn=True)
        with allure.step("Step 8 ввести название счета"):
            click_by_xpath(driver, "field_name_gazprom", sleep=True, scrn=True)
            send_keys_by_xpath(driver, "field_name_gazprom", "test", sleep=True, scrn=True)
        with allure.step("Step 9 нажать кнопку сохранить"):
            click_by_accessibility_id(driver, "btn_save", sleep=True, scrn=True)
        with allure.step("Step 10 нажать на ок в алерте"):
            click_by_accessibility_id(driver, "btn_ok_accept_alert", sleep=True, scrn=True)
        with allure.step("Step 11 нажать кнопку закрыть на экране добавления счета"):
            click_by_accessibility_id(driver, "btn_close", sleep=True, scrn=True)

    @allure.title("Проверка редактирования названия добавленного авто")
    @allure.description("Проверка применения изменений в редактировании авто")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_changing_auto(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 открыть детали авто по клику на ячейку авто"):
            click_by_xpath(driver, "btn_auto_second_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на кнопку редактирования данного авто"):
            click_by_xpath(driver, "btn_auto_second_cell_editing", sleep=True, scrn=True)
        with allure.step("Step 6 изменить название авто"):
            click_by_xpath(driver, "field_editing_name_auto")
            send_keys_by_xpath(driver, "field_editing_name_auto", "MoiO", sleep=True, scrn=True)
        with allure.step("Step 7 нажать на кнопку сохранить для применения редактирования"):
            click_by_accessibility_id(driver, "btn_save", sleep=True, scrn=True)

    @allure.title("Проверка редактирования названия добавленного счета газпрома")
    @allure.description("Проверка применения изменений в редактировании счета газпрома")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_changing_gazprom_name(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на ячейку счета газпрома"):
            click_by_xpath(driver, "btn_gazprom_first_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на кнопку редактирования на экране деталей счета"):
            click_by_xpath(driver, "btn_gazprom_first_cell_editing", sleep=True, scrn=True)
        with allure.step("Step 6 изменить название счета газпрома"):
            click_by_xpath(driver, "field_editing_gazprom_cell")
            send_keys_by_xpath(driver, "field_editing_gazprom_cell", "MoiO", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку сохранить после редактирования"):
            click_by_accessibility_id(driver, "btn_save", sleep=True, scrn=True)

    @allure.title("Проверка отображения деталей неоплаченного штрафов")
    @allure.description("Проверка перехода на экране детали штрафа в авто")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_auto_fines(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 открыть детали авто по клику на ячейку авто"):
            click_by_xpath(driver, "btn_auto_second_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на первую ячейку штрафа"):
            click_by_xpath(driver, "btn_first_cell_fines", sleep=True, scrn=True)

    @allure.title("Проверка перехода на экран оплаты штрафа по авто")
    @allure.description("Проверка открытия экрана оплаты штрафа, отображение суммы нередактируемой и без подсазок сумм")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auto_fines_payment(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 открыть детали авто по клику на ячейку авто"):
            click_by_xpath(driver, "btn_auto_second_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на первую ячейку штрафа"):
            click_by_xpath(driver, "btn_first_cell_fines", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на кнопку оплатить на экране деталей штрафа"):
            click_by_xpath(driver, "btn_pay_auto_fine", sleep=True, scrn=True)

    @allure.title("Проверка перехода на экран оплаты штрафа по авто")
    @allure.description("Проверка открытия экрана оплаты штрафа, отображение суммы нередактируемой и без подсазок сумм")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_gazprom_payment(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на ячейку счета газпрома"):
            click_by_xpath(driver, "btn_gazprom_first_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на кнопку погасить на экране газпрома"):
            click_by_xpath(driver, "btn_to_repay_gazprom", sleep=True, scrn=True)

    @allure.title("Проверка отмены удаления счета авто в тосте")
    @allure.description("Проверка отмены удаления через редактирование счета авто по кнопке отмена в тосте")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auto_cancel_deleting(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на кнопку редактирования на главном экране счетов и штрафов"):
            click_by_xpath(driver, "btn_edit_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на красную иконку удаления"):
            click_by_accessibility_id(driver, "btn_red_icon_delete", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на кнопку удалить в сдвинутой ячейке счета"):
            click_by_xpath(driver, "btn_delete_auto_cell", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку отмена в появившемся тосте об удалении"):
            click_by_xpath(driver, "btn_cancel_deleting_toast", sleep=True, scrn=True)
        with allure.step("Step 8 нажать на кнопку сохранить для применения редактирования"):
            click_by_accessibility_id(driver, "btn_save", sleep=True, scrn=True)

    @allure.title("Проверка удаления счета авто")
    @allure.description("Проверка удаления счета авто из редактирования")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auto_delete_from_editing(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 открыть детали авто по клику на ячейку авто"):
            click_by_xpath(driver, "btn_auto_second_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на кнопку редактирования данного авто"):
            click_by_xpath(driver, "btn_auto_second_cell_editing", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на кнопку удалить из редактрования авто"):
            click_by_xpath(driver, "btn_delete_from_editing", sleep=True, scrn=True)

    @allure.title("Проверка удаления счета газпрома из редактирования")
    @allure.description("Проверка удаления счета газпрома из редактрования счета")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_gazprom_from_editing(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на ячейку счета газпрома"):
            click_by_xpath(driver, "btn_gazprom_first_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на кнопку редактирования на экране деталей счета"):
            click_by_xpath(driver, "btn_gazprom_first_cell_editing", sleep=True, scrn=True)
        with allure.step("Step 6 нажать кнопку удалить на экране редактирования счета"):
            click_by_xpath(driver, "btn_delete_from_editing", sleep=True, scrn=True)

    # В зависимости от даты прогона автотеста ответ при нажатии на кнопку передать показания будет разным
    # Если время передачи показаний валидно - откроется боттом лист для передачи
    # Если время показаний не наступило, появится алерт с уведомлением о валидных датах
    @allure.title("Проверка кликабельности кнопки передать показания через счет газпрома")
    @allure.description("Проверка кликабельности кнопки передать показания через счет газпрома")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_gazprom_from_editing(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на ячейку счета газпрома"):
            click_by_xpath(driver, "btn_gazprom_first_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на плоскую кнопку передать показания"):
            click_by_xpath(driver, "btn_gazprom_submit_readings", sleep=True, scrn=True)

    @allure.title("Проверка добавления уже существующего счета газпрома")
    @allure.description("Проверка отображения ошибки при добавлении уже существуюшего счета газпрома")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_identical_gazprom(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "btn_little_add", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на ячейку газпрома"):
            click_by_accessibility_id(driver, "btn_gazprom", sleep=True, scrn=True)
        with allure.step("Step 6 ввести лицевой счет в поле газпром"):
            click_by_xpath(driver, "field_receipt_gazprom")
            send_keys_by_xpath(driver, "field_receipt_gazprom", "030606302", sleep=True, scrn=True)
        with allure.step("Step 7 ввести фамилию в поле фамилия"):
            click_by_xpath(driver, "field_surname_gazprom", sleep=True, scrn=True)
            send_keys_by_xpath(driver, "field_surname_gazprom", "Ефименко", sleep=True, scrn=True)
        with allure.step("Step 8 ввести название счета"):
            click_by_xpath(driver, "field_name_gazprom", sleep=True, scrn=True)
            send_keys_by_xpath(driver, "field_name_gazprom", "test", sleep=True, scrn=True)
        with allure.step("Step 9 нажать кнопку сохранить"):
            click_by_accessibility_id(driver, "btn_save", sleep=True, scrn=True)
        with allure.step("Step 10 нажать на ок в алерте"):
            click_by_accessibility_id(driver, "btn_ok_accept_alert", sleep=True, scrn=True)

    @allure.title("Проверка открытия фотографии в штрафе авто")
    @allure.description("Проверка открытия фотографии в штрафе авто")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_auto_fine_photo(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)
        with allure.step("Step 4 открыть детали авто по клику на ячейку авто"):
            click_by_xpath(driver, "btn_auto_second_cell", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на первую ячейку штрафа"):
            click_by_xpath(driver, "btn_first_cell_fines", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на ячейку фото"):
            click_by_accessibility_id(driver, "btn_auto_photo", sleep=True, scrn=True)
        with allure.step("Step 7 выйти из экрана просмотра фото"):
            click_by_accessibility_id(driver, "btn_cancel_auto_photo", sleep=True, scrn=True)





