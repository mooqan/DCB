import allure


from confHelper.configHelperIOS.authIOS import Test_authorization
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from elements.elementsIOS import *

@allure.epic("Epic #3 - Модуль О!Деньги")
@allure.feature("Feature #1 - О!Деньги")
@allure.severity(allure.severity_level.BLOCKER)
class Test_balance(capsIOS):
    @allure.story("Story #1 - Главная страница О!денег")
    @allure.title("Тест. Пополнение себе на mwallet положительный")
    @allure.description("Проверка пополнения себе баланса")
    def test_balance(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход на экран оплаты с лк"):
            click_by_xpath(driver, "btn_balance_plus", scrn=True, sleep=True)
        with allure.step("Step 3 открыть экран с источниками средств"):
            click_by_xpath(driver, "btn_select_type_payment", scrn=True, sleep=True)
        with allure.step("Step 4 выбор источника средств"):
            click_by_xpath(driver, "btn_select_ewallet", scrn=True, sleep=True)
        with allure.step("Step 5 ввод данных"):
            click_by_xpath(driver, "input_amount", scrn=True, sleep=True)
            click_by_xpath(driver, "5", scrn=True, sleep=True)
        with allure.step("Step 6 переход по кнопке продолжить"):
            click_by_xpath(driver, "btn_continue", scrn=True, sleep=True)
        # with allure.step("Step 7 переход на экран оплаты"):
        #     click_by_xpath(driver, "btn_to_pay", scrn=True, sleep=True)
        # with allure.step("Step 8 переход на главный экран"):
        #     click_by_xpath(driver, "btn_home", scrn=True, sleep=True)
