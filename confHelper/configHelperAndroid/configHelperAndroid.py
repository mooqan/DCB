import json

import pytest
from appium import webdriver
from helpers import take_screenshot_and_logcat
from confHelper.configHelperAndroid.devices_capabilities import device
import allure

APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'


class capsAnroid:
    @pytest.fixture(scope="function")
    def driverAndroid(self, request, device_logger):
        calling_request = request._pyfuncitem.name
        device_info = device.get(1)

        with allure.step("Step #0 Device Information"):
            allure.attach(json.dumps(device_info, indent=4), "Device Info", allure.attachment_type.JSON)

        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, device_info)

        def fin():
            take_screenshot_and_logcat(driver, device_logger, calling_request)
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value
