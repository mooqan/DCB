import allure
from appium.webdriver.common.touch_action import TouchAction

from confHelper.configHelperIOS.authIOS import Test_authorization
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import click_by_xpath, click_by_accessibility_id, send_keys_by_accessibility_id, find_element_by_accessibility_id


@allure.epic("Epic #2 - Личный кабинет в приложении МойО!")
@allure.feature("Feature #1 - Детализация в приложении мойО!")
@allure.severity(allure.severity_level.CRITICAL)
# Устройство для тестов на английском языке
# У абонента должна быть история детализации за последние два месяца
class Test_detalization(capsIOS):
    @allure.title("Проверка детализации за сегодня")
    @allure.description("Проверка открытия вкладки детализации и отображения расходов за сегодня")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_today_detalization(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 открыть вкладку детализации"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 выбрать период детализации за последний месяц"):
            click_by_xpath(driver,"btn_calendar", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на период последний месяц в боттом листе"):
            click_by_accessibility_id(driver, "btn_last_month", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на первую вкладку расходов в списке детализации под пайчартом"):
            click_by_xpath(driver, "btn_abon_spend", sleep=True, scrn=True)
        with allure.step("Step 6 свернуть список расходов после открытия"):
            click_by_xpath(driver, "btn_abon_spend", sleep=True, scrn=True)

    @allure.title("Проверка отображения истории детализации")
    @allure.description("Проверка открытия истории детализации")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_history_detalization(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 открыть вкладку детализации"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 открыть вкладку историю детализации"):
            click_by_accessibility_id(driver, "btn_history_detalization", sleep=True, scrn=True)

    @allure.title("Проверка отображения только платных событий в истории детализации")
    @allure.description("Проверка работы выключения ползунка для отображения платных событий детализации")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_paid_events(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 открыть вкладку детализации"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 выбрать период детализации за последний месяц"):
            click_by_xpath(driver, "btn_calendar", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на период последний месяц в боттом листе"):
            click_by_accessibility_id(driver, "btn_last_month", sleep=True, scrn=True)
        with allure.step("Step 5 открыть вкладку историю детализации"):
            click_by_accessibility_id(driver, "btn_history_detalization", sleep=True, scrn=True)
        with allure.step("Step 6 отключить ползунок бесплатных событий"):
            click_by_xpath(driver, "btn_slider_detalization", sleep=True, scrn=True)

    @allure.title("Проверка отображения событий в истории за выбранный период")
    @allure.description("Проверка выбора период в истории детализации")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_paid_events(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 открыть вкладку детализации"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 открыть вкладку историю детализации"):
            click_by_accessibility_id(driver, "btn_history_detalization", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на иконку календаря"):
            click_by_xpath(driver, "btn_history_calendar", sleep=True, scrn=True)
        with allure.step("Step 5 выбрать период в календаре"):
            click_by_accessibility_id(driver, "btn_last_week", sleep=True, scrn=True)
        with allure.step("Step 6 выбрать период за сегодня"):
            click_by_xpath(driver, "btn_history_calendar", sleep=True, scrn=True)
        with allure.step("Step 7 выбрать период по дате"):
            click_by_accessibility_id(driver, "btn_choose_period", sleep=True, scrn=True)
        with allure.step("Step 8 выбрать дату, месяц и год для отображения истории"):
            TouchAction(driver).press(x=144, y=344).move_to(x=79, y=302).release().perform()
            TouchAction(driver).press(x=138, y=333).move_to(x=144, y=302).release().perform()
            TouchAction(driver).press(x=78, y=534).move_to(x=77, y=504).release().perform()
            TouchAction(driver).press(x=138, y=532).move_to(x=145, y=501).release().perform()
            click_by_xpath(driver, "btn_done_bottom_list", sleep=True, scrn=True)

    @allure.title("Проверка выбора детализации на будущий период")
    @allure.description("Проверка отображения ошибки при выборе детализации на будущий период на главном экране детализации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_future_detalization(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 открыть вкладку детализации"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 открыть вкладку историю детализации"):
            click_by_accessibility_id(driver, "btn_history_detalization", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на иконку календаря"):
            click_by_xpath(driver, "btn_history_calendar", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на выбор периода по дате и году"):
            click_by_accessibility_id(driver, "btn_choose_period", sleep=True, scrn=True)
        with allure.step("Step 6 выбрать период на будущий год"):
            TouchAction(driver).press(x=292, y=368).move_to(x=300, y=333).release().perform()
            click_by_xpath(driver, "btn_done_bottom_list", sleep=True, scrn=True)

    @allure.title("Проверка выбора детализации более 30 дней")
    @allure.description("Проверка отображения ошибки при выборе детализации более 30 дней на главном экране детализации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_month_detalization(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 открыть вкладку детализации"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 открыть вкладку историю детализации"):
            click_by_accessibility_id(driver, "btn_history_detalization", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на иконку календаря"):
            click_by_xpath(driver, "btn_history_calendar", sleep=True, scrn=True)
        with allure.step("Step 5 нажать на выбор периода по дате и году"):
            click_by_accessibility_id(driver, "btn_choose_period", sleep=True, scrn=True)
        with allure.step("Step 6 выбрать дату более 30 дней и нажать далее"):
            TouchAction(driver).press(x=289, y=305).move_to(x=284, y=337).release().perform()
            click_by_xpath(driver, "btn_done_bottom_list", sleep=True, scrn=True)

    # Проверить что у абонента автозаполнена почта в профиле меню тк при заказе детализации почта уже будет указана
    # Дефолтный период заказа детализации сегодняшний день
    # По умолчанию формат детализации в pdf
    @allure.title("Проверка заказа детализации за дефолтный период")
    @allure.description("Проверка заказа детализации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_defoltday_detalization(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 открыть вкладку детализации"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 открыть вкладку заказать детализацию"):
            click_by_accessibility_id(driver, "btn_order_details", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на кнопку заказать детализацию"):
            click_by_xpath(driver, "btn_order_detalization", sleep=True, scrn=True)

    @allure.title("Проверка заказа детализации за дефолтный период в формате exel")
    @allure.description("Проверка изменения формата отчета по детализации и заказа ее в exel")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_exel_order_detalization(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 открыть вкладку детализации"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 открыть вкладку заказать детализацию"):
            click_by_accessibility_id(driver, "btn_order_details", sleep=True, scrn=True)
        with allure.step("Step 4 изменить формат детализации на эксель"):
            click_by_xpath(driver, "btn_choose_other_format", sleep=False, scrn=True)
            click_by_accessibility_id(driver, "exel_format", sleep=True, scrn=True)
        with allure.step("Step 4 нажать на кнопку заказать детализацию"):
            click_by_xpath(driver, "btn_order_detalization", sleep=True, scrn=True)






















