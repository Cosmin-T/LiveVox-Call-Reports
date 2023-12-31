# navigation.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
from logic.util import *
import logging
from logic.logs import *
from logic.dates import *

conf_log()

def nav_without_service(driver, review_xpath, call_reports, call_detail_report, call_center, report_format, call_center_key, report_format_key):
    try:

        navigator_list = [
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, review_xpath))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, call_reports))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, call_detail_report))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, call_center))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, report_format))),
        ]

        for i, nav_func in enumerate(navigator_list):
            element = nav_func()
            element.click()

            if i == 3:
                call_center_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, call_center)))
                call_center_input.send_keys(call_center_key + Keys.ENTER)

            if i == 4:
                report_format_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, report_format)))
                report_format_input.send_keys(report_format_key + Keys.ENTER)

        if nav_func():
            print_list = ['Clicked Review', 'Clicked Call Reports', 'Clicked CDR', 'USS Selected', 'Format Selected', 'From Date added', 'End Date added']
            for prnt in print_list:
                logging.info(prnt)
        else:
            logging.error(f'Error clicking: {prnt}')

    except Exception as e:
        logging.error(f'Error: {e}')


def nav_with_service(driver, review_xpath, call_reports, call_detail_report, call_center, report_format, service_format, call_center_key, report_format_key, service_format_key):
    try:

        navigator_list = [
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, review_xpath))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, call_reports))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, call_detail_report))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, call_center))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, report_format))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, service_format))),
        ]

        for i, nav_func in enumerate(navigator_list):
            element = nav_func()
            element.click()

            if i == 3:
                call_center_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, call_center)))
                call_center_input.send_keys(call_center_key + Keys.ENTER)

            if i == 4:
                report_format_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, report_format)))
                report_format_input.send_keys(report_format_key + Keys.ENTER)

            if i == 5:
                service_format_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, service_format)))
                service_format_input.send_keys(service_format_key + Keys.ENTER)


        if nav_func():
            print_list = ['Clicked Review', 'Clicked Call Reports', 'Clicked CDR', call_center + 'Selected', 'Service Selected', 'From Date added', 'End Date added']
            for prnt in print_list:
                logging.info(prnt)
        else:
            logging.error(f'Error clicking: {prnt}')

    except Exception as e:
        logging.error(f'Error: {e}')