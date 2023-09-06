from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
            "login": "email_test0041",
            "email": "email_test0041@mail.ru",
            "password": "email_test0041"
        }
    login_credentials = {
        "login": json["login"],
        "password": json["password"],
        "rememberMe": True
    }
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Статус код ответа должен быть равен 201, но он равен {response.status_code}"
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    response = api.login.post_v1_account_login(json=login_credentials)
    print()
    assert response.status_code == 200, f"Статус код ответа должен быть равен 200, но он равен {response.status_code}"

