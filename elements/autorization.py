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
    "btn_scanner_cancel":"tv_ok",
    "space_out_cntn":"touch_outside",
    "btn_scanner_course_cancel":"tv_ok",
    "btn_internet": "internet_leftover",
    "btn_outgoing_call": "outgoing_call_leftover",
    "btn_refill": "rl_refill",
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
    "btn_edit_profile":"edit",
    "cnt_email":"profile_email",
    "cnt_name":"profile_name",
    "btn_profile_save":"profile_save",
    "btn_choose_ru_lang":"lang_ru",
    #Dengi
    "btn_o!dengi":"menu_wallet",
    "btn_self_refill":"ic_refill",
    "btn_choose_payment_type":"choose",
    "cnt_amount":"amount",
    "btn_pay":"pay_btn",
    "btn_credit":"credit_repayment",
    "btn_cards":"my_cards",
    "btn_history":"history",
    "btn_fines":"unpaid_bills",
    "btn_qr_scanner":"qr",
    "btn_add_fav":"favoriteCardViewLayout",
    "btn_search_catalog":"tv_clickable",
    #Self_paymaent
    "btn_self_payment_cont":"btn",
    "btn_choose_payment_wallet":"tv_action",
}

elements_path = {
    #auth
    "cnt_phone_pswrd":"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText",
    "btn_cancel_system_secure":"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1]",
    #LK
    "btn_left_menu":"//androidx.drawerlayout.widget.DrawerLayout[@index='0']/android.view.ViewGroup[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.LinearLayout[@index='0']/android.view.ViewGroup[@index='0']/android.view.ViewGroup[@index='0']/android.widget.ImageButton[@index='0']",
    "cnt_last_name":"//android.widget.ScrollView[@index='1']/android.widget.RelativeLayout[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.LinearLayout[@index='2']/android.widget.FrameLayout[@index='0']/android.widget.EditText[@index='0']",
    "btn_choose_language":"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[4]",

    #Dengi
    "btn_ewallet_refill":"//android.widget.FrameLayout[@index='1']/android.view.ViewGroup[@index='0']/android.widget.RelativeLayout[@index='2']",
    "btn_ewallet":"//androidx.recyclerview.widget.RecyclerView[@index='1']/android.view.ViewGroup[@index='0']",
    "btn_mwallet": "//androidx.recyclerview.widget.RecyclerView[@index='1']/android.view.ViewGroup[@index='1']",
    "btn_bcard": "//androidx.recyclerview.widget.RecyclerView[@index='1']/android.view.ViewGroup[@index='2']",
    "btn_side_menu":"//androidx.drawerlayout.widget.DrawerLayout[@index='0']/android.view.ViewGroup[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.LinearLayout[@index='0']/android.view.ViewGroup[@index='0']/android.widget.ImageButton[@index='0']",
    "btn_setings":"//androidx.recyclerview.widget.RecyclerView[@index='0']/androidx.appcompat.widget.LinearLayoutCompat[@index='5']",
    "btn_payment_type_mwallet":"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView",
    "cnt_payment_value":"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText",
    "btn_self_payment_cont1":"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.Button",
    "btn_self_payment_cont2":"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.Button",
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


