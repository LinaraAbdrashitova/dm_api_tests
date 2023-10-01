import requests
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_delete_v1_account_login():
    api = Facade(host='http://5.63.153.31:5051')
    login = "email_tes495"
    password = "email_tes495"
    email = "email_tes495@mail.ru"
    # Регистрация пользователя
    api.account.register_new_user(login=login, email=email, password=password)
    # Активация пользователя
    api.account.activate_registered_user(login=login)
    # Авторизация пользователя, получение авторизационного токена
    token = api.login.get_auth_token(login=login, password=password)
    # Вызов метода разлогина с установленными заголовками в клиент или метод
    api.login.set_headers(headers=token)
    api.login.logout_user()