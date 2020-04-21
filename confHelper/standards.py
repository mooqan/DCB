""" Standart test cases"""
import os

from confHelper.selector_helper import find_element_by_id, find_element_by_xpath, find_elements_by_accessibility_id
from elements.autorization import elements, list_activity, elements_path
import time


directory = '%s/results/appiumscr/' % os.getcwd()
file_name = 'screenshot.png'
F_EXT = ".png"

def click_by_id(driver, id, activity, scrn=None):
    driver.implicitly_wait(10)
    btn = find_element_by_id(elements.get(id), driver)

    btn.click()

    # driver.wait_activity(list_activity.get(activity), 10)

    if not driver.wait_activity(list_activity.get(activity), 10):
        print('not in' + activity)

    time.sleep(5)

    if scrn is True:
        driver.save_screenshot(directory + activity + F_EXT)

    driver.implicitly_wait(10)

def send_keys_by_id(driver, id, activity, text, scrn=None):
    driver.implicitly_wait(10)
    cnt = find_element_by_id(elements.get(id), driver)
    cnt.send_keys(text)
    # driver.wait_activity(list_activity.get(activity), 10)

    if not driver.wait_activity(list_activity.get(activity), 10):
        print('not in' + activity)

    print('suc')

    time.sleep(5)

    if scrn is True:
        driver.save_screenshot(directory + activity + F_EXT)

    driver.implicitly_wait(10)

def click_by_xpath(driver, path, activity, scrn=None):
    driver.implicitly_wait(10)
    btn = find_element_by_xpath(elements_path.get(path), driver)
    btn.click()
    x = driver.wait_activity(list_activity.get(activity), 10)

    if not x:
        print('not in' + activity)

    time.sleep(5)

    if scrn is True:
         driver.save_screenshot(directory + activity + F_EXT)

    driver.implicitly_wait(10)

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