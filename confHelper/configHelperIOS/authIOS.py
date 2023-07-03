import allure

from confHelper.configHelperIOS.standards import *


def Test_authorization(driver):
    # click_by_xpath(driver, "allow_perm", sleep=True, scrn=True)
    with allure.step("Step 0 выдать разрешение на доступ"):
        click_by_xpath(driver, "accept_main_alert")
    with allure.step("Step 1 введение номера авторизации"):
        send_keys_by_accessibility_id(driver, "number_field", "702243852", sleep=False, scrn=True)
    with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
        click_by_accessibility_id(driver, "phone_number_next", sleep=True, scrn=True)
    with allure.step("Step 3 введение пароля авторизации"):
        send_keys_by_accessibility_id(driver, "phone_pass_cnt", "Qwerty65", sleep=False, scrn=True)
    with allure.step("Step 4 нажатие кнопки продолжить после введения пароля"):
        click_by_accessibility_id(driver, "pass_number_next", sleep=False, scrn=True)
        click_by_accessibility_id(driver, "cancel")
    with allure.step("Step 5 создание пинкода для авторизации"):
        click_by_accessibility_id(driver, "pin_1")
        click_by_accessibility_id(driver, "pin_1")
        click_by_accessibility_id(driver, "pin_1")
        click_by_accessibility_id(driver, "pin_1")
    with allure.step("Step 6 подтверждение пинкода для авторизации"):
        click_by_accessibility_id(driver, "pin_1")
        click_by_accessibility_id(driver, "pin_1")
        click_by_accessibility_id(driver, "pin_1")
        click_by_accessibility_id(driver, "pin_1")
