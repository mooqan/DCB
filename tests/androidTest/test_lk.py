from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import *
from confHelper.configHelperAndroid.authAndroid import Test_authorization
import pytest


@allure.epic("Epic #2 - Модуль Личного кабинета О!")
@allure.feature("Feature #1 - Личный кабинет")
@allure.severity(allure.severity_level.CRITICAL)
class Test_lk(capsAnroid):
    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода на пополнение баланса")
    @allure.description("Проверка работоспособности перехода на пополнение баланса")
    def test_balance_replenishment(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Проверка перехода на пополнение мобильного баланса"):
            click_by_id(driverAndroid, "btn_refill", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода на окно доступного интернета")
    @allure.description("Проверка работоспособности переход на окно доступного интернета")
    def test_accessible_internet(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #2 Проверка перехода в окно доступного интернет трафика"):
            click_by_id(driverAndroid, "btn_internet", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода на окно доступного трафика билинга")
    @allure.description("Проверка работоспособности переход на окно доступного интернета")
    def test_available_traffic(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #2 Проверка перехода в окно доступного трафика билинга"):
            click_by_id(driverAndroid, "btn_outgoing_call", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода в окно 'Мои номера'")
    @allure.description("Проверка работоспособности переход в окно 'Мои номера'")
    def test_my_numbers(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Переход в окно 'Мои номера'"):
            click_by_id(driverAndroid, "btn_sub_numbers", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода в окно 'Saima Telecom'")
    @allure.description("Проверка работоспособности переход в окно 'Saima Telecom'")
    def test_saima(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Переход в окно 'Saima Telecom'"):
            click_by_id(driverAndroid, "btn_saima", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода в окно 'Saima Telecom' абонентом других операторов")
    @allure.description("Проверка работоспособности переход в окно 'Saima Telecom' абонентом других операторов")
    @pytest.mark.skip(reason="не требуется") # очень не стабильный тест
    def test_not_nur_saima(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении другим оператором"):
            Test_authorization(driverAndroid, "+996 777 395 669", "Test12345", qr=False)
        with allure.step("Step #1 Переход в окно 'Saima Telecom'"):
            time.sleep(5)
            driverAndroid.back()
            click_by_id(driverAndroid, "btn_saima", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода в окно 'Стань абонентом О!'")
    @allure.description("Проверка работоспособности переход в окно 'Стань абонентом О!' бронирования номера")
    @pytest.mark.skip(reason="не требуется") # очень не стабильный тест
    def test_get_number(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 777 395 669", "Test12345", qr=False)
        with allure.step("Step #1 Переход в окно 'Стань абонентом О!'"):
            time.sleep(5)
            driverAndroid.back()
            click_by_id(driverAndroid, "btn_get_number", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода в окно 'Выбрать номер'")
    @allure.description("Проверка работоспособности переход в окно 'Выбрать номер'")
    @pytest.mark.skip(reason="не требуется") # очень не стабильный тест
    def test_get_other_number(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 777 395 669", "Test12345", qr=False)
        with allure.step("Step #1 Переход в окно 'Выбрать номер'"):
            time.sleep(5)
            driverAndroid.back()
            click_by_id(driverAndroid, "btn_get_other_number", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода в окно 'Тарифы'")
    @allure.description("Проверка работоспособности переход в окно 'Тарифы'")
    def test_tariffs(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Переход в окно 'Тарифы'"):
            click_by_id(driverAndroid, "btn_tariffs", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода в окно 'Сервисы'")
    @allure.description("Проверка работоспособности переход в окно 'Сервисы'")
    def test_services(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Переход в окно 'Сервисы'"):
            click_by_id(driverAndroid, "btn_services", scrn=True, sleep=True)

    @allure.story("Story #1 - Главная страница Личного кабинета")
    @allure.title("Тест перехода в окно 'Детализация'")
    @allure.description("Проверка работоспособности переход в окно 'Детализация'")
    def test_detail(self, driverAndroid):
        with allure.step("Step #0 Авторизация в приложении"):
            Test_authorization(driverAndroid, "+996 702 242 508", "Test12345")
        with allure.step("Step #1 Переход в окно 'Детализация'"):
            # TouchAction(driverAndroid).press(x=478, y=1612).move_to(x=503, y=895).release().perform()
            click_by_id(driverAndroid, "btn_detalizatation", scrn=True, sleep=True)