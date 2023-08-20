import requests
import json


def put_v1_account_password():
    """
    Change registered user password
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/password"

    payload = {
        "login": "cillum culpa labore ullamco",
        "token": "c3ff00bb-76f4-5c6b-5438-32a3ec94cbd1",
        "oldPassword": "occaecat",
        "newPassword": "Excepteur cupidatat id"
    }
    headers = {
        'X-Dm-Auth-Token': 'ut velit',
        'X-Dm-Bb-Render-Mode': 'ut velit',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )

    return response
