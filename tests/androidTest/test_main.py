from tests.androidTest.test_authorization import *
from tests.androidTest.test_lk import *
from tests.androidTest.test_omoney import *
from tests.androidTest.test_number_recovery import *
from tests.androidTest.test_night_update import *


class Test_main1(capsAnroid):
    Test_number_recovery()
    Test_lk()
    Test_auth()
    Test_OMoney()
    Test_left_menu()
    Test_night_update()
