import os

from confHelper.configHelper import capsAnroid
from confHelper.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from confHelper.auth import test_authorization

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Test_LK(capsAnroid):
    # def test_lk(self, driver):
    #     test_authorization(driver)
    #     click_by_id(driver, "btn_scanner_course_cancel", "ServicePaymentActivity1", scrn=True)
    #
    #     click_by_id(driver, "btn_refill", "ServicePaymentActivity", scrn=True)
    #     driver.back()
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

    def test_left_menu_profile(self, driver):
        test_authorization(driver)
        click_by_id(driver, "btn_scanner_course_cancel", "main_lk", scrn=True)

        click_by_xpath(driver, "btn_left_menu", "btn_left_menu", scrn=True)

        click_by_id(driver, "btn_edit_profile", "btn_edit_profile", scrn=True)

        send_keys_by_id(driver, "cnt_email", "cnt_email", "ripvantesla@gmail.com", scrn=True)
        send_keys_by_id(driver, "cnt_name", "cnt_name", "Anatolii", scrn=True)
        send_keys_by_xpath(driver, "cnt_last_name", "cnt_last_name", "Petrov", scrn=True)

        click_by_id(driver, "btn_profile_save", "btn_profile_save", scrn=True)






class Test_OMoney(capsAnroid):
    def test_OMoney(self, driver):
        test_authorization(driver)
        click_by_id(driver, "btn_scanner_course_cancel", "main_lk", scrn=True)

        click_by_id(driver, "btn_o!dengi", "main_omoney", scrn=True)

        click_by_id(driver, "btn_scanner_course_cancel", "main_omoney1", scrn=True)

        click_by_id(driver, "btn_refill", "refill", scrn=True)
        driver.back()

        click_by_id(driver, "btn_credit", "credit", scrn=True)
        driver.back()

        click_by_id(driver, "btn_cards", "cards", scrn=True)
        driver.back()

        click_by_id(driver, "btn_history", "history", scrn=True)
        driver.back()

        click_by_id(driver, "btn_fines", "fines", scrn=True)
        driver.back()

        click_by_id(driver, "btn_qr_scanner", "qr_scanner", scrn=True)
        driver.back()

        click_by_id(driver, "btn_add_fav", "add_fav", scrn=True)
        driver.back()

        click_by_id(driver, "btn_search_catalog", "catalog", scrn=True)
        driver.back()

    # def test_payment_ewallet(self, driver):
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
    #     click_by_xpath(driver, "btn_ewallet", "ChoosePaymentTypeActivity", scrn=True)
    #
    #     send_keys_by_id(driver, "cnt_amount", "ServicePaymentActivity", "10", scrn=True)
    #
    #     click_by_id(driver, "btn_pay", "ReplenishmentConfirmationActivity", scrn=True)
    #
    #     click_by_id(driver, "btn_confirm", "ReplenishmentConfirmationActivity", scrn=True)

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
        test_authorization(driver)

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