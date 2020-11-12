import allure


from confHelper.configHelperIOS.authIOS import Test_authorization
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from elements.elementsIOS import *

@allure.epic("Epic #999 - Ночные тесты")
@allure.feature("Feature #1 - Положительный тест.ночных")
@allure.severity(allure.severity_level.BLOCKER)
class Test_night(capsIOS):
    @allure.story("Story #1 - Ночной тест")
    @allure.title("Ночной тест")
    @allure.description("Проверка неразрыва сессии, наличие избранных, наличие банковских карт, наличие истории платежей, наличие комиссий")
    def test_night(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в О!деньги"):
            click_by_xpath(driver, "btn_O!dengi", scrn=True, sleep=True)
        with allure.step("Step 3 переход в мои карты"):
            click_by_xpath(driver, "my_cards", scrn=True, sleep=True)
        with allure.step("Step 4 возврат на экран О!денег"):
            click_by_xpath(driver, "btn_O!dengi", scrn=True, sleep=True)
        with allure.step("Step 5 переход на экран списка избранных"):
            click_by_xpath(driver, "my_favorites", scrn=True, sleep=True)
        with allure.step("Step 6 возврат на экран О!денег"):
            click_by_xpath(driver, "btn_O!dengi", scrn=True, sleep=True)
        with allure.step("Step 7 переход на экран истории платежей"):
            click_by_xpath(driver, "payment_history", scrn=True, sleep=True)
        with allure.step("Step 7 возврат на экран О!денег"):
            click_by_xpath(driver, "btn_O!dengi", scrn=True, sleep=True)
        with allure.step("Step 8 переход в мобильные операторы"):
            click_by_xpath(driver, "mobile_operators", scrn=True, sleep=True)
        with allure.step("Step 9 выдать доступ к контактам"):
            click_by_xpath(driver, "btn_system_ok", scrn=True, sleep=True)
        with allure.step("Step 10 ввод данных в поле номер"):
            click_by_xpath(driver, "number_7", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_2", sleep=False)
            click_by_xpath(driver, "number_2", sleep=False)
            click_by_xpath(driver, "number_4", sleep=False)
            click_by_xpath(driver, "number_2", sleep=False)
            click_by_xpath(driver, "number_3", sleep=False)
            click_by_xpath(driver, "number_5", sleep=False, scrn=True)
            click_by_xpath(driver, "number_6", sleep=False)
        with allure.step("Step 11 нажать кнопку продолжить"):
            click_by_xpath(driver, "btn_continue", scrn=True, sleep=True)
        with allure.step("Step 12 выбор источника средств баланс"):
            click_by_xpath(driver, "btn_select_type_payment", scrn=True, sleep=True)
            click_by_xpath(driver, "btn_select_mwallet", scrn=True, sleep=True)
        with allure.step("Step 13 ввод суммы и переход на экран подтверждения"):
            click_by_xpath(driver, "input_amount", scrn=True, sleep=True)
            click_by_xpath(driver, "5", scrn=True, sleep=True)
            click_by_xpath(driver, "btn_continue", scrn=True, sleep=True)
        with allure.step("Step 14 переход на экран завершения оплаты"):
            click_by_xpath(driver, "btn_to_pay", scrn=True, sleep=True)
        with allure.step("Step 15 переход на главный экран"):
            click_by_xpath(driver, "btn_home", scrn=True, sleep=True)
        with allure.step("Step 16 категория кошелек и банки"):
            click_by_xpath(driver, "wallet_and_banks", scrn=True, sleep=True)
        with allure.step("Step 17 сервис кошелек Оденьги"):
            click_by_xpath(driver, "wallet_Odengi", scrn=True, sleep=True)
        with allure.step("Step 18 ввод данных из хинта"):
            click_by_xpath(driver, "number_7", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_1", sleep=False)
            click_by_xpath(driver, "number_6", sleep=False, scrn=True)
            click_by_xpath(driver, "number_7", sleep=False)
        with allure.step("Step 19 нажать кнопку продолжить"):
            click_by_xpath(driver, "btn_continue", scrn=True, sleep=True)
        with allure.step("Step 20 выбор источника средств кошелек"):
            click_by_xpath(driver, "btn_select_type_payment", scrn=True, sleep=True)
            click_by_xpath(driver, "btn_select_ewallet", scrn=True, sleep=True)
        with allure.step("Step 21 ввод суммы и переход на экран подтверждения"):
            click_by_xpath(driver, "input_amount", scrn=True, sleep=True)
            click_by_xpath(driver, "5", scrn=True, sleep=True)
            click_by_xpath(driver, "btn_continue", scrn=True, sleep=True)
        with allure.step("Step 22 переход на экран завершения оплаты"):
            click_by_xpath(driver, "btn_to_pay", scrn=True, sleep=True)
        with allure.step("Step 23 переход на главный экран"):
            click_by_xpath(driver, "btn_home", scrn=True, sleep=True)
