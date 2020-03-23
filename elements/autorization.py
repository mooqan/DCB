import os

from confHelper.configHelper import capsAnroid

elements = {
    #auth
    "btn_confirm":"confirm",
    "cnt_phone_number":"et_input",
    "btn_phone_number_next":"btn",
    "cnt_phone_pswrd":"et_input",
    "btn_phone_pswrd_next":"btn",
    #LK
    "btn_internet": "internet_leftover",
    "btn_outgoing_call": "outgoing_call_leftover",
    "btn_refill": "ic_refill",
    "btn_sub_numbers": "sub_numbers",
    "btn_lottery": "lottery_view",
    "btn_services": "services",
    "btn_tariffs": "tariffs",
    "btn_detalizatation": "detalizatation",
    "cnt_searh_bar":"search_src_text",
    "btn_settings_lang":"settingsLang",
    "btn_ru_lang":"lang_ru",
    "btn_ok":"button1",
    "btn_container":"tv_title",
    #Dengi
    "btn_o!dengi":"menu_wallet",
    "btn_self_refill":"ic_refill",
    "btn_choose_payment_type":"choose",
    "cnt_amount":"amount",
    "btn_pay":"pay_btn",
}

elements_path = {
    #auth
    #LK
    #Dengi
    "btn_ewallet":"//androidx.recyclerview.widget.RecyclerView[@index='1']/android.view.ViewGroup[@index='0']",
    "btn_mwallet": "//androidx.recyclerview.widget.RecyclerView[@index='1']/android.view.ViewGroup[@index='1']",
    "btn_bcard": "//androidx.recyclerview.widget.RecyclerView[@index='1']/android.view.ViewGroup[@index='2']",
    "btn_side_menu":"//androidx.drawerlayout.widget.DrawerLayout[@index='0']/android.view.ViewGroup[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.LinearLayout[@index='0']/android.view.ViewGroup[@index='0']/android.widget.ImageButton[@index='0']",
    "btn_setings":"//androidx.recyclerview.widget.RecyclerView[@index='0']/androidx.appcompat.widget.LinearLayoutCompat[@index='5']",

}

# elements_lk = {
#     "btn_internet":"internet_leftover",
#     "btn_outgoing_call":"outgoing_call_leftover",
#     "btn_refill":"ic_refill",
#     "btn_sub_numbers":"sub_numbers",
#     "btn_lottery":"lottery_view",
#     "btn_services":"services",
#     "btn_tariffs":"tariffs",
#     "btn_detalizatation":"detalizatation",
# }

list_activity = {
    "LoginByPasswordActivity":".ui.auth.login.password.LoginByPasswordActivity",
    "UseConditionConfirmActivity":".ui.auth.conditions_confirm.UseConditionConfirmActivity",
    "PhoneNumberExistenceCheckActivity":".ui.auth.existence_check.PhoneNumberExistenceCheckActivity",
    "InternetServiceActivity": ".ui.services.group.internet.InternetServiceActivity",
    "CallServiceActivity": ".ui.services.group.call.CallServiceActivity",
    "ManageNumbersActivity": ".ui.manage_numbers.ManageNumbersActivity",
    "LotteryInfoActivity": ".ui.lottery.info.LotteryInfoActivity",
    "ServiceCategoryActivity": ".ui.services.service.category.ServiceCategoryActivity",
    "TariffCategoryActivity": ".ui.services.tariff.category.TariffCategoryActivity",
    "CompleteDetalizationActivity":".ui.detalization.replenish_detalization.CompleteDetalizationActivity",
    #Dengi
    "GettingWalletStatusActivity":"wallet.ui.account.getting_wallet_status.GettingWalletStatusActivity",
    "ServicePaymentActivity":"wallet.ui.payment.service.ServicePaymentActivity",
    "ChoosePaymentTypeActivity":"wallet.ui.payment.type.ChoosePaymentTypeActivity",
    "ReplenishmentConfirmationActivity":"wallet.ui.replenish.confirmation.ReplenishmentConfirmationActivity",
}


