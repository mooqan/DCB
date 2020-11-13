import pytest

from appium import webdriver
from helpers import take_screenhot_and_logcat
from confHelper.configHelperAndroid.devices_capabilities import device

APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'


class capsAnroid:
    @pytest.fixture(scope="function")
    def driver(self, request, device_logger):

        calling_request = request._pyfuncitem.name

        # Для смены девайса нужно сменить ключь в device.get(1)
        # Доступные ключи Pixel 3A XL == 1 ,  Xiaomi Note 5  ==  2 , Samsung S10 == 3 ,
        # Homtom HT17 == 4

        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, device.get(4))

        def fin():
            take_screenhot_and_logcat(driver, device_logger, calling_request)
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value