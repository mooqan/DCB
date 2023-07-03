import allure
from appium.webdriver.common.touch_action import TouchAction

from confHelper.configHelperIOS.authIOS import Test_authorization
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import click_by_xpath, click_by_accessibility_id, send_keys_by_accessibility_id, find_element_by_accessibility_id

@allure.epic("Epic #2 - Личный кабинет в приложении МойО!")
@allure.feature("Feature #1 - Личный кабинет главный экран")
@allure.severity(allure.severity_level.BLOCKER)
# Устройство для тестов на английском языке
# У абонента должен быть установлен пакетный тариф, абонент должен быть юзером НУРа не корпоративным
class Test_main_lk(capsIOS):
    # @allure.title("Проверка отображения личного куара абонента")
    # @allure.description("Проверка открытия личного куара на экране Личного кабинета")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_quar_lk(self, driver):
    #     with allure.step("Step 0 блок авторизации"):
    #         Test_authorization(driver)
    #     with allure.step("Step 1 убрать подсказку личного QR"):
    #         click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
    #     with allure.step("Step 2 нажать на иконку куара"):
    #         click_by_accessibility_id(driver, "lk_quar", sleep=True, scrn=True)
    #     with allure.step("Step 3 закрыть боттом лист с личным куаром"):
    #         click_by_accessibility_id(driver, "close_lk_qr", sleep=True, scrn=True)
    #
    # @allure.title("Проверка открытия экрана пополнения своего баланса")
    # @allure.description("Проверка перехода на экран пополнения баланса с личного кабинета")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_balance_replenishment_lk(self, driver):
    #     with allure.step("Step 0 блок авторизации"):
    #         Test_authorization(driver)
    #     with allure.step("Step 1 убрать подсказку личного QR"):
    #         click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
    #     with allure.step("Step 2 нажать на кнопку плюс в контейнере баланса"):
    #         click_by_xpath(driver, "plus_balance_lk", sleep=True, scrn=True)
    #     with allure.step("Step 3 нажать на кнопку назад с экрана пополнения"):
    #         click_by_xpath(driver, "btn_back_from_replenishment", sleep=True, scrn=True)
    #
    # @allure.title("Проверка открытия деталей интернет пакета")
    # @allure.description("Проверка перехода на экран дополнительных услуг по бублику интернет")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_internet_services(self, driver):
    #     with allure.step("Step 0 блок авторизации"):
    #         Test_authorization(driver)
    #     with allure.step("Step 1 убрать подсказку личного QR"):
    #         click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
    #     with allure.step("Step 2 нажать на кнопку плюс в бублике пакета интернет"):
    #         click_by_xpath(driver, "btn_plus_internet", sleep=True, scrn=True)
    #     with allure.step("Step 3 нажать на кнопку назад с экрана дополнительных услуг интернета"):
    #         click_by_xpath(driver, "btn_back_to_lk", sleep=True, scrn=True)
    #
    # @allure.title("Проверка открытия деталей пакета звонков вне сети")
    # @allure.description("Проверка перехода на экран дополнительных услуг по бублику звонки вне сети")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_calls_services(self, driver):
    #     with allure.step("Step 0 блок авторизации"):
    #         Test_authorization(driver)
    #     with allure.step("Step 1 убрать подсказку личного QR"):
    #         click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
    #     with allure.step("Step 2 нажать на кнопку плюс в бублике пакета интернет"):
    #         click_by_xpath(driver, "btn_plus_calls", sleep=True, scrn=True)
    #     with allure.step("Step 3 нажать на кнопку назад с экрана дополнительных услуг интернета"):
    #         click_by_xpath(driver, "btn_back_to_lk", sleep=True, scrn=True)
    #
    # @allure.title("Проверка открытия раздела мои номера")
    # @allure.description("Проверка перехода на экран мои номера")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_my_numbers(self, driver):
    #     with allure.step("Step 0 блок авторизации"):
    #         Test_authorization(driver)
    #     with allure.step("Step 1 убрать подсказку личного QR"):
    #         click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
    #     with allure.step("Step 2 нажать на раздел мои номера"):
    #         click_by_accessibility_id(driver, "btn_my_numbers", sleep=True, scrn=True)
    #     with allure.step("Step 3 нажать на кнопку назад с экрана моих номеров"):
    #         click_by_xpath(driver, "btn_back_to_lk", sleep=True, scrn=True)
    #
    # @allure.title("Проверка открытия saima")
    # @allure.description("Проверка перехода на экран авторизации saima")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_saima_auth(self, driver):
    #     with allure.step("Step 0 блок авторизации"):
    #         Test_authorization(driver)
    #     with allure.step("Step 1 убрать подсказку личного QR"):
    #         click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
    #     with allure.step("Step 2 нажать на раздел saima"):
    #         click_by_accessibility_id(driver, "btn_saima", sleep=True, scrn=True)
    #     with allure.step("Step 3 нажать на кнопку назад с экрана saima"):
    #         click_by_xpath(driver, "btn_back_to_lk", sleep=True, scrn=True)
    #
    # @allure.title("Проверка открытия раздела тарифы")
    # @allure.description("Проверка перехода на экран тарифов")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_tariffs_open(self, driver):
    #     with allure.step("Step 0 блок авторизации"):
    #         Test_authorization(driver)
    #     with allure.step("Step 1 убрать подсказку личного QR"):
    #         click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
    #     with allure.step("Step 2 нажать на раздел тарифы"):
    #         TouchAction(driver).press(x=179, y=522).move_to(x=184, y=147).release().perform()
    #         click_by_accessibility_id(driver, "btn_tariffs", scrn=True)
    #     with allure.step("Step 3 нажать на кнопку назад с экрана тарифов"):
    #         click_by_xpath(driver, "btn_back_to_lk", sleep=True, scrn=True)

    @allure.title("Проверка открытия раздела услуги")
    @allure.description("Проверка перехода на экран услуг")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_services_open(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел услуги"):
            TouchAction(driver).press(x=179, y=522).move_to(x=185, y=148).release().perform()
            click_by_accessibility_id(driver, "btn_service", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на кнопку назад с экрана услуг"):
            click_by_xpath(driver, "btn_back_to_lk", sleep=True, scrn=True)

    @allure.title("Проверка открытия раздела детализации")
    @allure.description("Проверка перехода на экран детализации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_detalization_open(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 нажать на раздел услуги"):
            TouchAction(driver).press(x=179, y=522).move_to(x=203, y=192).release().perform()
            click_by_accessibility_id(driver, "btn_detalizatation", sleep=True, scrn=True)
        with allure.step("Step 3 нажать на кнопку назад с экрана услуг"):
            click_by_xpath(driver, "btn_back_to_lk", sleep=True, scrn=True)



