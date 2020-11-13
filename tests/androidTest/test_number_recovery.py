
from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import *


@allure.epic("Epic #4 - Модуль Восстановления номера")
@allure.feature("Feature #1 - Восстановление номера")
@allure.severity(allure.severity_level.BLOCKER)
class Test_number_recovery(capsAnroid):
    @allure.story("Story #1 - восстановление номера")
    @allure.title("Тест восстановления номера")
    @allure.description("Проверка работоспособности подачи заявки")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_full_number_recovery(self, driverAndroid):
        with allure.step("Открыли не авторизованное приложение"):
            screenshot(driverAndroid, sleep=True)
        with allure.step("Step 1 нажимаем на кнопку восстановть номер"):
            click_by_id(driverAndroid,"btn_phone_recovery", sleep=True, scrn=True)
        with allure.step("Step 2 нажимаем на кнопку начать восстановление"):
            click_by_id(driverAndroid, "check_phone_recovery", sleep=True, scrn=True)
        with allure.step("Step 3 вводим номер"):
            send_keys_by_id(driverAndroid, "input_number", "996502583012", scrn=True)
        with allure.step("Step 4 нажимаем на кнопку проверить номер"):
            click_by_id(driverAndroid, "checking_number", sleep=True, scrn=True)
        with allure.step("Step 5 вводим фамилию"):
            send_keys_by_xpath(driverAndroid, "input_surname", "Сатылганова", sleep=True, scrn=True)
        with allure.step("Step 6 вводим имя"):
            send_keys_by_xpath(driverAndroid, "input_name", "Асель", sleep=None, scrn=True)
        with allure.step("Step 7 нажимаем на кнопку далее"):
            click_by_id(driverAndroid, "button_next", sleep=True, scrn=True)
        with allure.step("Step 8 вводим ICCID"):
            send_keys_by_xpath(driverAndroid, "input_iccid", "899960900119795795", sleep=None, scrn=True)
        with allure.step("Step 9 нажимаем на кнопку отправить"):
            click_by_id(driverAndroid, "button_send", sleep=True, scrn=True)
        with allure.step("Step 10 вводим контактный номер"):
            send_keys_by_xpath(driverAndroid, "input_contact_number", "+996700000176", sleep=None, scrn=True)
        with allure.step("Step 11 нажимаем на кнопку далее"):
            click_by_id(driverAndroid, "button_next", sleep=True, scrn=True)
        with allure.step("Step 12 читаем условие и нажимаем на кнопку далее"):
            click_by_id(driverAndroid, "button_next", sleep=True, scrn=True)
        with allure.step("Step 13 нажимаем на кнопку фото"):
            click_by_id(driverAndroid, "button_shot", sleep=True, scrn=True)
        #     нужна проверка видимости фото
        with allure.step("Step 14 нажимаем на кнопку да видны"):
            click_by_id(driverAndroid, "button_confirm", sleep=True, scrn=True)
        with allure.step("Step 15 читаем условие и нажимаем на кнопку далее"):
            click_by_id(driverAndroid, "button_next", sleep=True, scrn=True)
        with allure.step("Step 16 нажимаем на кнопку фото"):
            click_by_id(driverAndroid, "button_shot", sleep=True, scrn=True)
        #     нужна проверка видимости фото
        with allure.step("Step 17 нажимаем на кнопку да видны"):
            click_by_id(driverAndroid, "button_confirm", sleep=True, scrn=True)
        with allure.step("Step 18 читаем условие и нажимаем на кнопку далее"):
            click_by_id(driverAndroid, "button_next", sleep=True, scrn=True)
        with allure.step("Step 19 нажимаем на кнопку фото"):
            click_by_id(driverAndroid, "button_shot", sleep=True, scrn=True)
        #     нужна проверка видимости фото
        with allure.step("Step 20 нажимаем на кнопку да видны"):
            click_by_id(driverAndroid, "button_confirm", sleep=True, scrn=True)
        with allure.step("Step 21 читаем условие и нажимаем на кнопку далее"):
            click_by_id(driverAndroid, "button_next", sleep=True, scrn=True)
        with allure.step("Step 22 нажимаем на кнопку фото"):
            click_by_id(driverAndroid, "button_shot", sleep=True, scrn=True)
        #     нужна проверка видимости фото
        with allure.step("Step 23 нажимаем на кнопку да видны"):
            click_by_id(driverAndroid, "button_confirm", sleep=True, scrn=True)
        with allure.step("Step 24 нажимаем на кнопку отправить заявку"):
            click_by_id(driverAndroid, "button_next", sleep=True, scrn=True)


