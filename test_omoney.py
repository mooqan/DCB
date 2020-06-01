import allure

from confHelper.configHelper import capsAnroid
from confHelper.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from confHelper.auth import Test_authorization


class Test_OMoney(capsAnroid):
    def test_OMoney(self, driver):
        Test_authorization(driver)
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