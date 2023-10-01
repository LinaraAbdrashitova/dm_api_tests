from services.dm_api_account import Facade
from generic.helpers.mailhog import MailhogApi
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole, Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

def test_put_v1_account_token():
    api = Facade(host='http://5.63.153.31:5051')
    login = "email_tes508"
    password = "email_tes508"
    email = "email_tes508@mail.ru"
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    # активация пользователя
    response = api.account.activate_registered_user(login=login)
    assert_that(response.resource, has_properties(
        {
            "login": "email_tes508",
            "roles": [UserRole.GUEST, UserRole.PLAYER],
            "rating": Rating(enabled=True, quality=0, quantity=0)
        }
    ))




    # actual_json = json.loads(response.json(by_alias=True, exclude_none=True))
    # expected_json = {
    #     "resource":
    #         {
    #             "login": "email_tes54",
    #             "rating": {
    #                 "quality": 0,
    #                 "quantity": 0,
    #                 "enabled": True
    #             },
    #             "roles": [
    #                 "Guest",
    #                 "Player"
    #             ]
    #         }
    # }
    # assert actual_json == expected_json