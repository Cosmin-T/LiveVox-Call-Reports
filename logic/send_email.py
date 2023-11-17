import smtplib
from datetime import datetime
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from logic.util import *
import logging
from logic.logs import *

conf_log()

def send_uss():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f'USS Phone Invalid Report - {yesterday}'

    body = f'Please check the daily LiveVox date check for {yesterday} at: \n{URL}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        with open(FILE_OUTPUT_USS, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='txt')
            attachment.add_header('content-Disposition', 'attachment', filename='USS Phone Invalid Report.xlsx')
            msg.attach(attachment)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
            logging.info("Email sent successfully!")

    except Exception as e:
        logging.error(f'Exception: {e}')

def send_air():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f'Airprax-Airgas Phone Invalid Report - {yesterday}'

    body = f'Please check the daily LiveVox date check for {yesterday} at: \n{URL}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        with open(FILE_OUTPUT_AIR, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='txt')
            attachment.add_header('content-Disposition', 'attachment', filename='Airprax-Airgas Phone Invalid Report.xlsx')
            msg.attach(attachment)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
            logging.info("Email sent successfully!")

    except Exception as e:
        logging.error(f'Exception: {e}')