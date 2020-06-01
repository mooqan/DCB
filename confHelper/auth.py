from confHelper.standards import click_by_id, send_keys_by_id

def Test_authorization(driver):
    driver.implicitly_wait(100)
    # click_by_id(driver, "btn_confirm", "UseConditionConfirmActivity", scrn=True)
    send_keys_by_id(driver, "cnt_phone_number", "702 242 516", sleep=None, scrn=True)
    click_by_id(driver, "btn_phone_number_next", scrn=True)
    send_keys_by_id(driver, "cnt_phone_pswrd", "Qwerty65", scrn=True)
    click_by_id(driver, "btn_phone_pswrd_next", scrn=True)
    driver.wait_activity(".ui.main.MainActivity", 10)


