#  Copyright MIT License (c) 2020. Ang Hou Fu

import os
from datetime import datetime
from email.message import EmailMessage
import time
from smtplib import SMTP

import requests
import schedule


def job():
    now = datetime.now()
    r = requests.get(
        f"http://www.dailysudoku.com/sudoku//pdf/{now.year}/"
        f"{now.strftime('%m')}/{now.strftime('%Y-%m-%d')}_S1_N1.pdf",
        timeout=5)
    print(f'{datetime.now()}: Getting daily sudoku: {r.url}')
    if r.status_code != 404:
        msg = EmailMessage()
        msg['To'] = print_email
        msg['From'] = smtp_user
        msg['Subject'] = 'Daily sudoku'
        msg.add_attachment(r.content, maintype='application', subtype='pdf', filename='sudoku.pdf')
        with SMTP(smtp_server, 587) as s:
            s.starttls()
            s.login(smtp_user, smtp_password)
            s.send_message(msg)
        print(f'{datetime.now()}: Finished job sending to {print_email}.')
    else:
        raise Exception(f'{datetime.now()}: Daily sudoku returned 404.')


# if 'PRINTER_HOST' in os.environ:
print_email = os.environ.get('PRINT_EMAIL')
smtp_server = os.environ.get('SMTP_SERVER')
smtp_user = os.environ.get('SMTP_USER')
smtp_password = os.environ.get('SMTP_PWD')

if __name__ == '__main__':
    schedule.every().day.at("09:25").do(job_func=job)
    while True:
        print(f'{datetime.now()}: Running pending jobs.')
        schedule.run_pending()
        time.sleep(10800)
