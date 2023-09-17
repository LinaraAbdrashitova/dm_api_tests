from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
import json
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole, Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

def test_put_v1_account_token():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    # json = Registration(
    #     login="email_test53",
    #     email="email_test53@mail.ru",
    #     password="email_test53"
    # )
    # response = api.account.post_v1_account(json=json)
    #
    # token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token='026a5961-b617-4c1a-aa7c-569a847897bf')
    assert_that(response.resource, has_properties(
        {
            "login": "email_tes54",
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