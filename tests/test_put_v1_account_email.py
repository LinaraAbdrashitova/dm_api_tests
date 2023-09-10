import requests
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.change_email_model import ChangeEmailModel
from dm_api_account.models.registration_model import RegistrationModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = RegistrationModel(
        login="email_test52",
        email="email_test52@mail.ru",
        password="email_test52"
    )
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Статус код ответа должен быть равен 201, но он равен {response.status_code}"
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    new_json = ChangeEmailModel(
        login=json.login,
        email='new_' + json.email,
        password=json.password
    )
    response = api.account.put_v1_account_email(json=new_json)
