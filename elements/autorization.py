import os

from confHelper.configHelper import capsAnroid

elements = {
    #auth
    "btn_confirm":"confirm",
    "cnt_phone_number":"phone_number",
    "btn_phone_number_next":"next",
    "cnt_phone_pswrd":"et_password",
    "btn_phone_pswrd_next":"confirm",
    #LK
    "btn_internet": "internet_leftover",
    "btn_outgoing_call": "outgoing_call_leftover",
    "btn_refill": "ic_refill",
    "btn_sub_numbers": "sub_numbers",
    "btn_lottery": "lottery_view",
    "btn_services": "services",
    "btn_tariffs": "tariffs",
    "btn_detalizatation": "detalizatation",
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
    "ServicePaymentActivity":"wallet.ui.payment.service.ServicePaymentActivity",
    "InternetServiceActivity": ".ui.services.group.internet.InternetServiceActivity",
    "CallServiceActivity": ".ui.services.group.call.CallServiceActivity",
    "ManageNumbersActivity": ".ui.manage_numbers.ManageNumbersActivity",
    "LotteryInfoActivity": ".ui.lottery.info.LotteryInfoActivity",
    "ServiceCategoryActivity": ".ui.services.service.category.ServiceCategoryActivity",
    "TariffCategoryActivity": ".ui.services.tariff.category.TariffCategoryActivity",
    "CompleteDetalizationActivity":".ui.detalization.replenish_detalization.CompleteDetalizationActivity",
}


