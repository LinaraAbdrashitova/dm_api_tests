from collections import namedtuple
from datetime import datetime
import time
import pytest

from helpers.account_helper import AccountHelper
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
            sort_keys=True
        )
    ]
)


@pytest.fixture(scope='session')
def mailhog_api():
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    mailhog_client = MailHogApi(configuration=mailhog_configuration)
    return mailhog_client


@pytest.fixture(scope='session')
def account_api():
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_api_configuration)
    return account


@pytest.fixture(scope='session')
def account_helper(account_api, mailhog_api):
    account_helper = AccountHelper(dm_account_api=account_api, mailhog=mailhog_api)
    return account_helper


@pytest.fixture(scope='function')
def auth_account_helper(mailhog_api):
    # dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    # account = DMApiAccount(configuration=dm_api_configuration)
    # account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog_api)
    # login = prepare_user.login
    # password = prepare_user.password
    # email = prepare_user.email
    # account_helper.register_new_user(
    #     login=login,
    #     email=email,
    #     password=password
    # )
    # account_helper.user_login(login=login, password=password)
    # account_helper.auth_client(
    #     login=login,
    #     password=password
    # )
    # return account_helper

    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_api_configuration)
    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog_api)
    account_helper.auth_client(
        login="linara_27_01_2025_13_05_15",
        password="123456789"
    )
    return account_helper


@pytest.fixture
def prepare_user():
    time.sleep(1)
    now = datetime.now()
    data = now.strftime("%d_%m_%Y_%H_%M_%S")
    login = f'linara_{data}'
    email = f'{login}@mail.ru'
    password = '123456789'
    User = namedtuple("User", ["login", "password", "email"])
    user = User(login=login, password=password, email=email)
    return user
