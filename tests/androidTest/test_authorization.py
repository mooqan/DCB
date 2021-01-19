import allure

from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import send_keys_by_xpath
from confHelper.configHelperAndroid.authAndroid import *


@allure.epic("Epic #1 - Модуль авторизации в приложении Мой О!")
@allure.feature("Feature #1 - Авторизация")
@allure.story("Story #1 - Авторизация")
@allure.severity(allure.severity_level.BLOCKER)
class Test_auth(capsAnroid):
    @allure.title("Тест.авторизация")
    @allure.description("Проверка работоспособности авторизации")
    def test_payment_ewallet(self, driverAndroid):
        with allure.step("Step 1 введение номера"):
            # click_by_id(driver, "btn_confirm", "UseConditionConfirmActivity", scrn=True)
            # m = driver.find_element_by_id("kg.o.nurtelecom:id/et_input")
            # m.send_keys("702 242 516")
            # driverAndroid.implicitly_wait(10)
            # driverAndroid.find_element_by_id("android:id/button1").click()
            send_keys_by_id(driverAndroid, "cnt_phone_number", "+996 702 242 516", sleep=None, scrn=True)
        with allure.step("Step 2 нажатие далее"):
            click_by_id(driverAndroid, "btn_phone_number_next", scrn=True)
        with allure.step("Step 3 введение пароля"):
            # send_keys_by_id(driver, "cnt_phone_pswrd", "Qwerty65", scrn=True)
            send_keys_by_id(driverAndroid, "cnt_phone_pswrd", "Qwerty654321", scrn=True)
        with allure.step("Step 4 нажатие кнопки далее"):
            click_by_id(driverAndroid, "btn_phone_pswrd_next", scrn=True)
        with allure.step("Step 5 нажатие кнопки далее"):
            click_by_xpath(driverAndroid, "btn_cancel_system_secure", scrn=True)
        with allure.step("Step 6 скрытие контейнера о малом балансе"):
            click_by_id(driverAndroid, "space_out_cntn", scrn=True)
        with allure.step("Step 7 скрытие контейнера о сканере"):
            click_by_id(driverAndroid, "btn_scanner_cancel", scrn=True)

    # def test_payment_mwallet(self, driver):
    #     test_authorization(driver)
    #
    #     click_by_id(driver, "btn_scanner_course_cancel", "main_lk", scrn=True)
    #
    #     click_by_id(driver, "btn_o!dengi", "main_omoney", scrn=True)
    #
    #     click_by_id(driver, "btn_scanner_course_cancel", "main_omoney1", scrn=True)
    #
    #     click_by_id(driver, "btn_refill", "ServicePaymentActivity", scrn=True)
    #
    #     click_by_id(driver, "btn_choose_payment_type", "ChoosePaymentTypeActivity", scrn=True)
    #
    #     click_by_xpath(driver, "btn_mwallet", "ChoosePaymentTypeActivity", scrn=True)
    #
    #     send_keys_by_id(driver, "cnt_amount", "ServicePaymentActivity", "10", scrn=True)
    #
    #     click_by_id(driver, "btn_pay", "ReplenishmentConfirmationActivity", scrn=True)
    #
    #     click_by_id(driver, "btn_confirm", "ReplenishmentConfirmationActivity", scrn=True)
    #
    # def test_payment_bcard(self, driver):
    #     test_authorization(driver)
    #
    #     click_by_id(driver, "btn_scanner_course_cancel", "main_lk", scrn=True)
    #
    #     click_by_id(driver, "btn_o!dengi", "main_omoney", scrn=True)
    #
    #     click_by_id(driver, "btn_scanner_course_cancel", "main_omoney1", scrn=True)
    #
    #     click_by_id(driver, "btn_refill", "ServicePaymentActivity", scrn=True)
    #
    #     click_by_id(driver, "btn_choose_payment_type", "ChoosePaymentTypeActivity", scrn=True)
    #
    #     click_by_xpath(driver, "btn_bcard", "ChoosePaymentTypeActivity", scrn=True)
    #
    #     send_keys_by_id(driver, "cnt_amount", "ServicePaymentActivity", "10", scrn=True)
    #
    #     click_by_id(driver, "btn_pay", "ReplenishmentConfirmationActivity", scrn=True)
    #
    #     click_by_id(driver, "btn_confirm", "ReplenishmentConfirmationActivity", scrn=True)

# class Test3(capsAnroid):
#     def test_local(self, driver):
#         Test_authorization(driver)
#
#         click_by_xpath(driver, "btn_side_menu", "MainActivity", scrn=True)
#
#         click_by_xpath(driver, "btn_setings", "MainActivity", scrn=True)
#
#         click_by_id(driver, "btn_settings_lang", "MainActivity", scrn=True)
#
#         click_by_id(driver, "btn_ru_lang", "MainActivity2", scrn=True)
#
#         # click_by_id(driver, "btn_ok", "MainActivity3", scrn=True)
#         k = driver.find_element_by_id('android:id/button1')
#         k.click()
#         driver.save_screenshot('%s/results/appiumscr/' + 'locale_test' + '.png')
#         m = driver.find_element_by_id('kg.o.nurtelecom:id/tv_title')
#         m.get_attribute('text')
#         print(m)

# el = self.driver.find_element_by_accessibility_id('SomeAccessibilityID')
# text = el.text
