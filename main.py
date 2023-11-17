from logic.util import *
from logic.webdriver import *
from logic.login import *
from logic.logs import *
from logic.navigation import *
from logic.dates import *
from logic.download import *
from logic.process_uss import *
from logic.process_air import *
from logic.send_email import *

def uss():
    try:
        driver = initialize_webdriver(URL)
        log(driver, USER_XPATH, PASSWORD_XPATH, LOGIN_XPATH, USER, PASSWORD)
        nav_uss(driver, REVIEW_XPATH, CALL_REPORTS, CALL_DETAIL_REPORT, CALL_CENTER, REPORT_FORMAT)

        time.sleep(1)
        add_dates(driver, FROM_DATE_ID)
        add_dates(driver, TO_DATE_ID)

        time.sleep(1)
        down(driver, GENERATE_CLASS)
        time.sleep(10)


        reporting_uss()
        apply_filters_to_excel_uss()
        send_uss()
        remove_file_uss()

    finally:
        driver.quit()

def air():
    try:
        driver = initialize_webdriver(URL)
        log(driver, USER_XPATH, PASSWORD_XPATH, LOGIN_XPATH, USER, PASSWORD)
        nav_air(driver, REVIEW_XPATH, CALL_REPORTS, CALL_DETAIL_REPORT, CALL_CENTER, REPORT_FORMAT, SERVICE_FORMAT)

        time.sleep(1)
        add_dates(driver, FROM_DATE_ID)
        add_dates(driver, TO_DATE_ID)

        time.sleep(1)
        down(driver, GENERATE_CLASS)
        time.sleep(10)


        reporting_air()
        apply_filters_to_excel_air()
        send_air()
        remove_file_air()

    finally:
        driver.quit()

if __name__ == '__main__':
    uss()
    air()
