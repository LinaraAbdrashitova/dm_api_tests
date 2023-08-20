import requests
import json


def post_v1_account():
    """
    Register new user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account"

    payload = {
        "login": "email_test0",
        "email": "email_test0@mail.ru",
        "password": "email_test0"
    }
    headers = {
        'X-Dm-Auth-Token': 'ut velit',
        'X-Dm-Bb-Render-Mode': 'ut velit',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )

    return response