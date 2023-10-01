from services.dm_api_account import Facade
from generic.helpers.mailhog import MailhogApi
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
    api = Facade(host='http://5.63.153.31:5051')
    api.login.login_user(login="email_tes470", password="email_tet470", remember_me=True)
