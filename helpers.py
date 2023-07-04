import os
import allure

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def take_screenshot_and_logcat(driver, device_logger, calling_request):
    logcat_dir = device_logger.logcat_dir
    logcat_file_path = os.path.join(logcat_dir, calling_request + "_logcat.log")
    logcat_file = open(logcat_file_path, 'wb')
    logcat_data = driver.get_log('logcat')

    # Фильтруем логи и записываем только действия приложения
    app_actions = ["OkHttp", "kg.dcb.mobilebanking.debug", "ACTION_3"]

    for data in logcat_data:
        message = data['message']
        for action in app_actions:
            if action in message:
                data_string = f"Timestamp: {data['timestamp']}\nMessage: {message}"
                logcat_file.write((data_string + '\n').encode("UTF-8"))
                break

    logcat_file.close()
    allure.attach.file(logcat_file_path, "LogAndroid", allure.attachment_type.JSON)


