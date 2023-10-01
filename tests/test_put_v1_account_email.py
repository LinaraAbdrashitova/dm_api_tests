from services.dm_api_account import Facade
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole, Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = Facade(host='http://5.63.153.31:5051')
    login = "email_tes505"
    email = "email_tes505@mail.ru"
    password = "email_tet505"
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    response = api.account.change_registered_user_email(login=login,email="new_" + email, password=password)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.GUEST, UserRole.PLAYER],
            "rating": Rating(enabled=True, quality=0, quantity=0)
        }
    ))
