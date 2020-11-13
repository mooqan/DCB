from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import *


@allure.epic("Epic #5 - Ночные работы")
@allure.feature("Ночное обновление backand")
@allure.severity(allure.severity_level.BLOCKER)
class Test_night_update(capsAnroid):
    @allure.story("Story #1 - Проверка сохранения сессии")
    @allure.title("Проверка сохранения сессии")
    @allure.description("Проверка сохранения сессии и отсутствия потерь данных")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_night_update_full(self, driverAndroid):
        with allure.step("Step #1 В открытом приложении обновляем О!Деньги"):
            swipe(driverAndroid, sleep=True, scrn=True)
        with allure.step("Step #2 Переходим в раздел Мои карты"):
            click_by_xpath(driverAndroid, "btn_my_cards", sleep=True, scrn=True)
            driverAndroid.back()
        with allure.step("Step #3 Переход в раздел Быстрые платежи"):
            click_by_xpath(driverAndroid, "btn_fast_payments", sleep=True, scrn=True)
            driverAndroid.back()
        with allure.step("Step #4 переход в раздел Истории"):
            click_by_xpath(driverAndroid, "btn_history_xpath", sleep=True, scrn=True)
            driverAndroid.back()

    @allure.story("Story #2 - Проверка оплаты с баланса")
    @allure.title("Проверка работы оплаты с баланса")
    @allure.description("Проверка работы платежей с баланса")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_night_update_balance_payment(self, driverAndroid):
        with allure.step("Step #1 Переход к оплате мобильных операторов"):
            click_by_xpath(driverAndroid, "btn_number_replenishment", sleep=True, scrn=True)
        with allure.step("Step #2 Вводим номер"):
            send_keys_by_id(driverAndroid, "input_mobile_number", "996702243851", sleep=True, scrn=True)
        with allure.step("Step #3 Нажимаем далее"):
            click_by_id(driverAndroid, "btn_next", sleep=True, scrn=True)
        with allure.step("Step #4 Выбираем метод платежа"):
            click_by_xpath(driverAndroid, "btn_type_wallet", sleep=True, scrn=False)
            click_by_xpath(driverAndroid, "btn_payment_type_mwallet", sleep=True, scrn=True)
        with allure.step("Step #5 Ввод суммы"):
            send_keys_by_id(driverAndroid, "cnt_payment_value", "5", sleep=True, scrn=True)
        with allure.step("Step #6 Нажимаем продолжить"):
            click_by_id(driverAndroid, "btn_next", sleep=True, scrn=True)
        with allure.step("Step #7 Подтверждаем оплату"):
            click_by_xpath(driverAndroid, "btn_pay", sleep=True, scrn=True)
        with allure.step("Step #8 Переходим в О!деньги"):
            click_by_id(driverAndroid, "btn_open_main", sleep=True, scrn=True)
        with allure.step("Step #7 Переходим в историю"):
            click_by_id(driverAndroid, "btn_history", sleep=True, scrn=True)
            driverAndroid.back()

    @allure.story("Story #3 - Проверка оплаты с кошелька")
    @allure.title("Проверка работы оплаты с кошелька")
    @allure.description("Проверка работы платежей с кошелька")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_night_update_ewallet_payment(self, driverAndroid):
        with allure.step("Step #1 Переход к разделу кошельки и банки"):
            click_by_xpath(driverAndroid, "btn_catalog_category_wallets", sleep=True, scrn=True)
        with allure.step("Step #2 Открываем сервис пополнения кошелька"):
            click_by_xpath(driverAndroid, "btn_wallet_O!", sleep=True, scrn=True)
        with allure.step("Step #3 Вводим номер"):
            click_by_xpath(driverAndroid, "btn_favorites", sleep=True, scrn=True)
        with allure.step("Step #4 Нажимаем далее"):
            click_by_id(driverAndroid, "btn_next", sleep=True, scrn=True)
        with allure.step("Step #5 Выбираем метод платежа"):
            click_by_xpath(driverAndroid, "btn_type_wallet", sleep=True, scrn=False)
            click_by_xpath(driverAndroid, "btn_payment_type_ewallet", sleep=True, scrn=True)
        with allure.step("Step #6 Ввод суммы"):
            send_keys_by_id(driverAndroid, "cnt_payment_value", "5", sleep=True, scrn=True)
        with allure.step("Step #7 Нажимаем продолжить"):
            click_by_id(driverAndroid, "btn_next", sleep=True, scrn=True)
        with allure.step("Step #8 Подтверждаем оплату"):
            click_by_xpath(driverAndroid, "btn_pay", sleep=True, scrn=True)
        with allure.step("Step #9 Переходим в О!деньги"):
            click_by_id(driverAndroid, "btn_open_main", sleep=True, scrn=True)
        with allure.step("Step #10 Переходим в историю"):
            click_by_id(driverAndroid, "btn_history", sleep=True, scrn=True)
            driverAndroid.back()