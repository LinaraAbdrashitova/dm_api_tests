from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "email_tes498"
    email = "email_tes498@mail.ru"
    password = "email_tet498"
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    # api.login.login_user(
    #     login=login,
    #     password=password
    # )
