from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

def test_put_v1_account_password():
    api = Facade(host='http://5.63.153.31:5051')
    login = "email_tes494"
    password = "email_tes494"
    email = "email_tes494@mail.ru"
    new_password = "new_" + password
    # - Регистрация пользователя
    api.account.register_new_user(login=login, email=email, password=password)
    # - Активация пользователя
    api.account.activate_registered_user(login=login)
    # - Авторизация пользователя, получение авторизационного токена
    token = api.login.get_auth_token(login=login, password=password)
    # - Сброс пароля с пробросом авторизационного токена в хэдэры (на почтовый сервер придет новое письмо с новым токеном, который будет необходим для сброса пароля)
    api.account.reset_registered_user_password(login=login, email=email, headers=token)
    # - Смена пароля с пробросом авторизационного токена в хэдэры и указанием токена для сброса пароля из письма
    api.account.change_registered_user_password(login=login, old_password=password, new_password=new_password, headers=token)
    #token api.account.get_reset_password_token(login=login, email=email, headers=token)

