from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from logic.logs import *
import time

conf_log()

def down(driver, generate_class):

    try:
        download = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, generate_class)))
        download.click()
        logging.info(f'TXT file downloaded succesfully')
    except Exception as e:
        logging.error(f'Error: {e}')


