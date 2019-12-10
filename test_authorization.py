import os

from confHelper.configHelper import capsAnroid
from confHelper.standards import click_by_id, send_keys_by_id

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

directory = '/Users/ripvantesla/PycharmProjects/sample-code/sample-code/examples/python/pytest/results/appiumscr/'
file_name = 'screenshot.png'
F_EXT = ".png"

class Test(capsAnroid):
    def test_authorization(self, driver):
        click_by_id(driver, "btn_confirm", "UseConditionConfirmActivity")

        send_keys_by_id(driver, "cnt_phone_number", "PhoneNumberExistenceCheckActivity", "+996 702 242 516")

        click_by_id(driver, "btn_phone_number_next", "PhoneNumberExistenceCheckActivity")

        send_keys_by_id(driver, "cnt_phone_pswrd", "LoginByPasswordActivity", "qwerty654321")

        click_by_id(driver, "btn_phone_pswrd_next", "LoginByPasswordActivity")

        driver.wait_activity(".ui.main.MainActivity", 20)

    def test_lk(self, driver):
        self.test_authorization(driver)

        # click_by_id(driver, "btn_refill", "ServicePaymentActivity")
        # driver.back()

        click_by_id(driver, "btn_internet", "InternetServiceActivity")
        driver.back()

        click_by_id(driver, "btn_outgoing_call", "CallServiceActivity")
        driver.back()

        click_by_id(driver, "btn_sub_numbers", "ManageNumbersActivity")
        driver.back()

        # click_by_id(driver, "btn_lottery", "LotteryInfoActivity")
        # driver.back()

        click_by_id(driver, "btn_services", "ServiceCategoryActivity")
        driver.back()

        click_by_id(driver, "btn_tariffs", "TariffCategoryActivity")
        driver.back()

        click_by_id(driver, "btn_detalizatation", "CompleteDetalizationActivity")