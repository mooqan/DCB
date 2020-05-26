import os

import allure

from confHelper.configHelper import capsAnroid
from confHelper.standards import click_by_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from confHelper.auth import test_authorization

@allure.epic("Epic #1")
@allure.feature("Feature #1 - Авторизация")
@allure.story("Story #1 - Авторизация")
class Test_LK(capsAnroid):
    @allure.title("Тест.переходы на главном экране ЛК")
    @allure.description("Проверка работоспособности переходов на главной странице ЛК")
    def test_lk(self, driver):
        with allure.step("Step 0 блок успешной авторизации"):
            test_authorization(driver)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода на пополнение мобильного баланса"):
            click_by_id(driver, "btn_refill", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 2 проверка перехода в окно доступного интернет трафика"):
            click_by_id(driver, "btn_internet", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 3 проверка перехода в окно доступного трафика билинга"):
            click_by_id(driver, "btn_outgoing_call", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 4 проверка перехода в окно 'Мои номера'"):
            click_by_id(driver, "btn_sub_numbers", scrn=True, sleep=True)
            driver.back()
        # with allure.step("Step 5 проверка перехода в окно 'Лотерея'"):
        #     click_by_id(driver, "btn_lottery", scrn=True, sleep=True)
        #     driver.back()
        with allure.step("Step 6 проверка перехода в окно 'Сервисы'"):
            click_by_id(driver, "btn_services", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 7 проверка перехода в окно 'Тарифы'"):
            click_by_id(driver, "btn_tariffs", scrn=True, sleep=True)
            driver.back()
        with allure.step("Step 8 проверка перехода в окно 'Детализация'"):
            click_by_id(driver, "btn_detalizatation", scrn=True, sleep=True)
            driver.back()
    @allure.title("Тест.сохранения профиля ЛК")
    @allure.description("Проверка работоспособности сохраниения профиля ЛК")
    def test_left_menu_profile(self, driver):
        with allure.step("Step 0 блок успешной авторизации"):
            test_authorization(driver)
        # click_by_id(driver, "btn_scanner_course_cancel", scrn=True)
        with allure.step("Step 1 проверка перехода в боковое меню"):
           click_by_xpath(driver, "btn_left_menu", scrn=True, sleep=True)
        with allure.step("Step 2 проверка перехода в окно  'Профиля'"):
            click_by_id(driver, "btn_edit_profile", scrn=True, sleep=True)
        with allure.step("Step 3 проверка заполнения почты в окне 'Профиля'"):
           send_keys_by_id(driver, "cnt_email", "ripvantesla@gmail.com", scrn=True, sleep=True)
        with allure.step("Step 4 проверка заполнения имени в окне 'Профиля'"):
            send_keys_by_id(driver, "cnt_name", "Anatolii", scrn=True, sleep=True)
        with allure.step("Step 5 проверка заполнения фамилии в окне 'Профиля'"):
            send_keys_by_xpath(driver, "cnt_last_name", "Petrov", scrn=True, sleep=True)
        with allure.step("Step 6 проверка заполнения почты в окне 'Профиля'"):
            click_by_id(driver, "btn_profile_save", scrn=True, sleep=True)






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