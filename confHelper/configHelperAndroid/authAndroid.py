from confHelper.configHelperAndroid.standards import click_by_id, send_keys_by_id, click_by_xpath

def Test_authorization(driver):
    driver.implicitly_wait(100)
    # click_by_id(driver, "btn_confirm", "UseConditionConfirmActivity", scrn=True)
    # m = driver.find_element_by_id("kg.o.nurtelecom:id/et_input")
    # m.send_keys("702 242 516")
    send_keys_by_id(driver, "cnt_phone_number", "+996 702 242 516", sleep=None, scrn=True)
    click_by_id(driver, "btn_phone_number_next", scrn=True)
    send_keys_by_id(driver, "cnt_phone_pswrd", "Qwerty654321", scrn=True)
    # send_keys_by_xpath(driver, "cnt_phone_pswrd", "Qwerty654321", scrn=True)
    click_by_xpath(driver, "btn_phone_pswrd_next", scrn=True)
    click_by_xpath(driver, "btn_cancel_system_secure", scrn=True)
    driver.wait_activity(".ui.main.MainActivity", 10)
    click_by_id(driver, "space_out_cntn", scrn=True)
    click_by_id(driver, "btn_scanner_cancel", scrn=True)


