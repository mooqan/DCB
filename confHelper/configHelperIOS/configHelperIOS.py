import os

import allure
import pytest
from allure_commons.types import AttachmentType

from appium import webdriver
from helpers import take_screenhot_and_logcat


APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
IOS_PLATFORM_VERSION = '13.5'
IOS_DEVICE_NAME = ''


def take_screenshot_and_logcat(driver, device_logger, calling_request):
    pass


class WebDriver(object):
    pass


class capsIOS:
    @pytest.fixture(scope="function")
    def driver(self, request, device_logger):
        desired_caps = {
            'app': '/Users/nurtest/Desktop/App Release 2021-06-17 12-01-15/Main.ipa',
            'bundleId': 'kg.o.nurtelecom',
            'udid': '370f6355c96bad6c0db37b689668b389d134bd55',
            'platformName': 'iOS',
            'platformVersion': os.getenv('IOS_PLATFORM_VERSION') or '14.4',
            'deviceName': os.getenv('IOS_DEVICE_NAME') or 'iPhone 6s',
            'xcodeOrgId': 'Z8Y2883349',
            'xcodeSigningId': 'iPhone Developer',
            'automationName': "XCUITest",
            'useNewWDA': 'true',
            'appActivity': '.ui.splash.SplashScreenActivity',
            'autoGrantPermissions': 'true',
            'connectHardwareKeyboard': 'false',
            'showIOSLog': 'true',
            'enablePerformanceLogging': 'true',
            'nowReset': 'true',
            # 'autoAcceptAlerts': 'true',
        }

        calling_request = request._pyfuncitem.name

        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

        def fin():
            take_screenshot_and_logcat(driver, device_logger, calling_request)
            # allure.attach(driver.get_log("syslog"), name="log", attachment_type="CSV").body.encode()


            # for data in logcat_data:
            #     data_string = str(data['timestamp']) + ":  " + str(data['message'])
            # allure.attach
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value
