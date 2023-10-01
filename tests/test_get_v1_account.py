import requests
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)
def test_get_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "email_tes501"
    password = "email_tes501"
    email = "email_tes501@mail.ru"
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    # активация пользователя
    api.account.activate_registered_user(login=login)
    # авторизация пользователя и получение авторизационного токена
    token = api.login.get_auth_token(login=login, password=password)
    # получить информацию о пользователе
    api.account.set_headers(headers=token)
    api.account.get_current_user_info()



    # # Полученный токен проставляю во все апи: в апи account и login
    # api.account.set_headers(headers=token)
    # api.login.set_headers(headers=token)
    # api.account.get_current_user_info()
    # api.login.logout_user()
