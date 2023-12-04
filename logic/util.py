from logic.config_ini import *
import logging

config = con()

# webdriver
URL = config['DEFAULT']['URL']
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
FILE_NAME = config['DEFAULT']['FILE_NAME']
FILE_OUTPUT_USS = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report/USS Phone Invalid Report.xlsx'
FILE_OUTPUT_AIR = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report/Airgas-Airprax Phone Invalid Report.xlsx'
FILE_OUTPUT_KASEYA = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report/Kaseya Phone Invalid Report.xlsx'
FOLDER_PATH = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report'
OUTLOOK_TEMPLATE = config['DEFAULT']['OUTLOOK_TEMPLATE']

# nav keys without service
CALL_CENTER_KEY_USS = ''
REPORT_FORMAT_KEY_USS = ''

# nav keys with service
REPORT_FORMAT_KEY_AIR = 'Dragon 3P (3062852)'
CALL_CENTER_KEY_AIR = 'AGA_RETURN'
SERVICE_FORMAT_KEY_AIR = 'AIRPRAX_HCI_CLICKER (3179862)'

REPORT_FORMAT_KEY_KAS = 'KASAYA (3063659)'
CALL_CENTER_KEY_KAS = 'AGA_RETURN'
SERVICE_FORMAT_KEY_KAS = 'KASAYA_HCI_CLICKER (3183055)'

# email sending
SUBJECT_USS = 'USS Phone Invalid Report'
FILE_NAME_USS = 'USS Phone Invalid Report.xlsx'
SUBJECT_AIR = 'Airprax-Airgas Phone Invalid Report'
FILE_NAME_AIR = 'Airprax-Airgas Phone Invalid Report.xlsx'
SUBJECT_KAS = 'Kaseya Phone Invalid Report'
FILE_NAME_KAS = 'Kaseya Phone Invalid Report.xlsx'

SENDER_EMAIL = config['DEFAULT']['SENDER_EMAIL']
RECEIVER_EMAIL = config['DEFAULT']['RECEIVER_EMAIL']
GMAIL_APP_PASSWORD = config['DEFAULT']['GMAIL_APP_PASSWORD']

# logging
LOG_OUTPUT = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_call_report/log.txt'
LOG_LEVEL = logging.INFO