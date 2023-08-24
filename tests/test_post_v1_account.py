import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
            "login": "email_test001",
            "email": "email_test001@mail.ru",
            "password": "email_test001"
        }
    api.account.post_v1_account(json=json)
    response = api.account.put_v1_account_token()
    print(response)