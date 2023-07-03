import allure


from confHelper.configHelperIOS.authIOS import Test_authorization
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import click_by_accessibility_id, send_keys_by_id, click_by_xpath, send_keys_by_xpath
from elements.elementsIOS import *

@allure.epic("Epic #2")
@allure.feature("Feature #2 - Личный кабинет")
@allure.story("Story #1 - Переходы в личном кабинете")
class Test_lk(capsIOS):
    @allure.title("Тест. Сохранение личного профиля положительный")
    @allure.description("Прохождение флоу переходов в личном кабинете с чистой установкой")
    def test_lk1(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif")
            # click_by_xpath(driver, "btn_cancel_notif", scrn=True, sleep=True)
        with allure.step("Step 2 переход в боковое меню"):
            click_by_xpath(driver, "btn_menu", scrn=True, sleep=True)
        with allure.step("Step 3 переход в редактирование личного профиля"):
            click_by_xpath(driver, "btn_personal_profile", scrn=True, sleep=True)
        with allure.step("Step 4 ввод данных"):
            click_by_xpath(driver, "name_lk", scrn=True, sleep=True)
            name_input = driver.find_element_by_xpath(elements.get("name_lk"))
            name_input.clear()
            name_input.send_keys("MoiO")
        with allure.step("Step 5 сохранение профиля"):
            click_by_xpath(driver, "done", scrn=True, sleep=True)
            click_by_xpath(driver, "back", scrn=True, sleep=True)
