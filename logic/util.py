from logic.config_ini import *
import logging

config = con()

# webdriver
URL = 'https://portal.na6.livevox.com/login/auth/BII_1?url=https%3A%2F%2Fportal.na6.livevox.com%2FBII_1%23configure%2FftpBrowser'
CROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

# login
USER = config['DEFAULT']['USER']
USER_XPATH = '//*[@id="username"]'
PASSWORD = config['DEFAULT']['PASSWORD']
PASSWORD_XPATH = '//*[@id="password"]'
LOGIN_XPATH = '//*[@id="loginBtn"]/span'

# naviation_uss
REVIEW_XPATH = '//*[@id="lv-app"]/div/div/div/aside/div/div/div[2]/ul/button[3]'
CALL_REPORTS = '//*[@id="callReports"]/div/div[2]/div'
CALL_DETAIL_REPORT = '//*[@id="1"]/div/div[2]/div'
CALL_CENTER = '//*[@id="callcenter_combo"]'
REPORT_FORMAT = '//*[@id="report_format_combo"]'
FROM_DATE_ID = 'search-panel__start-date'
TO_DATE_ID = 'search-panel__end-date'
GENERATE_CLASS = 'lv-button__inside'

# navigation_airgass_airprax
SERVICE_FORMAT = '//*[@id="service_combo"]'


# pandas
FILE_NAME = '/Users/cosmint/Downloads/BII_1_*'
FILE_OUTPUT_USS = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report/USS Phone Invalid Report.xlsx'
FILE_OUTPUT_AIR = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report/Airgas-Airprax Phone Invalid Report.xlsx'
FOLDER_PATH = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report'
OUTLOOK_TEMPLATE = '/Users/cosmint/Documents/Work/Outlook Templates'

# email sending
SENDER_EMAIL = "jamroack@gmail.com"
RECEIVER_EMAIL = "cosmin.turculeanu@dandsltd.com"
GMAIL_APP_PASSWORD = config['DEFAULT']['GMAIL_APP_PASSWORD']


# logging
LOG_OUTPUT = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report/log.txt'
LOG_LEVEL = logging.INFO