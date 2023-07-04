import pytest

from appium import webdriver
from helpers import take_screenshot_and_logcat
from confHelper.configHelperAndroid.devices_capabilities import device

APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'


class capsAnroid:
    @pytest.fixture(scope="function")
    def driverAndroid(self, request, device_logger):

        # Для смены девайса нужно сменить ключь в device.get(1)
        # Доступные ключи Pixel 3A XL == 1 ,  Xiaomi Note 5  ==  2 , Samsung S10 == 3 ,
        # Homtom HT17 == 4 , Sony Z2 == 5, Samsung S10 == 6 (Исключительно для ночных работ)

        calling_request = request._pyfuncitem.name

        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, device.get(1))

        def fin():
            take_screenshot_and_logcat(driver, device_logger, calling_request)
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value