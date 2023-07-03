import allure
from appium.webdriver.common.touch_action import TouchAction

from confHelper.configHelperIOS.authIOS import Test_authorization, elements
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import click_by_xpath, click_by_accessibility_id, send_keys_by_accessibility_id, send_keys_by_xpath, find_element_by_accessibility_id

# Устройство для тестов на английском языке
# Абонент должен быть юзером НУРа не корпоративным
# Не иметь добавленных субномеров, номер должен быть дочерним (иметь родительскую группу)
# У субномера 0702242356 должен быть тариф пакетный, иметь баланс, после получения запроса - добавиться субномером
# У главного номера для автотестов имеется баланс
@allure.epic("Epic #2 - Модуль Личного кабинета в приложении Мой О!")
@allure.feature("Feature #2 - функционал мои номера")
@allure.severity(allure.severity_level.BLOCKER)
class Test_my_number(capsIOS):
    @allure.title("Проверка открытия открытия экрана Мои номера")
    @allure.description("Проверка перехода на пустой экран мои номера")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_my_numbers(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на кнопку назад с экрана моих номеров"):
            click_by_xpath(driver, "btn_back_to_lk", sleep=True, scrn=True)

    @allure.title("Проверка открытия открытия экрана моя группа")
    @allure.description("Проверка перехода экран родительской группы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_my_group(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на ячейку моя группа"):
            click_by_xpath(driver, "btn_subnumber_group", sleep=True, scrn=True)
        with allure.step("Step 4 вернуться на главный экран мои номера "):
            click_by_xpath(driver, "btn_back_to_my_numbers", sleep=True, scrn=True)

    # Родительский номер 996702242356
    # Убедиться что родитель именно данный номер или изменить в remove_subnumber_from_group номер
    @allure.title("Проверка выхода из родительской группы")
    @allure.description("Проверка удаления родителя и отсуствия впоследствии удаления ячейки моя группа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_from_my_group(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на ячейку моя группа"):
            click_by_xpath(driver, "btn_subnumber_group", sleep=True, scrn=True)
        with allure.step("Step 4 удалить родительский номер"):
            click_by_accessibility_id(driver, "remove_subnumber_from_group", sleep=True, scrn=True)
            click_by_xpath(driver, "delete_parent_number", sleep=True, scrn=True)
            click_by_accessibility_id(driver, "btn_ok_accept_deleting_number", sleep=True, scrn=True)

    # После отправки запроса на добавления подтвердить через смс на субномере добавление!
    @allure.title("Проверка успешного добавления субномера")
    @allure.description("Проверка флоу добавления субномера в мои номера с указанием имени")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_new_subnumber(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на кнопку добавления номера"):
            click_by_xpath(driver, "add_the_number", sleep=True, scrn=True)
        with allure.step("Step 4 ввести номер субномера"):
            send_keys_by_xpath(driver, "field_subnumber_phone", "702242356", sleep=True, scrn=True)
        with allure.step("Step 5 ввести имя субномера"):
            click_by_xpath(driver, "field_create_subnumber_name", sleep=True, scrn=True)
            name_input = driver.find_element_by_xpath(elements.get("field_create_subnumber_name"))
            name_input.clear()
            name_input.send_keys("Test")
        with allure.step("Step 6 нажать кнопку далее"):
            click_by_xpath(driver, "Further2", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку понятно в уведомлении о добавлении"):
            click_by_accessibility_id(driver, "btn_ok_adding_subnumber", sleep=True, scrn=True)

    @allure.title("Проверка успешного добавления умного устройства в субномера")
    @allure.description("Проверка флоу добавления умного устройства в субномера без указания имени")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_smart_subnumber(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на кнопку добавления номера"):
            click_by_xpath(driver, "add_the_number", sleep=True, scrn=True)
        with allure.step("Step 4 ввести номер субномера"):
            send_keys_by_xpath(driver, "field_subnumber_phone", "702245281", sleep=True, scrn=True)
        with allure.step("Step 6 нажать кнопку далее"):
            click_by_xpath(driver, "Further2", sleep=True, scrn=True)
        with allure.step("Step 7 ввести пин 2 для подтверждения добавления субномера"):
            send_keys_by_xpath(driver, "field_pin2", "4297", sleep=False, scrn=True)
        with allure.step("Step 8 нажать кнопку продолжить на экране ввода пина 2"):
            click_by_xpath(driver, "confirm_smart_number", sleep=True,scrn=True)

    @allure.title("Проверка удаления субномера из редактирования")
    @allure.description("Проверка успешного удаленич субномера с экрана редактирования субномера")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_subnumber(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на субномер"):
            click_by_xpath(driver, "click_subnumber", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на кнопку редактирования субномера"):
            click_by_xpath(driver, "changing_subnumber", sleep=True, scrn=True)
        with allure. step("Step 5 нажать кнопку удалить из моих субномеров"):
            click_by_xpath(driver, "delete_from_my_subnumbers", sleep=True, scrn=True)
        with allure.step("Step 6 подтвердить удаление"):
            click_by_accessibility_id(driver, "accept_deleting_subnumber", sleep=True, scrn=True)

    @allure.title("Проверка сброса внесенных изменений в редактировании")
    @allure.description("Проверка сброса редактирования по кнопке закрыть")
    @allure.severity(allure.severity_level.MINOR)
    def test_subnumber_reset_changes(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на субномер"):
            click_by_xpath(driver, "click_another_subnumber", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на кнопку редактирования субномера"):
            click_by_xpath(driver, "changing_subnumber_2", sleep=True, scrn=True)
        with allure.step("Step 5 изменить имя субномера"):
            click_by_xpath(driver, "change_subnumber_name", sleep=True, scrn=True)
            name_input = driver.find_element_by_xpath(elements.get("change_subnumber_name"))
            name_input.clear()
            name_input.send_keys("Reset")
        with allure.step("Step 6 нажать по кнопке закрыть, на скрине проверить, что имя не изменено"):
            click_by_accessibility_id(driver, "btn_close_changing_name", sleep=True, scrn=True)

    @allure.title("Проверка редактирования имени субномера")
    @allure.description("Проверка редактирования имени субномера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_change_subnumber_name(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на субномер"):
            click_by_xpath(driver, "click_another_subnumber", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на кнопку редактирования субномера"):
            click_by_xpath(driver, "changing_subnumber_2", sleep=True, scrn=True)
        with allure.step("Step 5 изменить имя субномера"):
            send_keys_by_xpath(driver, "change_subnumber_name", "MoiO", sleep=True, scrn=True)
        with allure.step("Step 6 сохранить измнения по кнопке готово"):
            click_by_accessibility_id(driver, "btn_done", sleep=True, scrn=True)

    @allure.title("Проверка добавления своего номера в субномера")
    @allure.description("Проверка отображения ошибки при попытке добавить свой номер в субномера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_my_number(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "add_subnumber_little_btn", sleep=True, scrn=True)
        with allure.step("Step 4 ввести номер субномера"):
            send_keys_by_xpath(driver, "field_subnumber_phone", "702243852", sleep=True, scrn=True)
        with allure.step("Step 5 нажать кнопку далее для отправки запроса на добавление"):
            click_by_xpath(driver, "Further2", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку понятно в уведомлении об ошибке"):
            click_by_accessibility_id(driver, "btn_ok_adding_subnumber", sleep=True, scrn=True)

    @allure.title("Проверка добавления корпоративного номера в субномера")
    @allure.description("Проверка отображения ошибки при попытке добавить корпоративный номер в субномера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_corporate_number(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "add_subnumber_little_btn", sleep=True, scrn=True)
        with allure.step("Step 4 ввести номер субномера"):
            send_keys_by_xpath(driver, "field_subnumber_phone", "700000167", sleep=True, scrn=True)
        with allure.step("Step 5 нажать кнопку далее для отправки запроса на добавление"):
            click_by_xpath(driver, "Further2", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку понятно в уведомлении об ошибке"):
            click_by_accessibility_id(driver, "btn_ok_adding_subnumber", sleep=True, scrn=True)

    @allure.title("Проверка добавления абонента другого оператора в субномера")
    @allure.description("Проверка отображения ошибки при попытке добавить абонента другого оператора в субномера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_another_operator_to_subnumber(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "add_subnumber_little_btn", sleep=True, scrn=True)
        with allure.step("Step 4 ввести номер субномера"):
            send_keys_by_xpath(driver, "field_subnumber_phone", "551620122", sleep=True, scrn=True)
        with allure.step("Step 5 нажать кнопку далее для отправки запроса на добавление"):
            click_by_xpath(driver, "Further2", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку понятно в уведомлении об ошибке"):
            click_by_accessibility_id(driver, "btn_ok_adding_subnumber", sleep=True, scrn=True)

    @allure.title("Проверка добавления уже добавленного номера в субномера")
    @allure.description("Проверка отображения ошибки при попытке добавить уже существующего номера в субномера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_exist_subnumber(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "add_subnumber_little_btn", sleep=True, scrn=True)
        with allure.step("Step 4 ввести номер субномера"):
            send_keys_by_xpath(driver, "field_subnumber_phone", "702242356", sleep=True, scrn=True)
        with allure.step("Step 5 нажать кнопку далее для отправки запроса на добавление"):
            click_by_xpath(driver, "Further2", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку понятно в уведомлении об ошибке"):
            click_by_accessibility_id(driver, "btn_ok_adding_subnumber", sleep=True, scrn=True)

    @allure.title("Проверка неуспешного добавления mbb номера")
    @allure.description("Проверка отображения ошибки при вводе неверного пин2 при добавлении mbb номера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_mbb_subnumber_false_pin(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "add_subnumber_little_btn", sleep=True, scrn=True)
        with allure.step("Step 4 ввести номер субномера"):
            send_keys_by_xpath(driver, "field_subnumber_phone", "709758245", sleep=True, scrn=True)
        with allure.step("Step 5 нажать кнопку далее"):
            click_by_xpath(driver, "Further2", sleep=True, scrn=True)
        with allure.step("Step 6 ввести пин 2 для подтверждения добавления субномера"):
            send_keys_by_xpath(driver, "field_pin2", "1111", sleep=False, scrn=True)
        with allure.step("Step 7 нажать кнопку продолжить на экране ввода пина 2"):
            click_by_xpath(driver, "confirm_smart_number", sleep=True,scrn=True)
        with allure.step("Step 8 нажать кнопку закрыть в уведомлении об ошибке"):
            click_by_accessibility_id(driver, "btn_close_invalid_pin", sleep=True, scrn=True)

    @allure.title("Проверка включения получения уведомлений о низком балансе")
    @allure.description("Проверка включения получения уведомлений о низком балансе")
    @allure.severity(allure.severity_level.NORMAL)
    def test_on_subnumber_push(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на субномер"):
            click_by_xpath(driver, "click_another_subnumber", sleep=True, scrn=True)
        with allure.step("Step 4 сделать активным ползунок в ячейке получения уведомления о низком балансе"):
            click_by_xpath(driver, "btn_less_balance", sleep=True, scrn=True)

    @allure.title("Проверка отмены отправленного запроса на добавление субномераа")
    @allure.description("Проверка исчезновения ячейки субномера, которому отправили запрос на добавление")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancellation_subnumber_request(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на плоскую кнопку добавить"):
            click_by_xpath(driver, "add_subnumber_little_btn", sleep=True, scrn=True)
        with allure.step("Step 4 ввести номер субномера"):
            send_keys_by_xpath(driver, "field_subnumber_phone", "702244901", sleep=True, scrn=True)
        with allure.step("Step 5 нажать кнопку далее для отправки запроса на добавление"):
            click_by_xpath(driver, "Further2", sleep=True, scrn=True)
        with allure.step("Step 7 нажать кнопку понятно в уведомлении об ошибке"):
            click_by_accessibility_id(driver, "btn_ok_adding_subnumber", sleep=True, scrn=True)
        with allure.step("Step 8 нажать кнопку отмена в ячейке добавления субномера"):
            click_by_xpath(driver, "btn_cancel_subnumber_request", sleep=True, scrn=True)

    @allure.title("Проверка смены тарифа")
    @allure.description("Проверка смены тарифа субномеру")
    @allure.severity(allure.severity_level.NORMAL)
    def test_subnumber_change_tariff(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на субномер"):
            click_by_xpath(driver, "click_another_subnumber", sleep=True, scrn=True)
        with allure.step("Step 4 нажать по ячейке смена тарифа"):
            click_by_accessibility_id(driver, "btn_tariffs_subnumber", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на базовые тарифы в субномерах"):
            click_by_xpath(driver, "btn_basic_tariffs_subnumber", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на тариф оной на субномер"):
            TouchAction(driver).press(x=216, y=512).move_to(x=242, y=315).release().perform()
            click_by_xpath(driver, "btn_onoi_for_subnumber", sleep=True, scrn=True)
        with allure.step("Step 7 подключить тариф оной"):
            click_by_xpath(driver, "btn_change_tariffs_subnumber", sleep=True, scrn=True)
        with allure.step("Step 8 подтвердить подключение"):
            click_by_accessibility_id(driver, "btn_yes", sleep=True, scrn=True)

    @allure.title("Проверка подключения услуги субномера")
    @allure.description("Проверка усрешного подключения услуги субномера")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subnumber_connect_the_service(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на субномер"):
            click_by_xpath(driver, "click_another_subnumber", sleep=True, scrn=True)
        with allure.step("Step 4 нажать по ячейке услуги"):
            click_by_accessibility_id(driver, "btn_connected_services", sleep=True, scrn=True)
        with allure.step("Step 5 нажать по категории доступных услуг спорт"):
            click_by_xpath(driver, "btn_affordable_services_sport", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на кнопку подключить в ячейке доступной услуге спорта"):
            click_by_xpath(driver, "btn_connect_service_sport", sleep=True, scrn=True)
        with allure.step("Step 7 подтвердить подключение"):
            click_by_accessibility_id(driver, "btn_yes", sleep=True, scrn=True)

    @allure.title("Проверка отключения услуги субномера")
    @allure.description("Проверка успешного отключения услуги субномера")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subnumber_disable_the_service(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел мои номера"):
            click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на субномер"):
            click_by_xpath(driver, "click_another_subnumber", sleep=True, scrn=True)
        with allure.step("Step 4 нажать по ячейке услуги"):
            click_by_accessibility_id(driver, "btn_connected_services", sleep=True, scrn=True)
        with allure.step("Step 5 нажать по ячейке уже подключенных услуг"):
            click_by_xpath(driver, "btn_active_services_subnumber", sleep=True, scrn=True)
        with allure.step("Step 6 нажать на ячейку подключенной услуги"):
            click_by_xpath(driver, "btn_service_sport_detail", sleep=True, scrn=True)
        with allure.step("Step 7 нажать на кнопку отключения услуги"):
            click_by_xpath(driver, "btn_turn_of_service", sleep=True, scrn=True)
        with allure.step("Step 8 подтвердить удаление"):
            click_by_accessibility_id(driver, "btn_yes", sleep=True, scrn=True)



