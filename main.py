from logic.util import *
from logic.webdriver import *
from logic.login import *
from logic.logs import *
from logic.navigation import *
from logic.dates import *
from logic.download import *
from logic.process import *
from logic.send_email import *

def uss():
    try:
        driver = initialize_webdriver(URL)
        log(driver, USER_XPATH, PASSWORD_XPATH, LOGIN_XPATH, USER, PASSWORD)
        nav_without_service(driver, REVIEW_XPATH, CALL_REPORTS, CALL_DETAIL_REPORT, CALL_CENTER, REPORT_FORMAT)

        time.sleep(1)
        add_dates(driver, FROM_DATE_ID)
        add_dates(driver, TO_DATE_ID)

        time.sleep(1)
        down(driver, GENERATE_CLASS)
        time.sleep(10)


        reporting(FILE_OUTPUT_USS, FILE_NAME)
        apply_filters_to_excel(FILE_OUTPUT_USS)
        send(FILE_OUTPUT_USS, SUBJECT_USS, FILE_NAME_USS)
        remove_file(FILE_NAME)

    finally:
        driver.quit()

def air():
    try:
        driver = initialize_webdriver(URL)
        log(driver, USER_XPATH, PASSWORD_XPATH, LOGIN_XPATH, USER, PASSWORD)
        nav_with_service(driver, REVIEW_XPATH, CALL_REPORTS, CALL_DETAIL_REPORT, CALL_CENTER, REPORT_FORMAT, SERVICE_FORMAT, REPORT_FORMAT_KEY_AIR, CALL_CENTER_KEY_AIR, SERVICE_FORMAT_KEY_AIR)

        time.sleep(1)
        add_dates(driver, FROM_DATE_ID)
        add_dates(driver, TO_DATE_ID)

        time.sleep(1)
        down(driver, GENERATE_CLASS)
        time.sleep(10)


        reporting(FILE_OUTPUT_AIR, FILE_NAME)
        apply_filters_to_excel(FILE_OUTPUT_AIR)
        send(FILE_OUTPUT_AIR, SUBJECT_AIR, FILE_NAME_AIR)
        remove_file(FILE_NAME)

    finally:
        driver.quit()

def kaseya():
    try:
        driver = initialize_webdriver(URL)
        log(driver, USER_XPATH, PASSWORD_XPATH, LOGIN_XPATH, USER, PASSWORD)
        nav_with_service(driver, REVIEW_XPATH, CALL_REPORTS, CALL_DETAIL_REPORT, CALL_CENTER, REPORT_FORMAT, SERVICE_FORMAT, REPORT_FORMAT_KEY_KAS, CALL_CENTER_KEY_KAS, SERVICE_FORMAT_KEY_KAS)

        time.sleep(1)
        add_dates(driver, FROM_DATE_ID)
        add_dates(driver, TO_DATE_ID)

        time.sleep(1)
        down(driver, GENERATE_CLASS)
        time.sleep(10)


        reporting(FILE_OUTPUT_KASEYA, FILE_NAME)
        apply_filters_to_excel(FILE_OUTPUT_KASEYA)
        send(FILE_OUTPUT_KASEYA, SUBJECT_KAS, FILE_NAME_KAS)
        remove_file(FILE_NAME)

    finally:
        driver.quit()

if __name__ == '__main__':
    uss()
    air()
    kaseya()
