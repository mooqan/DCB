import allure

from appium.webdriver.common.touch_action import TouchAction
from confHelper.configHelperIOS.authIOS import Test_authorization
from confHelper.configHelperIOS.configHelperIOS import capsIOS
from confHelper.configHelperIOS.standards import *

# Устройство для тестов на английском языке
# Абонент должен быть юзером НУРа не корпоративным
@allure.epic("Epic #3 - Модуль О!денег в приложении Мой О!")
@allure.feature("Feature #1 - экран О!денег")
@allure.severity(allure.severity_level.BLOCKER)
class Test_main_Odengi(capsIOS):
    @allure.title("Проверка открытия экрана пополнения своего баланса")
    @allure.description("Проверка перехода на экран пополнения в контейнере баланс")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_balance_Replenishment(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран пополнения своего баланса"):
            click_by_xpath(driver, "btn_plus_balance_Odengi", sleep=True, scrn=True)

    @allure.title("Проверка открытия экрана пополнения баланса кошелька")
    @allure.description("Проверка перехода на экран пополнения в контейнере кошелек")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_ewallet_Replenishment(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран пополнения кошелька"):
            click_by_xpath(driver, "btn_plus_wallet_Odengi", sleep=True, scrn=True)

    @allure.title("Проверка открытия экрана О!Бонус")
    @allure.description("Проверка перехода на экран О!Бонусов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_Obonus(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран бонусов"):
            click_by_accessibility_id(driver, "btn_bonus", sleep=True, scrn=True)

    @allure.title("Проверка открытия экрана кредиты")
    @allure.description("Проверка перехода на экран кредитов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_loan(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран кредитов"):
            click_by_accessibility_id(driver, "btn_loan", sleep=True, scrn=True)

    @allure.title("Проверка открытия экрана мои карты")
    @allure.description("Проверка перехода на экран моих карт")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_my_cards(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран мои карты"):
            click_by_accessibility_id(driver, "btn_my_cards", sleep=True, scrn=True)

    @allure.title("Проверка открытия экрана истории платежей")
    @allure.description("Проверка перехода на экран истории платежей")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_my_history_payments(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран история платежей"):
            click_by_accessibility_id(driver, "btn_history_payments", sleep=True, scrn=True)

    @allure.title("Проверка открытия экрана счета и штрафы")
    @allure.description("Проверка перехода на экран счета и штрафы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_bills_and_fines(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран счета и штрафы"):
            click_by_accessibility_id(driver, "btn_bills_and_fines", sleep=True, scrn=True)

    @allure.title("Проверка открытия камеры сканера")
    @allure.description("Проверка открытия камеры сканирования куаров и штрихкодов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Open_scaner_qr(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть камеру сканирования куаров и штрафов"):
            click_by_accessibility_id(driver, "btn_qr", sleep=True, scrn=True)
        with allure.step("Step 4 выдать доступ к камере"):
            click_by_accessibility_id(driver, "btn_accept_camera_alert", sleep=True)

    # Для данной проверки убедиться что в профиле имеются избранные платежи больше четырех
    @allure.title("Проверка перехода на экран всех добавленных избранных")
    @allure.description("Проверка открытия экрана добавленных избранных")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_see_all_favorites(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран всех добавленных избранных"):
            click_by_xpath(driver, "btn_see_all_favorites", sleep=True, scrn=True)

    @allure.title("Проверка перехода на экран поиска по каталога")
    @allure.description("Проверка открытия экрана поиска по каталогу")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_catalog_search(self, driver):
        with allure.step("Step 0 блок авторизации"):
            Test_authorization(driver)
        with allure.step("Step 1 убрать подсказку личного QR"):
            click_by_xpath(driver, "cnt_qr_notif", scrn=True, sleep=True)
        with allure.step("Step 2 перейти на экран О!денег"):
            click_by_accessibility_id(driver, "btn_main_Odengi", sleep=True, scrn=True)
        with allure.step("Step 3 открыть экран поиска по каталогу"):
            click_by_xpath(driver, "directory_search", sleep=True, scrn=True)






