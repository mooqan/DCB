import os
import pytest

from appium import webdriver
from helpers import take_screenhot_and_logcat


APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
IOS_PLATFORM_VERSION = '13.3'
IOS_DEVICE_NAME = ''

class capsIOS:
    @pytest.fixture(scope="function")
    def driver(self, request, device_logger):
        desired_caps = {
            'app': '/Users/test/Library/Developer/Xcode/DerivedData/App-duxyvcnoyuemovfmttrrprfuafgk/Build/Products/Debug-iphonesimulator/Main.app',
            'platformName': 'iOS',
            'platformVersion': os.getenv('IOS_PLATFORM_VERSION') or '13.3',
            'deviceName': os.getenv('IOS_DEVICE_NAME') or 'iPhone 8',
            'appActivity': '.ui.splash.SplashScreenActivity',
            'autoGrantPermissions': 'true',
            'connectHardwareKeyboard':'false',
            'showIOSLog':'true',
            'enablePerformanceLogging':'true'
        }
        calling_request = request._pyfuncitem.name

        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

        def fin():
            take_screenhot_and_logcat(driver, device_logger, calling_request)

            # for data in logcat_data:
            #     data_string = str(data['timestamp']) + ":  " + str(data['message'])
            # allure.attach
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value
