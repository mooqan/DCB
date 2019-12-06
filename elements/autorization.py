import os

from confHelper.configHelper import capsAnroid



пше

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