import requests


def delete_v1_account_login_all():
    """
    Logout from every device
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login/all"

    headers = {
        'X-Dm-Auth-Token': 'ut velit',
        'X-Dm-Bb-Render-Mode': 'ut velit',
        'Accept': 'text/plain'
    }

    response = requests.request(
        mehtod="DELETE",
        url=url,
        headers=headers
    )

    return response
