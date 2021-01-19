""" Standart test cases"""
import os

import allure
from allure_commons.types import AttachmentType

from confHelper.configHelperAndroid.selectorHelper import find_element_by_id, find_element_by_xpath, \
    find_elements_by_accessibility_id
from elements.elementsAndroid import elements, list_activity, elements_path
import time

directory = '%s/results/appiumscr/' % os.getcwd()
file_name = 'screenshot.png'
F_EXT = ".png"


def click_by_id(driver, id, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    btn = find_element_by_id(elements.get(id), driver)
    btn.click()

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    driver.implicitly_wait(10)


def send_keys_by_id(driver, id, text, sleep=None, scrn=None):
    driver.implicitly_wait(10)

    cnt = find_element_by_id(elements.get(id), driver)
    cnt.send_keys(text)

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    driver.implicitly_wait(5)


def click_by_xpath(driver, path, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    btn = find_element_by_xpath(elements_path.get(path), driver)
    btn.click()

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    driver.implicitly_wait(5)


def send_keys_by_xpath(driver, id, text, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    cnt = find_element_by_xpath(elements_path.get(id), driver)
    cnt.send_keys(text)

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    driver.implicitly_wait(5)


def click_by_ac(driver, id, activity, scrn=None):
    driver.implicitly_wait(10)
    btn = find_elements_by_accessibility_id(elements.get(id), driver)
    btn.click()
    x = driver.wait_activity(list_activity.get(activity), 10)

    if not x:
        print('not in' + activity)

    time.sleep(5)

    if scrn is True:
        driver.save_screenshot(directory + activity + F_EXT)

    driver.implicitly_wait(10)


def screenshot(driver, sleep=None):
    if sleep is True:
        time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def swipe(driver, sleep=None, scrn=None):
    driver.swipe(100, 600, 100, 1400)

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
