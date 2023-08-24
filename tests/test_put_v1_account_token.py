from services.dm_api_account import DmApiAccount
import requests


def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    response = api.account.put_v1_account_token()
    print(response)
