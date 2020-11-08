import allure

from confHelper.configHelperIOS.standards import click_by_xpath


def Test_authorization(driver):
    click_by_xpath(driver, "allow_perm", sleep=True, scrn=True)

    with allure.step("Step 1 введение номера авторизации"):
        # send_keys_by_id(driver, "phone_number_cnt", "700000516", sleep=False, scrn=True)
        click_by_xpath(driver, "number_7")
        click_by_xpath(driver, "number_0")
        click_by_xpath(driver, "number_2")
        click_by_xpath(driver, "number_2")
        click_by_xpath(driver, "number_4")
        click_by_xpath(driver, "number_3")
        click_by_xpath(driver, "number_8")
        click_by_xpath(driver, "number_5", scrn=True)
        click_by_xpath(driver, "number_2")

    with allure.step("Step 2 нажатие кнопки продолжить после введения номера"):
        # click_by_id(driver, "phone_number_next", sleep=True, scrn=True)
        click_by_xpath(driver, "Further2", sleep=True, scrn=True)
    with allure.step("Step 3 введение пароля авторизации"):
        # send_keys_by_id(driver, "phone_pass_cnt", "Qwerty7654321", sleep=False, scrn=True)
        click_by_xpath(driver, "shift")
        click_by_xpath(driver, "Q")
        click_by_xpath(driver, "w")
        click_by_xpath(driver, "e")
        click_by_xpath(driver, "r")
        click_by_xpath(driver, "t")
        click_by_xpath(driver, "y")
        click_by_xpath(driver, "more")
        click_by_xpath(driver, "6")
        click_by_xpath(driver, "5", scrn=True)
    with allure.step("Step 4 нажатие кнопки продолжить после введения пароля"):
        # click_by_id(driver, "pass_number_next", sleep=False, scrn=True)
        click_by_xpath(driver, "Further2", scrn=True)
    with allure.step("Step 5 создание пинкода для авторизации"):
        click_by_xpath(driver, "pin_1")
        click_by_xpath(driver, "pin_1", scrn=True)
        click_by_xpath(driver, "pin_1")
        click_by_xpath(driver, "pin_1")
    with allure.step("Step 6 подтверждение пинкода для авторизации"):
        click_by_xpath(driver, "pin_1")
        click_by_xpath(driver, "pin_1", scrn=True)
        click_by_xpath(driver, "pin_1")
        click_by_xpath(driver, "pin_1")
