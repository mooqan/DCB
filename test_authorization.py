import os

import allure

from confHelper.configHelper import capsAnroid
from confHelper.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from confHelper.auth import *

@allure.epic("Epic #1")
@allure.feature("Feature #1 - Авторизация")
@allure.story("Story #1 - Авторизация")
class test_auth(capsAnroid):
    def test_payment_ewallet(self, driver):
        with allure.step("Step 1 введение номера"):
            send_keys_by_id(driver, "cnt_phone_number", "702 242 516", sleep=None, scrn=True)


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

class Test3(capsAnroid):
    def test_local(self, driver):
        Test_authorization(driver)

        click_by_xpath(driver, "btn_side_menu", "MainActivity", scrn=True)

        click_by_xpath(driver, "btn_setings", "MainActivity", scrn=True)

        click_by_id(driver, "btn_settings_lang", "MainActivity", scrn=True)

        click_by_id(driver, "btn_ru_lang", "MainActivity2", scrn=True)

        # click_by_id(driver, "btn_ok", "MainActivity3", scrn=True)
        k = driver.find_element_by_id('android:id/button1')
        k.click()
        driver.save_screenshot('%s/results/appiumscr/' + 'locale_test' + '.png')
        m = driver.find_element_by_id('kg.o.nurtelecom:id/tv_title')
        m.get_attribute('text')
        print(m)

        # el = self.driver.find_element_by_accessibility_id('SomeAccessibilityID')
        # text = el.text