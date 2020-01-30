from confHelper.standards import click_by_id, send_keys_by_id


def test_authorization(driver):
    click_by_id(driver, "btn_confirm", "UseConditionConfirmActivity", scrn=True)

    send_keys_by_id(driver, "cnt_phone_number", "PhoneNumberExistenceCheckActivity", "+996 702 242 516", scrn=True)

    click_by_id(driver, "btn_phone_number_next", "PhoneNumberExistenceCheckActivity")

    send_keys_by_id(driver, "cnt_phone_pswrd", "LoginByPasswordActivity", "qwertyuio", scrn=True)

    click_by_id(driver, "btn_phone_pswrd_next", "LoginByPasswordActivity")

    driver.wait_activity(".ui.main.MainActivity", 20)