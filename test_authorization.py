import os

from confHelper.configHelper import capsAnroid

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test(capsAnroid):
    def test_authorization(self, driver):
        confirmButton = driver.find_element_by_id("kg.o.nurtelecom:id/confirm")
        confirmButton.click()
        driver.implicitly_wait(30)

        phoneNumberContainer = driver.find_element_by_id("kg.o.nurtelecom:id/phone_number")
        phoneNumberContainer.send_keys("+996 702 242 516")
        driver.implicitly_wait(30)

        phoneNumberAccept = driver.find_element_by_id("kg.o.nurtelecom:id/next")
        phoneNumberAccept.click()
        driver.implicitly_wait(30)

        phonePasswordContainer = driver.find_element_by_id("kg.o.nurtelecom:id/et_password")
        phonePasswordContainer.send_keys("qwerty654321")
        driver.implicitly_wait(30)

        phonePasswordAccept = driver.find_element_by_id("kg.o.nurtelecom:id/confirm")
        phonePasswordAccept.click()
        driver.wait_activity(".ui.main.MainActivity", 100)

    def test_lk_screen(self, driver, ):
        self.test_authorization(driver)
        internetButton = driver.find_element_by_id("kg.o.nurtelecom:id/internet_leftover")
        internetButton.click()
        driver.back()
        callLimmitButton = driver.find_element_by_id("kg.o.nurtelecom:id/outgoing_call_leftover")
        callLimmitButton.click()
        driver.back()
        driver.implicitly_wait(30)


# class Test1(Test):
#     def test_add_contacts(self, driver):
#         internetButton = driver.find_element_by_id("kg.o.nurtelecom:id/internet_leftover")
#         internetButton.click()
#         driver.implicitly_wait(30)

        # textfields = driver.find_elements_by_class_name("android.widget.EditText")
        # textfields[0].send_keys("Appium User")
        # textfields[2].send_keys("someone@appium.io")
        #
        # assert 'Appium User' == textfields[0].text
        # assert 'someone@appium.io' == textfields[2].text
        #
        # driver.find_element_by_accessibility_id("Save").click()
        #
        # # for some reason "save" breaks things
        # alert = driver.switch_to_alert()
        #
        # # no way to handle alerts in Android
        # driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()
        #
        # driver.press_keycode(3)
