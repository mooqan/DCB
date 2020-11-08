import allure

from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from elements.elementsIOS import *

@allure.epic("Epic #1")
@allure.feature("Feature #1 - Авторизация")
@allure.story("Story #1 - Авторизация")
class Test(capsIOS):
    @allure.title("Тест.положительный Авторизация в приложение")
    @allure.description("Прохождение флоу авторизации в приложении с чистой установкой")
    def test_authorization(self, driver):
        click_by_xpath(driver, "allow_perm", sleep=True, scrn=True)

        with allure.step("Step 1 введение номера авторизации"):
            # send_keys_by_id(driver, "phone_number_cnt", "700000516", sleep=False, scrn=True)
            click_by_xpath(driver, "number_7", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_0", sleep=False)
            click_by_xpath(driver, "number_5", sleep=False)
            click_by_xpath(driver, "number_1", sleep=False, scrn=True)
            click_by_xpath(driver, "number_6", sleep=False)

        with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
            # click_by_id(driver, "phone_number_next", sleep=True, scrn=True)
            click_by_xpath(driver, "Further2", sleep=False, scrn=True)
        with allure.step("Step 3 введение пароля авторизации"):
            # send_keys_by_id(driver, "phone_pass_cnt", "Qwerty7654321", sleep=False, scrn=True)
            click_by_xpath(driver, "shift", sleep=False)
            click_by_xpath(driver, "Q", sleep=False)
            click_by_xpath(driver, "w", sleep=False)
            click_by_xpath(driver, "e", sleep=False)
            click_by_xpath(driver, "r", sleep=False)
            click_by_xpath(driver, "t", sleep=False)
            click_by_xpath(driver, "y", sleep=False)
            click_by_xpath(driver, "more", sleep=False)
            click_by_xpath(driver, "3", sleep=False)
            click_by_xpath(driver, "2", sleep=False, scrn=True)
            click_by_xpath(driver, "1", sleep=False)
        with allure.step("Step 4 нажатие кнопки продолжить после введения пароля"):
            # click_by_id(driver, "pass_number_next", sleep=False, scrn=True)
            click_by_xpath(driver, "Further2", sleep=False, scrn=True)
        with allure.step("Step 5 создание пинкода для авторизации"):
            click_by_xpath(driver, "pin_1", sleep=False)
            click_by_xpath(driver, "pin_1", sleep=False, scrn=True)
            click_by_xpath(driver, "pin_1", sleep=False)
            click_by_xpath(driver, "pin_1", sleep=False)
        with allure.step("Step 6 подтверждение пинкода для авторизации"):
            click_by_xpath(driver, "pin_1", sleep=False)
            click_by_xpath(driver, "pin_1", sleep=False, scrn=True)
            click_by_xpath(driver, "pin_1", sleep=False)
            click_by_xpath(driver, "pin_1", sleep=False)



        #     test_authorization(driver)
    #
    #     click_by_id(driver, "btn_refill", "ServicePaymentActivity", scrn=True)
    #     driver.back()
    #
    #     click_by_id(driver, "btn_internet", "InternetServiceActivity", scrn=True)
    #     driver.back()
    #
    #     click_by_id(driver, "btn_outgoing_call", "CallServiceActivity", scrn=True)
    #     driver.back()
    #
    #     click_by_id(driver, "btn_sub_numbers", "ManageNumbersActivity", scrn=True)
    #     driver.back()
    #
    #     # click_by_id(driver, "btn_lottery", "LotteryInfoActivity", scrn=True)
    #     # driver.back()
    #
    #     click_by_id(driver, "btn_services", "ServiceCategoryActivity", scrn=True)
    #     driver.back()
    #
    #     click_by_id(driver, "btn_tariffs", "TariffCategoryActivity", scrn=True)
    #     driver.back()
    #
    #     click_by_id(driver, "btn_detalizatation", "CompleteDetalizationActivity", scrn=True)
    #
    # def test_payment(self, driver):
    #     test_authorization(driver)
    #
    #     click_by_id(driver, "btn_o!dengi", "GettingWalletStatusActivity", scrn=True)
    #
    #     click_by_xpath(driver, "btn_self_refill", "ServicePaymentActivity", scrn=True)
