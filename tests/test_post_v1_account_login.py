from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.login_credentials_model import LoginCredentials
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole, Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = Registration(
        login="email_test0157",
        email="email_test0157@mail.ru",
        password="email_test0157"
    )
    login_credentials = LoginCredentials(
        login=json.login,
        password=json.password,
        rememberMe=True
    )
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    response = api.login.post_v1_account_login(json=login_credentials, status_code=200)
    assert_that(response.resource, has_properties(
        {"login": json.login,
         "roles": [UserRole.GUEST, UserRole.PLAYER],
         "rating": Rating(enabled=True, quality=0, quantity=0)}
    ))
