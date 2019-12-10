""" Standart test cases"""
from selenium.webdriver.support.wait import WebDriverWait

from confHelper.selector_helper import find_element_by_id
from elements.autorization import elements, list_activity
import time


directory = '/Users/ripvantesla/PycharmProjects/sample-code/sample-code/examples/python/pytest/results/appiumscr/'
file_name = 'screenshot.png'
F_EXT = ".png"

def click_by_id(driver, id, activity):
    driver.implicitly_wait(10)
    btn = find_element_by_id(elements.get(id), driver)
    btn.click()
    driver.wait_activity(list_activity.get(activity), 10)
    time.sleep(5)
    driver.save_screenshot(directory + activity + F_EXT)
    driver.implicitly_wait(10)

def send_keys_by_id(driver, id, activity, key):
    driver.implicitly_wait(10)
    btn_outgoing_call = find_element_by_id(elements.get(id), driver)
    btn_outgoing_call.send_keys(key)
    driver.wait_activity(list_activity.get(activity), 10)
    time.sleep(5)
    driver.save_screenshot(directory + activity + F_EXT)
    driver.implicitly_wait(10)
