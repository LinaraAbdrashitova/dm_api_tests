import requests


def put_v1_account_token():
    """
    Activate register user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/urn:uuid:b8633334-db95-5585-88de-204d1f4a74c3"

    headers = {
        'X-Dm-Auth-Token': 'ut velit',
        'X-Dm-Bb-Render-Mode': 'ut velit',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers
    )

    return response
