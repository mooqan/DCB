import os

from confHelper.configHelper import capsAnroid
from confHelper.standards import click_by_id, send_keys_by_id, click_by_xpath
from confHelper.auth import test_authorization

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Test(capsAnroid):
    def test_lk(self, driver):
        test_authorization(driver)

        click_by_id(driver, "btn_refill", "ServicePaymentActivity", scrn=True)
        driver.back()

        click_by_id(driver, "btn_internet", "InternetServiceActivity", scrn=True)
        driver.back()

        click_by_id(driver, "btn_outgoing_call", "CallServiceActivity", scrn=True)
        driver.back()

        click_by_id(driver, "btn_sub_numbers", "ManageNumbersActivity", scrn=True)
        driver.back()

        # click_by_id(driver, "btn_lottery", "LotteryInfoActivity", scrn=True)
        # driver.back()

        click_by_id(driver, "btn_services", "ServiceCategoryActivity", scrn=True)
        driver.back()

        click_by_id(driver, "btn_tariffs", "TariffCategoryActivity", scrn=True)
        driver.back()

        click_by_id(driver, "btn_detalizatation", "CompleteDetalizationActivity", scrn=True)

    def test_payment(self, driver):
        test_authorization(driver)

        click_by_id(driver, "btn_o!dengi", "GettingWalletStatusActivity", scrn=True)

        click_by_xpath(driver, "btn_self_refill", "ServicePaymentActivity", scrn=True)

class Test2(capsAnroid):
    def test_payment_ewallet(self, driver):
        test_authorization(driver)

        click_by_id(driver, "btn_o!dengi", "GettingWalletStatusActivity", scrn=True)

        click_by_id(driver, "btn_self_refill", "ServicePaymentActivity", scrn=True)

        click_by_id(driver, "btn_choose_payment_type", "ChoosePaymentTypeActivity", scrn=True)

        click_by_xpath(driver, "btn_ewallet", "ChoosePaymentTypeActivity", scrn=True)

        send_keys_by_id(driver, "cnt_amount", "ServicePaymentActivity", "10", scrn=True)

        click_by_id(driver, "btn_pay", "ReplenishmentConfirmationActivity", scrn=True)

        click_by_id(driver, "btn_confirm", "ReplenishmentConfirmationActivity", scrn=True)

    def test_payment_mwallet(self, driver):
        test_authorization(driver)

        click_by_id(driver, "btn_o!dengi", "GettingWalletStatusActivity", scrn=True)

        click_by_id(driver, "btn_self_refill", "ServicePaymentActivity", scrn=True)

        click_by_id(driver, "btn_choose_payment_type", "ChoosePaymentTypeActivity", scrn=True)

        click_by_xpath(driver, "btn_mwallet", "ChoosePaymentTypeActivity", scrn=True)

        send_keys_by_id(driver, "cnt_amount", "ServicePaymentActivity", "10", scrn=True)

        click_by_id(driver, "btn_pay", "ReplenishmentConfirmationActivity", scrn=True)

        click_by_id(driver, "btn_confirm", "ReplenishmentConfirmationActivity", scrn=True)

    # def test_payment_bcard(self, driver):
    #     self.test_authorization(driver)
    #
    #     click_by_id(driver, "btn_o!dengi", "GettingWalletStatusActivity", scrn=True)
    #
    #     click_by_id(driver, "btn_self_refill", "ServicePaymentActivity", scrn=True)
    #
    #     click_by_id(driver, "btn_choose_payment_type", "ChoosePaymentTypeActivity", scrn=True)
    #
    #     click_by_xpath(driver, "btn_bcard", "ChoosePaymentTypeActivity", scrn=True)
    #
    #     send_keys_by_id(driver, "cnt_amount", "ServicePaymentActivity", "10", scrn=True)
    # git
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