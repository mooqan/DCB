import os

from confHelper.configHelper import capsAnroid
from elements.autorization import elements_autorization, elements_lk
from confHelper.selector_helper import find_element_by_id

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test(capsAnroid):
    def test_authorization(self, driver):
        confirm_button = find_element_by_id(elements_autorization.get("btn_confirm"), driver)
        confirm_button.click()

        driver.implicitly_wait(30)
        phone_number_container = find_element_by_id(elements_autorization.get("cnt_phone_number"), driver)
        phone_number_container.send_keys("+996 702 242 516")

        driver.implicitly_wait(30)
        phone_number_next_button = find_element_by_id(elements_autorization.get("btn_phone_number_next"), driver)
        phone_number_next_button.click()

        driver.implicitly_wait(30)
        phone_pswrd_container = find_element_by_id(elements_autorization.get("cnt_phone_pswrd"), driver)
        phone_pswrd_container.send_keys("qwerty654321")

        driver.implicitly_wait(30)
        phone_pswrd_next_button = find_element_by_id(elements_autorization.get("btn_phone_pswrd_next"), driver)
        phone_pswrd_next_button.click()

        driver.wait_activity(".ui.main.MainActivity", 100)

    def test_lk(self, driver):
        self.test_authorization(driver)
        internet_Button = find_element_by_id(elements_lk.get("btn_internet"), driver)
        internet_Button.click()
        driver.back()
        driver.implicitly_wait(30)


# confirmButtonResource.click()
        #
        # confirmButton = driver.find_element_by_id("kg.o.nurtelecom:id/confirm")
        # confirmButton.click
        #
        #
        # driver.implicitly_wait(30)
        #
        # phoneNumberConteinerResource.send_keys("+996 702 242 516")
        # driver.implicitly_wait(30)
        #
        # phoneNumberAcceptResource.click()
        # driver.implicitly_wait(30)
        #
        # phonePasswordContainerResource.send_keys("qwerty654321")
        # driver.implicitly_wait(30)
        #
        # phonePasswordAcceptResource.click()
        # driver.wait_activity(".ui.main.MainActivity", 100)

    # def test_lk_screen(self, driver, ):
    #     self.test_authorization(driver)
    #     driver.implicitly_wait(30)
    #
    #     internetButtonResource.click()
    #     driver.back()
    #
    #     driver.implicitly_wait(30)
    #     callLimmitButtonResource.click()
    #     driver.back()
    #     driver.implicitly_wait(30)


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
