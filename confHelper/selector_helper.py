"""This file stores selectors"""
APP_PREFIX = "kg.o.nurtelecom:id/"

def find_element_by_id(el_id, driver):
    return driver.find_element_by_id(f"{APP_PREFIX}{el_id}")