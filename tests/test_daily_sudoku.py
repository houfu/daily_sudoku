from datetime import datetime
from smtplib import SMTP
from unittest.mock import DEFAULT

import pytest

from daily_sudoku import __version__
from daily_sudoku.main import job


def test_version():
    assert __version__ == '0.1.0'


def test_job(requests_mock, mocker):
    now = datetime.now()
    url = f"http://www.dailysudoku.com/sudoku//pdf/{now.year}/{now.strftime('%m')}/{now.strftime('%Y-%m')}-" \
          f"{now.strftime('%e').strip()}_S1_N1.pdf"
    mocker.patch.dict('os.environ', {
        'PRINT_EMAIL': 'test@dest.com',
        'SMTP_SERVER': 'smtp.test.com',
        'SMTP_USER': 'test@source.com',
        'SMTP_PWD': 'PASSWORD'
    })
    requests_mock.get(url, status_code=200, content=b'ABC')
    mocker.patch.multiple(SMTP, starttls=DEFAULT, login=DEFAULT)
    send_message = mocker.patch.object(SMTP, 'send_message')
    job()
    send_message.assert_called()

    send_message.reset_mock()
    with pytest.raises(Exception):
        requests_mock.get(url, status_code=404, content='ABC')
        job()
    send_message.assert_not_called()
